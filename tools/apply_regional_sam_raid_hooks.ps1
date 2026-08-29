param(
	[string[]]$Paths = @(
		'common/raids/air_raids.txt',
		'common/raids/bridge_strikes.txt',
		'common/raids/critical_military_infrastructure_strikes_raids.txt',
		'common/raids/energy_infrastructure_strikes_raids.txt'
	)
)

$ErrorActionPreference = 'Stop'
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$utf8Bom = New-Object System.Text.UTF8Encoding($true)

function Get-RaidBlocks([string]$Text) {
	$blocks = New-Object System.Collections.Generic.List[object]
	$depth = 0
	$inString = $false
	$escaped = $false
	$inComment = $false
	$lineStart = $true
	$currentName = $null
	$currentStart = -1

	for ($i = 0; $i -lt $Text.Length; $i++) {
		if ($lineStart -and -not $inString -and -not $inComment -and $depth -eq 1 -and -not $currentName) {
			$match = [regex]::Match($Text.Substring($i), '^\s*([A-Za-z0-9_]+)\s*=\s*\{')
			if ($match.Success) {
				$currentName = $match.Groups[1].Value
				$currentStart = $i
			}
		}

		$char = $Text[$i]
		if ($inComment) {
			if ($char -eq "`n") { $inComment = $false; $lineStart = $true } else { $lineStart = $false }
			continue
		}
		if ($inString) {
			if ($escaped) { $escaped = $false }
			elseif ($char -eq '\') { $escaped = $true }
			elseif ($char -eq '"') { $inString = $false }
			$lineStart = ($char -eq "`n")
			continue
		}
		if ($char -eq '#') { $inComment = $true; $lineStart = $false; continue }
		if ($char -eq '"') { $inString = $true; $lineStart = $false; continue }
		if ($char -eq '{') { $depth++ }
		elseif ($char -eq '}') {
			$depth--
			if ($currentName -and $depth -eq 1) {
				$blocks.Add([pscustomobject]@{ Name = $currentName; Start = $currentStart; End = $i + 1 })
				$currentName = $null
				$currentStart = -1
			}
		}
		$lineStart = ($char -eq "`n")
	}

	return $blocks
}

function Get-RaidClass([string]$Name) {
	if ($Name -match '_(bl|bs)$') { return 'ballistic' }
	if ($Name -match '_drones?$') { return 'air' }
	if ($Name -match '_rc$') { return 'cruise' }
	throw "Cannot classify raid '$Name'."
}

function Get-SuccessFactor([string]$Class, [string]$Indent, [string]$NewLine) {
	$upperClass = $Class.ToUpperInvariant()
	$weight = "@REGIONAL_SAM_${upperClass}_RAID_WEIGHT"
	$reference = "@REGIONAL_SAM_${upperClass}_RAID_REFERENCE"
	$key = "regional_sam_${Class}_defense"
	$variable = "SAM_${Class}_defense"
	$i1 = $Indent + "`t"
	$i2 = $i1 + "`t"
	$i3 = $i2 + "`t"

	return $NewLine +
		$Indent + "# Regional $Class defence from the raid target state." + $NewLine +
		$Indent + $key + ' = {' + $NewLine +
		$i1 + 'scope = state' + $NewLine +
		$i1 + 'formula = {' + $NewLine +
		$i2 + 'base = 1' + $NewLine +
		$i2 + 'modifier = {' + $NewLine +
		$i3 + "factor = var:$variable" + $NewLine +
		$i2 + '}' + $NewLine +
		$i1 + '}' + $NewLine +
		$i1 + "weight = $weight" + $NewLine +
		$i1 + "reference = $reference" + $NewLine +
		$i1 + 'can_actor_affect = no' + $NewLine +
		$i1 + 'can_target_affect = yes' + $NewLine +
		$Indent + '}' + $NewLine
}

foreach ($relativePath in $Paths) {
	$path = Join-Path (Get-Location) $relativePath
	$bytes = [System.IO.File]::ReadAllBytes($path)
	$hasBom = $bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF
	$text = [System.IO.File]::ReadAllText($path)
	$newLine = if ($text.Contains("`r`n")) { "`r`n" } else { "`n" }
	$blocks = @(Get-RaidBlocks $text)
	$modified = 0
	$modifierCount = 0
	$consumeCount = 0

	for ($index = $blocks.Count - 1; $index -ge 0; $index--) {
		$blockInfo = $blocks[$index]
		$block = $text.Substring($blockInfo.Start, $blockInfo.End - $blockInfo.Start)
		$class = Get-RaidClass $blockInfo.Name
		$key = "regional_sam_${class}_defense"
		$effect = "consume_state_SAM_ammunition_${class}"
		$successMatch = [regex]::Match($block, '(?ms)(success_factors\s*=\s*\{\s*success\s*=\s*\{\s*)([ \t]*base\s*=\s*[^\r\n]+\r?\n)')
		if (-not $successMatch.Success) { throw "No success factor insertion point in '$($blockInfo.Name)'." }
		$baseIndex = $successMatch.Groups[2].Index
		$baseLineStart = $block.LastIndexOf("`n", [Math]::Max(0, $baseIndex - 1)) + 1
		$baseIndent = $block.Substring($baseLineStart, $baseIndex - $baseLineStart)

		if (-not $block.Contains($key)) {
			$factor = Get-SuccessFactor $class $baseIndent $newLine
			$insertAt = $successMatch.Index + $successMatch.Length
			$block = $block.Insert($insertAt, $factor)
			$modifierCount++
		}

		if (-not $block.Contains($effect)) {
			$damageMatches = [regex]::Matches($block, '(?m)^([ \t]*)raid_damage_units\s*=\s*\{')
			if ($damageMatches.Count -ne 4) { throw "Expected 4 raid_damage_units blocks in '$($blockInfo.Name)', found $($damageMatches.Count)." }
			for ($damageIndex = $damageMatches.Count - 1; $damageIndex -ge 0; $damageIndex--) {
				$damageMatch = $damageMatches[$damageIndex]
				$indent = $damageMatch.Groups[1].Value
				$hook = $indent + 'var:target_state = {' + $newLine +
					$indent + "`t$effect = yes" + $newLine +
					$indent + '}' + $newLine
				$block = $block.Insert($damageMatch.Index, $hook)
				$consumeCount++
			}
		}

		$upperClass = $class.ToUpperInvariant()
		$factorPattern = "(?ms)($key\s*=\s*\{.*?\bweight\s*=\s*)[^\s#]+(\s+reference\s*=\s*)[^\s#]+"
		$factorReplacement = "`${1}@REGIONAL_SAM_${upperClass}_RAID_WEIGHT`${2}@REGIONAL_SAM_${upperClass}_RAID_REFERENCE"
		$block = [regex]::Replace($block, $factorPattern, $factorReplacement, 1)
		$unindentedFactor = [regex]::Match($block, "(?ms)^$key\s*=\s*\{\r?\n.*?^\}")
		if ($unindentedFactor.Success) {
			$indentedFactor = [regex]::Replace($unindentedFactor.Value, '(?m)^', $baseIndent)
			$block = $block.Remove($unindentedFactor.Index, $unindentedFactor.Length).Insert($unindentedFactor.Index, $indentedFactor)
			$unindentedComment = "# Regional $class defence from the raid target state."
			$block = $block.Replace($newLine + $unindentedComment, $newLine + $baseIndent + $unindentedComment)
		}

		$keyCount = [regex]::Matches($block, "(?m)^\s*$key\s*=").Count
		$effectCount = [regex]::Matches($block, "(?m)^\s*$effect\s*=\s*yes").Count
		$allKeyCount = [regex]::Matches($block, '(?m)^\s*regional_sam_(air|cruise|ballistic)_defense\s*=').Count
		$allEffectCount = [regex]::Matches($block, '(?m)^\s*consume_state_SAM_ammunition_(air|cruise|ballistic)\s*=\s*yes').Count
		if ($keyCount -ne 1 -or $allKeyCount -ne 1) {
			throw "Raid '$($blockInfo.Name)' must contain exactly one '$key' success factor."
		}
		if ($effectCount -ne 4 -or $allEffectCount -ne 4) {
			throw "Raid '$($blockInfo.Name)' must contain exactly four '$effect' outcome hooks."
		}

		if ($block -ne $text.Substring($blockInfo.Start, $blockInfo.End - $blockInfo.Start)) {
			$text = $text.Substring(0, $blockInfo.Start) + $block + $text.Substring($blockInfo.End)
			$modified++
		}
	}

	if (-not [regex]::IsMatch($text, '(?m)^@REGIONAL_SAM_AIR_RAID_WEIGHT\s*=')) {
		$constants =
			'@REGIONAL_SAM_AIR_RAID_WEIGHT = -0.4' + $newLine +
			'@REGIONAL_SAM_AIR_RAID_REFERENCE = 80' + $newLine +
			'@REGIONAL_SAM_CRUISE_RAID_WEIGHT = -0.45' + $newLine +
			'@REGIONAL_SAM_CRUISE_RAID_REFERENCE = 80' + $newLine +
			'@REGIONAL_SAM_BALLISTIC_RAID_WEIGHT = -0.5' + $newLine +
			'@REGIONAL_SAM_BALLISTIC_RAID_REFERENCE = 50' + $newLine + $newLine
		$text = $constants + $text
	}

	$encoding = if ($hasBom) { $utf8Bom } else { $utf8NoBom }
	[System.IO.File]::WriteAllText($path, $text, $encoding)
	Write-Output "${relativePath}: raids=$($blocks.Count), modified=$modified, factors=$modifierCount, hooks=$consumeCount"
}
