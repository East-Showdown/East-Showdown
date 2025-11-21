NDefines.NGame.START_DATE = "2022.1.1.1"
NDefines.NGame.END_DATE = "2026.1.1.1"
NDefines.NGame.MAP_SCALE_PIXEL_TO_KM = 0.514					-- Yes we did the math
NDefines.NGame.SAVE_VERSION = 18								-- 0.6.1.0
NDefines.NGame.HANDS_OFF_START_TAG = "URG"		-- tag for player country for -hands_off runs. use an existing tag that is less likely to affect the game
NDefines.NGame.TRADE_ROUTE_RECALCULATE_FREQUENCY_DAYS = 30 -- Max recalculation time for all trade routes (0 means we do not recalucate prediodically trade routes)
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_OPINION = 1.1                        -- Acceptance factor for opinion
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_OPINION = 1.0 -- Acceptance factor for opinion 
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_SAME_IDEOLOGY = 10 -- Acceptance value added if same ideology 
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_SCRIPTED_IDEOLOGY_ACCEPTANCE = 1.0 -- Acceptance factor for scripted ideology acceptance modifier 
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_TRADE_INFLUENCE = 0.50 -- Acceptance factor for trade influence (adjusted from base value) 
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_COMPETING_FACTIONS = -30 -- Acceptance value added if both countries are in factions and factions are different 
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_EMBARGO = -200 -- Acceptance value added if either side has embargoed the other 
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_OPINION = 1.0 -- Acceptance factor for opinion 
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_SAME_IDEOLOGY = 10 -- Acceptance value added if same ideology 
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_SCRIPTED_IDEOLOGY_ACCEPTANCE = 1.0 -- Acceptance factor for scripted ideology acceptance modifier 
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_TRADE_INFLUENCE = 0.50 -- Acceptance factor for trade influence (adjusted from base value) 
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_COMPETING_FACTIONS = -30 -- Acceptance value added if both countries are in factions and factions are different 
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_EMBARGO = -200 -- Acceptance value added if either side has embargoed the other 
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_NO_TRADE_ROUTE = -100                     -- Acceptance value added if there is no valid trade route between the countries
NDefines.NDiplomacy.MARKET_ACCESS_ACCEPTANCE_NON_AGGRESSION_PACT = 25                  -- Acceptance value added if there is a non-aggression pact between the countries
NDefines.NDiplomacy.EQUIPMENT_PURCHASE_ACCEPTANCE_NON_AGGRESSION_PACT = 25             -- Acceptance value added if there is a non-aggression pact between the countries
NDefines.NDiplomacy.TRUCE_PERIOD_AFTER_KICKING_FROM_FACTION = 30				-- Truce period after kicking someone from faction in days.
NDefines.NDiplomacy.PEACE_INCREASE_COST_FACTOR_PER_MISSING_PERCENT_FOR_CAPITULATION = 0.002 	-- increase factor if loser has not capitulated for every percent between surrender level and BASE_SURRENDER_LEVEL
NDefines.NDiplomacy.INFLUENCE_NEUTRAL_DIST_CAPITAL = 80.0           -- distance to capital that results in a cost modifier of 1.0
NDefines.NDiplomacy.INFLUENCE_MAX_DIST_CAPITAL = 100.0              -- distance to capital that results in a cost modifier of INFLUENCE_MAX_DIST_COST_MODIFIER
NDefines.NDiplomacy.INFLUENCE_NEUTRAL_DIST_CORE = 20.0              -- distance to nearest core state that results in a cost modifier of 1.0
NDefines.NDiplomacy.INFLUENCE_MAX_DIST_CORE = 30.0                 -- distance to nearest core state that results in a cost modifier of INFLUENCE_MAX_DIST_COST_MODIFIER
NDefines.NDiplomacy.INFLUENCE_NEUTRAL_DIST_CONTROLLED = 10.0        -- distance to nearest controlled state that results in a cost modifier of 1.0
NDefines.NDiplomacy.INFLUENCE_MAX_DIST_CONTROLLED = 14.0           -- distance to nearest controlled state that results in a cost modifier of INFLUENCE_MAX_DIST_COST_MODIFIER
NDefines.NDiplomacy.INFLUENCE_MIN_DIST_COST_MODIFIER = 0.80        -- Cost modifier at min (zero) distance
NDefines.NDiplomacy.INFLUENCE_MAX_DIST_COST_MODIFIER = 1.20         -- Cost modifier at max distance
NDefines.NDiplomacy.INFLUENCE_RATIO_CAPITAL = 0.2                  -- Ratio of influence based on distance to capital
NDefines.NDiplomacy.INFLUENCE_RATIO_CORE = 0.3                     -- Ratio of influence based on distance to nearest core territory
NDefines.NDiplomacy.INFLUENCE_RATIO_CONTROLLED = 0.5               -- Ratio of influence based on distance to neared controlled territory (including uncontested peace conference bids)
NDefines.NDiplomacy.INFLUENCE_DISTANCE_DIVISOR = 30.0              -- Divide pixel distance with this when determining distance to capital / core / controlled states. Just an arbitrary way of scaling the distance numbers.
NDefines.NDiplomacy.PEACE_TRIGGER_AI_MAX_INFLUENCE_VALUE = 0.99	-- Max influence value for pc_is_state_outside_influence_for trigger
NDefines.NDiplomacy.VOLUNTEERS_TRANSFER_SPEED = 4					-- days to transfer a unit to another nation
NDefines.NDiplomacy.TENSION_TIME_SCALE_START_DATE = "2022.1.1.1"	-- Starting at this date the tension values will be scaled down (will be equal to 1 before that)
NDefines.NDiplomacy.PEACE_SCORE_SCALE_FACTOR = 1.35                -- Losers' total value times this factor becomes the default total peace conference score that is distributed to the winners.
NDefines.NDiplomacy.PEACE_CONTEST_REFUND_FACTOR = { 1.0, 0.90, 0.80, 0.70 } -- How much of the spent peace conference score that gets refunded in a contest. First element applies for the first round of conflicts second element for the second round of conflicts etc. The final element is used for each consecutive turn so setting that to e.g. 0.7 means you get 70 % of the spent score back for every turn thereafter.
NDefines.NDiplomacy.LICENSE_ACCEPTANCE_OPINION_FACTOR = 0.2		-- Opinion modifier for acceptance of license production requests.  №№№№№№№№№№№
NDefines.NDiplomacy.LICENSE_ACCEPTANCE_PUPPET_BASE = 20			-- Acceptance modifier for puppets requesting production licenses.
NDefines.NDiplomacy.LICENSE_ACCEPTANCE_TECH_DIFFERENCE = 5 		-- Acceptance modifier for each year of technology difference.
NDefines.NDiplomacy.LICENSE_ACCEPTANCE_TECH_DIFFERENCE_BASE = 20    -- Acceptance base for tech difference
NDefines.NCountry.CONVOY_LENDLEASE_RANGE_FACTOR = 1				-- How much range affects convoy need for lend lease
NDefines.NCountry.CONVOY_INTERNATIONAL_MARKET_RANGE_FACTOR = 1	-- How much range affects convoy need for international market
NDefines.NCountry.CONVOY_RANGE_FACTOR = 1                        -- how much range affects convoy need
NDefines.NCountry.STARTING_COMMAND_POWER = 50					-- starting command power for every country
NDefines.NCountry.BASE_MAX_COMMAND_POWER = 400					-- base value for maximum command power
NDefines.NCountry.BASE_COMMAND_POWER_GAIN = 1					-- base value for daily command power gain
NDefines.NCountry.AIR_SUPPLY_CONVERSION_SCALE = 0.17 -- 0.01
NDefines.NCountry.SPECIAL_FORCES_CAP_BASE = 0.04					-- Max ammount of special forces battalions is total number of non-special forces battalions multiplied by this and modified by a country modifier
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 36					-- You can have a minimum of this many special forces battalions regardless of the number of non-special forces battalions you have this can also be modified by a country modifier
NDefines.NResistance.GARRISON_MANPOWER_LOST_BY_ATTACK = 0.016 	-- Ratio of manpower lost by garrison at each attack on garrison (this number will be reduced by the hardness of garrison template)
NDefines.NProduction.CIC_BANK_SPEED_BOOST_FACTOR = 0.25                 -- The CIC bank can boost production speed with this factor (0.5 means 50 %)
NDefines.NProduction.MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_VALUE = 1		-- The minimum number of factories we have to put on consumer goods by value.
NDefines.NProduction.MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_PERCENT = 0.1	-- The minimum number of factories we have to put on consumer goods in percent.
NDefines.NProduction.BASE_FACTORY_SPEED = 2 				-- Base factory speed multiplier (how much hoi3 style IC each factory gives).
NDefines.NProduction.MAX_EQUIPMENT_RESOURCES_NEED = 6 -- vanila 3 Max number of different strategic resources an equipment can be dependent on.
NDefines.NProduction.BASE_LAND_EQUIPMENT_CONVERSION_IC_COST_FACTOR = 0.1 -- vanilla 0.9, Fraction of the chassis industry cost which is always included in the conversion cost.
NDefines.NPolitics.BASE_POLITICAL_POWER_INCREASE = 5	-- Weekly increase of PP.
NDefines.NBuildings.MAX_BUILDING_LEVELS = 50			-- Max levels a building can have.
NDefines.NBuildings.AIRBASE_CAPACITY_MULT = 50		-- Each level of airbase building multiplied by this gives capacity (max operational value). Value is int. 1 for each airplane.
NDefines.NBuildings.RADAR_RANGE_BASE = 224				-- Radar range base first level radar will be this + min best radar will be this + max
NDefines.NBuildings.RADAR_RANGE_MIN = 256				-- Radar range (from state center to province center) in measure of map pixels. Exluding techs.
NDefines.NBuildings.RADAR_RANGE_MAX = 840				-- Range is interpolated between building levels 1-15.
NDefines.NBuildings.RADAR_INTEL_EFFECT = 100			-- Province covered by radar increases intel by 10 (where 255 is max). Province may be covered by multiple radars then the value sums up.
NDefines.NBuildings.BASE_FACTORY_REPAIR = 0.3			-- Default repair rate before factories are taken into account
NDefines.NBuildings.BASE_FACTORY_REPAIR_FACTOR = 1.8	-- Factory speed modifier when repairing.
NDefines.NBuildings.SUPPLY_PORT_LEVEL_THROUGHPUT = 5   -- vanilla 3 supply throughput per level of naval base lancaster
NDefines.NBuildings.MAX_SHARED_SLOTS = 50				-- Max slots shared by factories
NDefines.NMilitary.MIN_DIVISION_BRIGADE_HEIGHT = 4		-- Min height of regiments in division designer.
NDefines.NMilitary.DIVISIONAL_COMMANDER_TRAIT_XP_REQUIREMENT = 600.0	--Get a trait if any valid options & xp gained >= this
NDefines.NMilitary.MAX_DIVISION_SUPPORT_WIDTH = 2
NDefines.NMilitary.MAX_DIVISION_SUPPORT_HEIGHT = 6
NDefines.NMilitary.DIVISIONAL_COMMANDER_RANK_XP_THRESHOLD = { 		-- XP thresholds for divisional commander ranks. [TAG]_DIVISION_EXPERIENCE_TITLE_ARMY_EXPERIENCE_[array index]
0,
100.0,
300.0,
600.0,
1000.0
}
NDefines.NMilitary.HOURLY_ORG_MOVEMENT_IMPACT = -0.2		--vanila -0.2 how much org is lost every hour while moving an army.
NDefines.NMilitary.ZERO_ORG_MOVEMENT_MODIFIER = -0.8		-- speed impact at 0 org.
NDefines.NMilitary.INFRA_ORG_IMPACT = 0.5				-- коэффициент масштабирования инфры на орг. рег.
NDefines.NMilitary.ENGAGEMENT_WIDTH_PER_WIDTH = 2.0	-- how much enemy combat width we are allowed to engage per width of our own
NDefines.NMilitary.FIELD_EXPERIENCE_ON_DIVISION_MULT = 0.03	-- Multiply field experience gained by this when applying to divisional commander
NDefines.NMilitary.WAR_SCORE_AIR_IC_LOSS_FACTOR = 0.1							-- war score gained for every IC of damage done to an enemy's air mission
NDefines.NMilitary.WAR_SCORE_LAND_DAMAGE_FACTOR = 0.1          				-- war score gained for every strengh damage done to an enemy's army
NDefines.NMilitary.WAR_SCORE_ATTACKER_AND_WINNER_FACTOR = 1.2					-- factor applied to war score gained for strength damage done when being the attacker and the winner
NDefines.NMilitary.WAR_SCORE_LAND_IC_LOSS_FACTOR = 0.1         				-- war score gained for every IC damage done to an enemy's army
NDefines.NMilitary.WAR_SCORE_PROVINCE_FACTOR = 2.0							-- war score gained when capturing a province for the first time multiplied by province's worth
NDefines.NMilitary.WAR_SCORE_LEND_LEASE_GIVEN_IC_FACTOR = 0.001  				-- war score gained for every IC of lend lease sent to allies
NDefines.NMilitary.WAR_SCORE_LEND_LEASE_GIVEN_FUEL_FACTOR = 0.001  			-- war score gained for every 100 units of fuel lend lease sent to allies
NDefines.NMilitary.WAR_SCORE_LEND_LEASE_RECEIVED_IC_FACTOR = 0.001  			-- war score deducted for every IC of lend lease received from allies
NDefines.NMilitary.WAR_SCORE_LEND_LEASE_RECEIVED_FUEL_FACTOR = 0.001 		-- war score deducted for every 100 units of fuel lend lease received from allies
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 50			-- how many divisions a corps commander is limited to. 0 = inf < 0 = blocked
NDefines.NMilitary.DIVISION_SIZE_FOR_XP = 8                   -- how many battalions should a division have to count as a full divisions when calculating XP stuff
NDefines.NMilitary.CORPS_COMMANDER_ARMIES_CAP = -1			-- how many armies a corps commander is limited to. 0 = inf < 0 = blocked
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 100			-- how many divisions a field marshall is limited to. 0 = inf < 0 = blocked
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = 10				-- how many armies a field marshall is limited to. 0 = inf < 0 = blocked
NDefines.NMilitary.LAND_AIR_COMBAT_STR_DAMAGE_MODIFIER = 0.036    -- was 0.025 pre air attack changes 0.032 vanilla   air global damage modifier
NDefines.NMilitary.LAND_AIR_COMBAT_ORG_DAMAGE_MODIFIER = 0.036    --was 0.030 pre air attack changes 0.032 vanilla   global damage modifie
NDefines.NMilitary.AIR_SUPPORT_BASE = 0.10-- 0.25 vanilla
NDefines.NAir.AIR_WING_MAX_STATS_ATTACK = 500 -- 100
NDefines.NAir.AIR_WING_MAX_STATS_DEFENCE = 500 -- 100
NDefines.NAir.AIR_WING_MAX_STATS_AGILITY = 500 -- 100
NDefines.NAir.AIR_WING_MAX_STATS_SPEED = 3000 -- 800
NDefines.NAir.AIR_WING_MAX_STATS_BOMBING = 1000 -- 100
NDefines.NAir.DETECT_CHANCE_FROM_AIRCRAFTS_EFFECTIVE_COUNT = 600 -- 3000
NDefines.NAir.COMBAT_DAMAGE_SCALE = 0.15 -- 1 vanilla Higher value = more shot down planes
NDefines.NAir.AIR_WING_XP_TRAINING_MISSION_ACCIDENT_FACTOR = 0.01 -- 0.20
NDefines.NAir.DISRUPTION_FACTOR = 1 -- 4.0
NDefines.NMilitary.LAND_AIR_COMBAT_MAX_PLANES_PER_ENEMY_WIDTH = 1 -- vanial 3 how many CAS/TAC can enter a combat depending on enemy width there
NDefines.NMilitary.ATTRITION_DAMAGE_ORG = 0.08					   -- vanila 0.08 ущерб от истощения Организации
NDefines.NMilitary.ATTRITION_EQUIPMENT_LOSS_CHANCE = 0.025		    -- #0.1 Chance for loosing equipment when suffer attrition. Scaled up the stronger attrition is. Then scaled down by equipment reliability.
NDefines.NMilitary.ATTRITION_EQUIPMENT_PER_TYPE_LOSS_CHANCE = 0.025 -- #0.1  Chance for loosing equipment when suffer attrition. Scaled up the stronger attrition is. Then scaled down by equipment reliability.
NDefines.NMilitary.COMBAT_MOVEMENT_SPEED = 0.33	               -- vanila 0.33 speed reduction base modifier in combat
NDefines.NMilitary.SUPPLY_USE_FACTOR_MOVING = 1.5                -- Deprecated/Unused
NDefines.NMilitary.SUPPLY_USE_FACTOR_INACTIVE = 0.95			   -- Deprecated/Unused
NDefines.NMilitary.SUPPLY_GRACE = 72							   -- troops always carry 3 days of food and supply
NDefines.NMilitary.SUPPLY_GRACE_MAX_REDUCE_PER_HOUR = 2          -- supply grace is not decreased instantly when it is buffed temporarily and buff is removed
NDefines.NMilitary.SUPPLY_ORG_MAX_CAP = 0.30                     -- vanilla 0.35 Максимальная организация учитывается по этому показателю если полностью отсутствует снабжение
NDefines.NMilitary.MAX_OUT_OF_SUPPLY_DAYS = 20 				   -- #was 30 how many days of shitty supply until max penalty achieved
NDefines.NMilitary.OUT_OF_SUPPLY_ATTRITION = 0.20                 -- max attrition when out of supply
NDefines.NMilitary.OUT_OF_SUPPLY_SPEED = -0.8                    -- max speed reduction from supply
NDefines.NMilitary.NON_CORE_SUPPLY_SPEED = -0.5				   -- we are not running on our own VP supply so need to steal stuff along the way
NDefines.NMilitary.NON_CORE_SUPPLY_AIR_SPEED = -0.25			   -- we are not running on our own VP supply so need to steal stuff along the way a bit less due to air supply
NDefines.NMilitary.OUT_OF_SUPPLY_MORALE = -0.2                   -- max org regain reduction from supply
NDefines.NMilitary.LOW_SUPPLY = 0.99							   -- When the supply status of an unit becomes low.
NDefines.NMilitary.COMBAT_SUPPLY_LACK_ATTACKER_ATTACK = -0.25     -- attack combat penalty for attacker if out of supply
NDefines.NMilitary.COMBAT_SUPPLY_LACK_ATTACKER_DEFEND = -0.65     -- defend combat penalty for attacker if out of supply
NDefines.NMilitary.COMBAT_SUPPLY_LACK_DEFENDER_ATTACK = -0.35     -- attack combat penalty for defender if out of supply
NDefines.NMilitary.COMBAT_SUPPLY_LACK_DEFENDER_DEFEND = -0.15     -- defend combat penalty for defender if out of supply
NDefines.NMilitary.AVERAGE_SUPPLY_USE_PESSIMISM = 1.5					-- Multiplier for when AI calculates average supply use of entire army.
NDefines.NMilitary.LAND_SPEED_MODIFIER = 0.45                    -- vanila 0.5 basic speed control скорость дивок
NDefines.NMilitary.BASE_FORT_PENALTY = -0.15 					   -- vanilla -0.15 fort penalty
NDefines.NMilitary.MULTIPLE_COMBATS_PENALTY = -0.5               -- defender penalty if attacked from multiple directions
NDefines.NMilitary.DIG_IN_FACTOR = 0.03						   --vanila 0.02 bonus factor for each dug-in level
NDefines.NMilitary.ARMY_LEADER_XP_GAIN_PER_UNIT_IN_COMBAT = 0.1 -- #was 0.1 XP gain per unit in combat
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_IMPACT = -0.6          -- #was -0.35 effect on defense due to enemy air superiorty
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_DEFENSE = 0.20	       -- more AA attack will approach this amount of help (diminishing returns)
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_DEFENSE_STEEPNESS = 112 -- how quickly defense approaches the max impact diminishing returns curve
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_SPEED_IMPACT = -0.3     -- vanila 0.3 effect on speed due to enemy air superiority
NDefines.NMilitary.ANTI_AIR_TARGETTING_TO_CHANCE = 0.02			-- Balancing value to determine the chance of ground AA hitting an attacking airplane affecting both the effective average damage done by AA to airplanes and the reduction of damage done by airplanes due to AA support
NDefines.NMilitary.ANTI_AIR_ATTACK_TO_AMOUNT = 0				-- Balancing value to convert equipment stat anti_air_attack to the random % value of airplanes being hit.
NDefines.NMilitary.ENCIRCLED_PENALTY = -0.30                      	-- #was -0.3 penalty when completely encircled когда окружили
NDefines.NMilitary.UNIT_EXP_LEVELS = { 0.1, 0.3, 0.6, 0.8 }		-- Experience needed to progress to the next level
NDefines.NMilitary.EQUIPMENT_COMBAT_LOSS_FACTOR = 0.70	 	   -- % was 0.70 (lancaster)of equipment lost to strength ratio in combat so some % is returned if below 1
NDefines.NMilitary.ORG_LOSS_FACTOR_ON_CONQUER = 0.1              -- percentage of (max) org loss on takign enemy province
NDefines.NMilitary.COMBAT_STACKING_START = 8						-- at what nr of divisions stacking penalty starts
NDefines.NMilitary.COMBAT_STACKING_EXTRA = 4                      -- extra stacking from directions
NDefines.NMilitary.STRATEGIC_SPEED_RAIL_BASE = 40.0               -- Base speed of strategic redeployment when on railways
NDefines.NMilitary.STRATEGIC_SPEED_RAIL_MAX = 60.0                -- Additional speed of strategic redeployment on max-level railways
NDefines.NMilitary.PROMOTE_LEADER_CP_COST = 20.0					-- cost of promoting a leader
NDefines.NMilitary.UNIT_LEADER_MODIFIER_COOLDOWN_ON_GROUP_CHANGE = 3		-- time in days for a unit leader to regain its modifiers
NDefines.NMilitary.UNIT_LEADER_ASSIGN_TRAIT_COST = 5.0					-- cost to assign a new trait to a unit leader
NDefines.NMilitary.FUEL_FLOW_PENALTY_FOR_SUPPLY_CHUNK_EDGE_RATIO = 0.5 -- поток питания ограниченный контролем входящих краевых провинций будет иметь меньшее влияние на поток топлива
NDefines.NMilitary.OUT_OF_FUEL_EQUIPMENT_MULT = 0.1				-- 0.1 vanilla ratio of the stats that you get from equipments that uses fuel and you lack it
NDefines.NMilitary.OUT_OF_FUEL_SPEED_MULT = 0.4					-- vanilla 0.4 speed mult that armies get when out of fuel
NDefines.NMilitary.OUT_OF_FUEL_TRAINING_XP_GAIN_MULT = 0.0		-- xp gain mult from training when a unit is out of fuel
NDefines.NMilitary.FUEL_CAPACITY_DEFAULT_HOURS = 96				-- 96 vanilla default capacity if not specified
NDefines.NAir.PORT_STRIKE_DAMAGE_FACTOR = 1.0								-- How much damage is dealt to ports during a port strike (per plane damage [complex number] * num flying planes * define)
NDefines.NAir.THRUST_WEIGHT_AGILITY_FACTOR = 0.5								-- For plane designs additive agility bonus per point of thrust exceeding weight
NDefines.NAir.AIR_WING_MAX_SIZE = 20 							-- Max amount of airplanes in wing
NDefines.NAir.AIR_WING_AVERAGE_SIZE = 20 						-- Eyeballed average amount of airplanes in wing. Used when calculating air volunteer.
NDefines.NAir.AIR_WING_BOMB_DAMAGE_FACTOR = 2					-- Used to balance the damage done while bombing.
NDefines.NAir.BIGGEST_AGILITY_FACTOR_DIFF = 3.0					-- biggest factor difference in agility for doing damage (caps to this)
NDefines.NAir.BIGGEST_SPEED_FACTOR_DIFF = 2.5					-- biggest factor difference in speed for doing damage (caps to this)
NDefines.NAir.TOP_SPEED_DAMAGE_BONUS_FACTOR = 0.025				-- A factor for scaling the top speed of a plane into damage buff. If an attacking wing has a speed advantage of any form their speed value will be converted into a percentage bonus with this modifier
NDefines.NAir.COMBAT_DAMAGE_STATS_MULTILPIER = 0.2
NDefines.NAir.COMBAT_BETTER_AGILITY_DAMAGE_REDUCTION = 0.30 		-- How much the better agility (than opponent's) can reduce their damage to us.
NDefines.NAir.COMBAT_BETTER_SPEED_DAMAGE_INCREASE = 0.60 		-- How much the better Speed (than opponent's) can reduce increase our damage to them.
NDefines.NAir.NAVAL_STRIKE_CARRIER_MULTIPLIER = 5.0              -- damage bonus when planes are in naval combat where their carrier is present (and can thus sortie faster and more effectively)
NDefines.NAir.ACCIDENT_CHANCE_BASE = 0.05							-- Base chance % (0 - 100) for accident to happen. Reduced with higher reliability stat.
NDefines.NAir.ACCIDENT_CHANCE_CARRIER_MULT = 2.0					-- The total accident chance is scaled up when it happens on the carrier ship.
NDefines.NAir.ACCIDENT_CHANCE_BALANCE_MULT = 0.5					-- Multiplier for balancing how often the air accident really happens. The higher mult the more often.
NDefines.NAir.ACCIDENT_EFFECT_MULT = 0.005						-- Multiplier for balancing the effect of accidents
NDefines.NAir.ACE_DEATH_CHANCE_BASE = 0.003						-- Base chance % for ace pilot die when an airplane is shot down in the Ace wing.
NDefines.NAir.ACE_DEATH_BY_OTHER_ACE_CHANCE = 1.0				-- chance to an ace dying by another ace if it was hit by ace in combat
NDefines.NAir.ACE_DEATH_CHANCE_PLANES_MULT = 0.001				-- The more airplanes was lost in a single airplanes (more bloody it was) the higher chance of Ace to die.
NDefines.NAir.AIR_AGILITY_TO_NAVAL_STRIKE_AGILITY = 0.01         		-- conversion factor to bring agility in line with ship AA
NDefines.NAir.ACE_WING_SIZE =	20								-- size of wing ace bonuses are set up for. if lower more bonus if higher less bonus
NDefines.NAir.AA_INDUSTRY_AIR_DAMAGE_FACTOR = -0.05				-- 5x levels = 60% defense from bombing
NDefines.NAir.NAVAL_STRIKE_DETECTION_BALANCE_FACTOR = 0.7		-- Value used to scale the surface_visibility stats to balance the gameplay so 100% detection chance still won't spam the strikes.
NDefines.NAir.NAVAL_RECON_DETECTION_BALANCE_FACTOR = 0.7			-- Value used to scale the surface_visibility stats to balance the gameplay so 100% detection chance still won't spam spotting.
NDefines.NAir.AIR_MORE_GROUND_CREWS_COST = 5.0					-- CP cost to maintain more ground crews
NDefines.NAir.AIR_WING_XP_TRAINING_MISSION_GAIN_DAILY = 3.0 						--Daily gain when running training exercise mission
NDefines.NAir.MISSION_COMMAND_POWER_COSTS = {  -- command power cost per plane to create a mission
1.5, -- AIR_SUPERIORITY
1.5, -- CAS
1.0, -- INTERCEPTION
0.0, -- STRATEGIC_BOMBER
0.0, -- NAVAL_BOMBER
0.0, -- DROP_NUKE
0.0, -- PARADROP
0.0, -- NAVAL_KAMIKAZE
0.0, -- PORT_STRIKE
0.0, -- ATTACK_LOGISTICS
0.2, -- AIR_SUPPLY
0.0, -- TRAINING
0.0, -- NAVAL_MINES_PLANTING
0.0, -- NAVAL_MINES_SWEEPING
0.1, -- RECON
0.0 -- NAVAL_PATROL
}
NDefines.NAir.THRUST_WEIGHT_SPEED_FACTOR = 3								-- For plane designs additive Km/h max speed bonus per point of thrust exceeding weight
NDefines.NNavy.RESOURCE_PURCHASE_PRIORITY = 6									-- Default convoy priority for export equipment purchase
NDefines.NNavy.NAVY_PIERCING_THRESHOLD_DAMAGE_VALUES = {	-- 0 armor will always receive maximum damage (so add overmatching at your own peril). the system expects at least 2 values with no upper limit.
1.00,
1.00,
0.70,
0.40,
0.30,
0.10 -- 
}
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_MANPOWER_FACTOR = 0.001			-- war score gained for every manpower killed when sinking a ship
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_SHIP_PRODUCTION_COST_FACTOR = 0.004		-- war score gained for every IC of the sunk ship
NDefines.NNavy.WAR_SCORE_GAIN_FOR_SUNK_CONVOY = 0.05							-- war score gained for every sunk convoy
NDefines.NNavy.WAR_SCORE_DECAY_FOR_BUILT_CONVOY = 0.03  						-- war score deducted when convoy-raided enemy produces one new convoy
NDefines.NNavy.COMBAT_ARMOR_PIERCING_DAMAGE_REDUCTION = -0.9					-- All damage reduction % when target armor is >= then shooter armor piercing.
NDefines.NNavy.AMPHIBIOUS_LANDING_PENALTY = -0.1								-- amphibious landing penalty
NDefines.NNavy.AMPHIBIOUS_INVADE_ATTACK_LOW = 0.8 							-- low and high cap of attack modifier scale. Scale interpolated by invasion progress.
NDefines.NNavy.NAVAL_SPEED_MODIFIER = 2.0	                    				-- basic speed control
NDefines.NNavy.NAVAL_MINES_INTEL_DIFF_FACTOR = 0.1					-- Better our decryption over enemy encryption will reduce the penalties from the enemy mines in the region. This value is a factor to be used for balancing.
NDefines.NNavy.NAVAL_MINES_ACCIDENT_STRENGTH_LOSS = 75.0						-- Amount of strength loss when hit by naval mine
NDefines.NNavy.NAVAL_MINES_ACCIDENT_ORG_LOSS_FACTOR = 0.6						-- Amount of strength loss when hit by naval mine
NDefines.NNavy.AIR_SPOTTER_NORMALIZED_AIRWING_SIZE = 20						-- each plane will contribute 1/this of the air-wing's detection stat
NDefines.NNavy.BASE_JOIN_COMBAT_HOURS						= 8				-- the taskforces that wants to join existing combats will wait for at least this amount
NDefines.NNavy.ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE								= 0.25	-- received air damage is calculated using following: 1 - ( (ship_anti_air + fleet_anti_air * SHIP_TO_FLEET_ANTI_AIR_RATIO )^ANTI_AIR_POW_ON_INCOMING_AIR_DAMAGE ) * ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE
NDefines.NNavy.ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE							= 0.2
NDefines.NNavy.GUN_HIT_PROFILES = { -- hit profiles for guns if target ih profile is lower the gun will have lower accuracy
80.0,	-- big guns
145.0,	-- torpedoes
45.0	-- small guns
}
NDefines.NNavy.CONVOY_HIT_PROFILE												= 120.0  	-- convoys has this contant hit profile
NDefines.NNavy.HIT_PROFILE_MULT 												= 100.0  	-- multiplies hit profile of every ship
NDefines.NNavy.HIT_PROFILE_SPEED_FACTOR										= 2		-- factors speed value when determining it profile (Vis * HIT_PROFILE_MULT * Ship Hit Profile Mult)
NDefines.NRailwayGun.DISTRIBUTION_HOLD_POSITION_SCORE = 35							-- Score for staying in the same province when distributing Railway Guns
NDefines.NAI.DIPLOMACY_PURCHASE_EQUIPMENT_MONTHS = 2
NDefines.NAI.EQUIPMENT_MARKET_UPDATE_FREQUENCY_DAYS = 11                    -- How often the AI runs its market logic
NDefines.NAI.EQUIPMENT_MARKET_MAX_CIVS_FOR_PURCHASES_RATIO = 0.1            -- Ratio of available civilian factories to max use for equipment purchases (0.2 = 20 % so 50 available civs would mean max ca 10 civs to spend on purchases at any one time). Gets modified by equipment_market_spend_factories AI strategy.
NDefines.NAI.EQUIPMENT_MARKET_BASE_MARKET_RATIO = 0.2                       -- The AI tries to keep ca this ratio of equipment surplus for sale on the market. Gets modified by equipment_market_for_sale_factor AI strategy.
NDefines.NAI.EQUIPMENT_MARKET_DEFAULT_CIC_CHUNK_FOR_SALE = 150.0            -- When putting things up for sale on the market this determines the default "chunk" size of equipment the AI puts up. Gets overridden by equipment_market_min_for_sale AI strategy. (If one equipment is worth 5 CIC a value of 150 would result in chunk sizes of 150/5 = 30 units)
NDefines.NAI.EQUIPMENT_MARKET_NR_DELIVERIES_SOFT_MAX = 10                   -- AI tries to adjust assigned factories and amount of equipment to keep nr deliveries at max this
NDefines.NAI.EQUIPMENT_MARKET_EXTRA_CONVOYS_OVERRIDE = 2                    -- Makes the AI able to buy convoys even if they are lacking free convoys. 0 will make them stop this behavior anything > 0 will allow overriding the perceived nr of free convoys. Only if convoy equipment has a non-zero weight does the actual value matter.
NDefines.NAI.EQUIPMENT_MARKET_CONTRACT_DURATION_ACCEPTANCE = -10            -- If expected contract duration is longer than EQUIPMENT_MARKET_NR_DELIVERIES_SOFT_MAX deliveries then add this to the PurchaseContract AI acceptance score per nr overdue deliveries
NDefines.NAI.EQUIPMENT_MARKET_CONTRACT_EFFICIENCY_TO_CANCEL = 0.1           -- If contract efficiency stays below this the AI will cancel the contract
NDefines.NAI.EQUIPMENT_MARKET_EQUIPMENT_SUNK_TO_CANCEL = 0.5                -- If more equipment is sunk then the given percentage the AI will cancel the contract
NDefines.NAI.EQUIPMENT_MARKET_SHORTAGE_DAYS_TO_CANCEL = 30                  -- If equipment deficit will take more than these many days to fix the AI will cancel the contract
NDefines.NAI.EQUIPMENT_MARKET_MAX_CONVOY_RATIO_FOR_MARKET_PEACE = 0.5       -- Max ratio of total convoys to use for equipment trade while at peace
NDefines.NAI.EQUIPMENT_MARKET_MAX_CONVOY_RATIO_FOR_MARKET_WAR = 0.25        -- Max ratio of total convoys to use for equipment trade while at war
NDefines.NAI.EQUIPMENT_MARKET_SCORE_FACTOR_VARIANT_SCORE = 5.0              -- Score coefficient for VariantScore (high is good)
NDefines.NAI.EQUIPMENT_MARKET_SCORE_FACTOR_CIC_VALUE_NEEDED = 8.0           -- Score coefficient for CicValueNeeded (high is prio)
NDefines.NAI.EQUIPMENT_MARKET_SCORE_FACTOR_SUBSIDY_VALUE = 2.0              -- Score coefficient for SubsidyValue (high is good)
NDefines.NAI.EQUIPMENT_MARKET_SCORE_FACTOR_COST_PER_UNIT = -5.0             -- Score coefficient for SubsidizedCostPerUnit (low is good)
NDefines.NAI.EQUIPMENT_MARKET_SCORE_FACTOR_AI_STRAT_WEIGHT = 50.0           -- Score coefficient for AiStratWeight (high is prio)
NDefines.NAI.EQUIPMENT_MARKET_SCORE_FACTOR_DIPLO_OPINION = 1.0              -- Score coefficient for DiploOpinion mainly used as tie breaker (high is good)
NDefines.NAI.AI_WANTED_LAND_BASED_PLANES_FACTOR = 0.50		-- Factor applied to desire for land based planes (total airbase space * define)
NDefines.NAI.AI_WANTED_CARRIER_BASED_PLANES_FACTOR = 1.0	-- Factor applied to desire for carrier based planes (total carrier space * define)
NDefines.NAI.CONSTRUCTION_PRIO_INFRASTRUCTURE = 0.20                                    -- base prio for infrastructure in the construction queue
NDefines.NAI.CONSTRUCTION_PRIO_CIV_FACTORY = 0.80                                       -- base prio for civilian factories in the construction queue
NDefines.NAI.CONSTRUCTION_PRIO_MIL_FACTORY = 0.70                                       -- base prio for military factories in the construction queue
NDefines.NAI.CONSTRUCTION_PRIO_RAILWAY = 4.00                                           -- base prio for railways in the construction queue
NDefines.NAI.CONSTRUCTION_PRIO_RAILWAY_GUN_REPAIR = 15.00                               -- base prio for railway gun repairs in the construction queue
NDefines.NAI.CONSTRUCTION_PRIO_UNSPECIFIED = 0.50                                       -- base prio for unspecified buildings (none of the categories above) in the construction queue
NDefines.NAI.CONSTRUCTION_PRIO_FACTOR_OCCUPIED_TERRITORY = 1.00                         -- factor prio with this if occupied territory
NDefines.NAI.CONSTRUCTION_PRIO_FACTOR_OWNED_NONCORE = 1.50                              -- factor prio with this if owned non-core territory
NDefines.NAI.CONSTRUCTION_PRIO_FACTOR_OWNED_CORE = 2.00                                 -- factor prio with this if owned core territory
NDefines.NAI.CONSTRUCTION_PRIO_FACTOR_REPAIRING = 0.30                                  -- factor prio with this if building is being repaired
NDefines.NAI.INDUSTRIAL_ORG_TRAIT_UNLOCK_RANDOMNESS = 3		-- AI will pick a random from N top traits when choosing a trait to unlock
NDefines.NAI.INDUSTRIAL_ORG_POLICY_CHANGE_RANDOMNESS = 3	-- AI will pick a random from N top policies when choosing a policy to attach to an MIO
NDefines.NAI.INDUSTRIAL_ORG_RESEARCH_ASSIGN_RANDOMNESS = 3	-- AI will pick a random from N top MIOs when choosing an MIO to assign to a research
NDefines.NAI.INDUSTRIAL_ORG_PRODUCTION_ASSIGN_RANDOMNESS = 3-- AI will pick a random from N top MIOs when choosing an MIO to assign to a production line
NDefines.NAI.INDUSTRIAL_ORG_POLICY_CHANGE_SCALE = 1.0		-- Policy change weight will be scaled by this value
NDefines.NAI.INDUSTRIAL_ORG_TRAIT_RANK_FACTOR = 0.80		-- When precomputing weights traits will affect the final score less the further down the tree they are by this factor
NDefines.NAI.INDUSTRIAL_ORG_RESEARCH_BONUS_FACTOR = 1.0		-- Research bonus will be multiplied by this factor when evaluating design teams
NDefines.NAI.MIN_POLITICAL_POWER_MONTHLY_GAIN_FOR_IMPROVE_RELATIONS = 0.50	-- If country makes less than this PP per month they won't improve relations
NDefines.NAI.RESEARCH_NEW_WEIGHT_FACTOR = 0.3 			-- Impact of previously unexplored tech weights. Higher means more random exploration.
NDefines.NAI.RESEARCH_AHEAD_BONUS_FACTOR = 2.0          -- To which extent AI should care about ahead of time bonuses to research
NDefines.NAI.RESEARCH_BONUS_FACTOR = 0.9 				-- To which extent AI should care about bonuses to research
NDefines.NAI.MAX_AHEAD_RESEARCH_PENALTY = 2             -- max ahead of tiem penalty ai will pick ever
NDefines.NAI.PRODUCTION_EQUIPMENT_SURPLUS_FACTOR = 0.4	-- Base value for how much of currently used equipment the AI will at least strive to have in stock
NDefines.NAI.DEFAULT_MODULE_VARIANT_CREATION_XP_CUTOFF_LAND = 50	-- Army XP needed before attempting to create a variant of a type that uses the tank designer (the tank designer DLC feature must be active).
NDefines.NAI.DEFAULT_LEGACY_VARIANT_CREATION_XP_CUTOFF_LAND = 50	-- Army XP needed before attempting to create a variant of a type that uses the legacy upgrades system. ai_strategy supports land_xp_spend_priority upgrade_xp_cutoff. If none is set this define is used instead.
NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_ARMY_SPIRIT = 0.4    -- How quickly is desire to unlock army spirits accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_NAVY_SPIRIT = 0.4   -- How quickly is desire to unlock naval spirits accumulated?
NDefines.NAI.DESIRE_USE_XP_TO_UNLOCK_AIR_SPIRIT = 0.4     -- How quickly is desire to unlock air spirits accumulated?
NDefines.NAI.MIN_AI_UNITS_PER_TILE_FOR_STANDARD_COHESION = 2.0	-- How many units should we have for each tile along a front in order to switch to standard cohesion (less moving around)
NDefines.NAI.MIN_FRONT_SIZE_TO_CONSIDER_STANDARD_COHESION = 20	-- How long should fronts be before we consider switching to standard cohesion (under this standard cohesion fronts will switch back to relaxed)
NDefines.NAI.DEFAULT_SUPPLY_TRAIN_NEED_FACTOR = 1.5     -- AI multiplies current train usage by this to determine desired nr of wanted trains. Can be modified by wanted_supply_train min_wanted_supply_trains ai strats.
NDefines.NAI.POLITICAL_IDEA_MIN_SCORE = 0.1				-- Only replace or add an idea if score is above this score.
NDefines.NAI.HIGH_COMMAND_ADDED_WEIGHT_FACTOR = 1.0		-- Weight multiplier for high_command advisors over other chosen advisor or idea types
NDefines.NAI.EVAL_MODIFIER_MAX_COMMAND_POWER_FACTOR = 0.02                -- Increasing CP cap with x is maybe 100 times less useful than e.g. gaining x more XP per day
NDefines.NAI.AT_WAR_THREAT_FACTOR = 2.0					-- How much increase in threat does AI feel for being in war against osmeone
NDefines.NAI.NEIGHBOUR_WAR_THREAT_FACTOR = 1.10 		-- How much increase in threat does AI feel against neighbours who are at war
NDefines.NAI.POTENTIAL_ALLY_JOIN_WAR_FACTOR = 100 		-- How much increase in threat does AI feel against neighbours who are allied against one of our enemies
NDefines.NAI.POTENTIAL_FUTURE_ENEMY_FACTOR = 100 		-- How much increase in threat does AI feel against neighbours who at war with our allies
NDefines.NAI.NEUTRAL_THREAT_PARANOIA = 10				-- How scared neutrals are of everyone
NDefines.NAI.DIFFERENT_FACTION_THREAT = 30				-- Threat caused by not being in the same faction
NDefines.NAI.MAX_THREAT_FOR_FIRST_YEAR_CIVILIAN_MODE = 60 -- above this threshold ai will leave first year civilian factory mode which bumps it civilian factory scores while building
NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_LOW = 0.85		-- Minimum org % for a unit to actively attack an enemy unit when executing a plan
NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_LOW = 0.4	-- Minimum strength for a unit to actively attack an enemy unit when executing a plan
NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_MED = 0.7		-- (LOWMEDHIGH) corresponds to the plan execution agressiveness level.
NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_MED = 0.3
NDefines.NAI.PLAN_ATTACK_MIN_ORG_FACTOR_HIGH = 0.4
NDefines.NAI.PLAN_ATTACK_MIN_STRENGTH_FACTOR_HIGH = 0.2
NDefines.NAI.AREA_DEFENSE_CAPITAL_VP_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_HOME_VP_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_OTHER_VP_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_COAST_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_CAPITAL_COAST_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_HOME_COAST_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_OTHER_COAST_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_CAPITAL_PEACE_BASE_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_CAPITAL_BASE_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_HOME_BASE_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.AREA_DEFENSE_OTHER_BASE_WEIGHT = { 0.0, 0.0, 0.0 }
NDefines.NAI.ORG_UNIT_WEAK = 0.15						-- Organization % for unit to be considered weak
NDefines.NAI.STR_UNIT_WEAK = 0.4						-- Strength (equipment) % for unit to be considered weak
NDefines.NAI.WANTED_UNITS_INDUSTRY_FACTOR = 1.45                        -- How many units a country wants is partially based on how much military industry that is available
NDefines.NAI.WANTED_CARRIER_PLANES_PER_CARRIER_CAPACITY_FACTOR = 1					-- Scales how many carrier planes the AI want per carrier deck space.
NDefines.NAI.UPGRADE_PERCENTAGE_OF_FORCES = 0.1					-- How big part of the army that should be considered for upgrading
NDefines.NAI.MISSING_CONVOYS_BOOST_FACTOR = 18.0					-- The more convoys a country is missing the more resources it diverts to cover this.
NDefines.NAI.HOUR_BAD_COMBAT_REEVALUATE = 100                   -- if we are in combat for this amount and it goes shitty then try skipping it
NDefines.NAI.MIN_PLAN_VALUE_TO_MICRO_INACTIVE = 0.2				-- The AI will not consider members of groups which plan is not activated AND evaluates lower than this.
NDefines.NAI.LAND_DEFENSE_AA_IMPORTANCE_FACTOR = 0.7			-- Factor of AA influence on strategic importance ( 0.0 - 1.0 )
NDefines.NAI.STR_BOMB_AA_IMPORTANCE_FACTOR = 0.25				-- Factor of AA influence on strategic importance ( 0.0 - 1.0 )
NDefines.NAI.ASSIGN_TANKS_TO_WAR_FRONT = 4.0                            -- Scoring factor for assigning tank divisions to active war fronts
NDefines.NAI.DESIGN_COMPANY_SCORE_MULTIPLIER = 2.0              -- score multiplier for hiring a design company
NDefines.NAI.POLITICAL_ADVISOR_SCORE_MULTIPLIER = 1.0           -- score multiplier for hiring political advisors
NDefines.NAI.DEPLOYED_UNIT_MANPOWER_RATIO_TO_BUFFER_WARTIME = 0.3 				-- deployment will try to buffer a ratio of deployed manpower (for reinforcements) during war time
NDefines.NAI.UPGRADES_DEFICIT_LIMIT_DAYS = 50                           -- Ai will avoid upgrading units in the field to new templates if it takes longer than this to fullfill their equipment need
NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_MINE_SWEEPING = 0.15 -- maximum ratio of screens forces to be used in mine sweeping
NDefines.NAI.MAX_SCREEN_TASKFORCES_FOR_MINE_LAYING = 0.15 -- maximum ratio of screens forces to be used in mine laying
NDefines.NAI.MAX_SCREEN_FORCES_FOR_INVASION_SUPPORT = 0.2 -- max ratio of screens forces to be used in naval invasion missions
NDefines.NAI.CONVOY_ESCORT_MUL_FROM_NO_CONVOYS = 0.02                    -- score multiplier when no convoys are around
NDefines.NAI.FIX_SUPPLY_BOTTLENECK_SATURATION_THRESHOLD = 0.75;  -- Try to fix supply bottlenecks if supply node saturation exceeds this value.
NDefines.NAI.PEACE_BID_FOLD_TURNS_AGAINST_OTHER_AI = 2
NDefines.NAI.PEACE_BID_FOLD_AGAINST_PLAYER_CHANCE = 0.5                 -- Likelihood that AI will fold in a bidding contest against human player.
NDefines.NAI.PEACE_BID_FOLD_AGAINST_AI_CHANCE_UNCONTROLLED = 0.40		-- Likelihood an AI will fold against an AI in a bidding contest where they do not control the state in question if their own bid is take_states and there is a bidder with more points.
NDefines.NAI.PEACE_BID_FOLD_AGAINST_LIBERATE_CONTEST = 1.0				-- Likelihood that the AI will back down against a same-ideology country performing a contesting liberate bid ##Bordergore prevention therapy
NDefines.NAI.PEACE_BID_FOLD_MINOR_VS_MAJOR = 1.0						-- Likelihood that AI minors will fold against majors (majors will already try and return cores and claims so this should not be a particularly big deal)
NDefines.NOperatives.AGENCY_UPGRADE_DAYS = 20						-- Number of days needed to upgrade an intelligence agency
NDefines.NOperatives.AGENCY_OPERATIVE_RECRUITMENT_TIME = 20			-- Number of days to wait to have operative to recruit when an operative slot first becomes available
NDefines.NOperatives.OPERATIVE_BASE_INTEL_NETWORK_GAIN = 0.8				-- Base amount of network strength gain per day provided by an operative
NDefines.NCharacter.ADVISOR_PROMOTION_COST = 0	-- Cost to promote someone to advisor
--defines to calculate the capitals supply. This will be also used for max supply of other nodes depending on how well they are connected to capital. Using the formula:
--CapitalSupply = CAPITAL_SUPPLY_BASE + (NumberOfCivilianFactories * CAPITAL_SUPPLY_CIVILIAN_FACTORIES) + (NumberOfMilitaryFactories * CAPITAL_SUPPLY_MILITARY_FACTORIES) + (NumberOfDockyards * CAPITAL_SUPPLY_DOCKYARDS)
NDefines.NSupply.CAPITAL_SUPPLY_BASE = 10.0 -- vanilla 5.0 base supply for capital
NDefines.NSupply.CAPITAL_SUPPLY_CIVILIAN_FACTORIES = 0.5 -- vannila 0.3 supply from one civilian factory #
NDefines.NSupply.CAPITAL_SUPPLY_MILITARY_FACTORIES = 0.8 -- vannila 0.6 supply from one military factory
NDefines.NSupply.CAPITAL_SUPPLY_DOCKYARDS = 0.65 -- #was 0.4 supply from one naval factory
-- defines that are used for supply reach for capital
-- supply flow will start from INITIAL_SUPPLY_FLOW and will be reduced by a penalty on each province it travels (which depends on how far we are from our origin terrain etc)
-- a supply reach >= 1.0 considered "perfect" and will be able to fully support units on that particular province (assuming you are not over capacity)
NDefines.NSupply.CAPITAL_INITIAL_SUPPLY_FLOW = 7.0 -- #was 5.0 starting supply from
NDefines.NSupply.CAPITAL_STARTING_PENALTY_PER_PROVINCE = 0.65 --#was 0.5  starting penalty that will be added as supply moves away from its origin (modified by stuff like terrain)
NDefines.NSupply.CAPITAL_ADDED_PENALTY_PER_PROVINCE = 0.7 -- #was 1.2 added penalty as we move away from origin
-- defines that are used for supply reach for built nodes
NDefines.NSupply.NODE_INITIAL_SUPPLY_FLOW = 4.5 -- #was 2.8
NDefines.NSupply.NODE_STARTING_PENALTY_PER_PROVINCE = 0.4 -- #was 0.50
NDefines.NSupply.NODE_ADDED_PENALTY_PER_PROVINCE = 0.40  -- #was 0.70
-- defines that are used for supply reach for dockyards
NDefines.NSupply.NAVAL_BASE_INITIAL_SUPPLY_FLOW = 6.0 -- #was 3.3
NDefines.NSupply.NAVAL_BASE_STARTING_PENALTY_PER_PROVINCE = 0.55 -- #was 0.84
NDefines.NSupply.NAVAL_BASE_ADDED_PENALTY_PER_PROVINCE = 1.1 -- #was 1.1
NDefines.NSupply.SUPPLY_FLOW_PENALTY_CROSSING_RIVERS = 0.40 -- #was 0.20 crossing rivers introduces additional penalty
NDefines.NSupply.SUPPLY_HUB_FULL_MOTORIZATION_BONUS = 3.2     ---vanilla 2.2
-- How many trucks does it cost to fully motorize a hub
NDefines.NSupply.SUPPLY_HUB_FULL_MOTORIZATION_TRUCK_COST = 180.0
NDefines.NSupply.RAILWAY_BASE_FLOW = 15.0 		-- #was 10.0 how much base flow railway gives when a node connected to its capital/a naval node by a railway
NDefines.NSupply.RAILWAY_FLOW_PER_LEVEL = 10.0 	--  #was 10.0 how much additional flow a railway level gives
NDefines.NSupply.RAILWAY_FLOW_PENALTY_PER_DAMAGED = 10.5  --   #was 5.0 penalty to flow per damaged railway
NDefines.NSupply.RAILWAY_MIN_FLOW = 2.5 		-- #was 5.0 	minimum railway flow can be reduced to
-- used for calculating "flow" from a naval node to another naval node when it is connected via a convoy route
-- NAVAL_BASE_MAX_SUPPLY_FLOW_FACTOR = 0.9 -- flow of the parent node is factored to this ratio (so at most it can transfer parent naval node flow * this define)
NDefines.NSupply.NAVAL_BASE_FLOW = 10.0 -- was 5.0 max output/input of a naval node is limited by this base value + additional ratio for each level
NDefines.NSupply.NAVAL_FLOW_PER_LEVEL = 6.0 -- was 3.0 max output/input of a naval node is limited by previous base value + this define per its level
NDefines.NSupply.SUPPLY_NODE_MIN_SUPPLY_THRESHOLD = 1.0 -- if supply of a node is below this value it will be set to 0 -- Currently unused? This should happen when enough damage occurs
NDefines.NSupply.INFRA_TO_SUPPLY = 0.8							-- was 0.3 each level of infra gives this many supply
NDefines.NSupply.VP_TO_SUPPLY_BASE = 0.2							-- Bonus to supply from a VP no matter the level
NDefines.NSupply.VP_TO_SUPPLY_BONUS_CONVERSION = 0.05			-- Bonus to supply local supplies from Victory Points multiplied by this aspect and rounded to closest integer
NDefines.NSupply.SUPPLY_FROM_DAMAGED_INFRA = 0.4                -- was 0.15 damaged infrastructure counts as this in supply calcs
NDefines.NSupply.SUPPLY_BASE_MULT = 0.1							-- was 0.2 multiplier on supply base values
NDefines.NSupply.SUPPLY_DISRUPTION_DAILY_RECOVERY = 2.0		-- was 1.5 every day nodes recover this much of their accumulated disruption.
NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN = 3 -- railways will be put on cooldown when they are captured by enemy and will not be usable during the cooldown
NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN_CORE = 5
NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN_CIVILWAR = 0
NDefines.NSupply.DEFAULT_STARTING_TRUCK_RATIO = 1.5 -- countries get this ratio of starting truck in their buffers compared to their need
NDefines.NSupply.DEFAULT_STARTING_TRAIN_RATIO = 1.5 -- #was 1.0 countries get this ratio of starting trains in their buffers compared to their need
NDefines.NSupply.SUPPLY_POINTS_PER_TRAIN = 1.8  -- old default 1.25 -- Amount of supply that can fit in a train. (Trains distribute supply from capital to a supply node.)
NDefines.NIndustrialOrganisation.ASSIGN_DESIGN_TEAM_PP_COST_PER_DAY = 0.1					-- Cost in Political Power daily generation when one MIO is assigned to a research slot
NDefines.NIndustrialOrganisation.ASSIGN_INDUSTRIAL_MANUFACTURER_PP_COST_PER_DAY = 0.0		-- Cost in Political Power daily generation when one MIO is assigned to a production line
NDefines.NIndustrialOrganisation.FUNDS_FOR_SIZE_UP = 1000					-- Funds needed for a MIO to increment its size and get points to unlock traits
NDefines.NIndustrialOrganisation.FUNDS_FOR_SIZE_UP_LEVEL_FACTOR = 0.8 			-- How much each level mutliplies the funds for size up 
NDefines.NIndustrialOrganisation.UNLOCKED_TRAITS_PER_SIZE_UP = 1			-- Number of points for unlocking traits obtained when the MIO increments its size
NDefines.NIndustrialOrganisation.DESIGN_TEAM_CHANGE_XP_COST = 5				-- Flat cost added to the XP cost of a new equipment design
NDefines.NIndustrialOrganisation.FUNDS_FOR_RESEARCH_COMPLETION_PER_RESEARCH_COST = 500     -- Funds added to MIO when the Design Team has completed a research multiplied by research_cost in technology template
NDefines.NIndustrialOrganisation.FUNDS_FOR_CREATING_EQUIPMENT_VARIANT = 0		-- Funds added to MIO when a new variant is created with the Design Team assigned to it
NDefines.NIndustrialOrganisation.FUNDS_FROM_MANUFACTURER_PER_IC_PER_DAY = 0.1		-- Funds added to MIO when a manufacturer is attached to a production line. Added every day proportional to IC produced.
NDefines.NIndustrialOrganisation.MAX_FUNDS_FROM_MANUFACTURER_PER_DAY = 100		-- Max funds generated per manufacturer per day. Set to 0 for no Maximum.
NDefines.NIndustrialOrganisation.DESIGN_TEAM_RESEARCH_BONUS = 0.05				-- Research bonus for applying a Design Team that matches the technology
NDefines.NIndustrialOrganisation.ENABLE_TASK_CAPACITY = false					-- Enable limited task capacity for MIOs
NDefines.NIndustrialOrganisation.DEFAULT_INITIAL_TASK_CAPACITY = 0				-- Default start task capacity for each MIO (may be overriden in DB)
NDefines.NIndustrialOrganisation.DEFAULT_INITIAL_POLICY_ATTACH_COST = 25		-- Default start attach cost in PP for policies
NDefines.NIndustrialOrganisation.DEFAULT_INITIAL_ATTACH_POLICY_COOLDOWN = 180	-- Default start cooldown in days after attaching a policy
NDefines.NIndustrialOrganisation.LEGACY_COST_FACTOR_SCALE = 1.0					-- Multiplier to use when legacy Designer cost factors is applied to MIOs (<IdeaGroup>_cost_factor)
NDefines.NMarket.PURCHASE_CONTRACT_DELIVERY_TOTAL_DAYS = 30 -- Number of days between purchase contract deliveries 
NDefines.NMarket.IC_TO_CIC_FACTOR = 2.0 -- The factor for mapping IC cost to CIC cost. Should be a positive number. 
NDefines.NMarket.MAX_CIV_FACTORIES_PER_CONTRACT = 15 -- Max number of factories that can be assigned for paying single contract. 
NDefines.NMarket.LOW_PRICE_LEVEL_FACTOR = 0.75 -- The factor of base equipment price for low price level. Should be in range (01] 
NDefines.NMarket.HIGH_PRICE_LEVEL_FACTOR = 1.25 -- The factor of base equipment price for high price level. Should be more than 1. 
NDefines.NMarket.MIN_DELIVERY_LIMIT_WARNING_UI = 0.8 -- The delivery percentage under we want to let player know the contract is inefficient. [01] 
NDefines.NMarket.PURCHASE_CONTRACT_SUBSIDY_BONUS_SPEED_FACTOR = 1.0 -- The factor of speed bonus from subsidies 
NDefines.NMarket.CONVOY_WEIGHT_OVERRIDE = 0.0 -- Overrides the default lend leas weight of convoys for international market 
NDefines.NMarket.REQUEST_AUTOMATION_AUTO_ACCEPT_MARKET_ACCESS_DEFAULT = true -- Whether by default should accept market access requests from other countries. 
NDefines.NMarket.REQUEST_AUTOMATION_AUTO_SEND_MARKET_ACCESS_DEFAULT = true -- Whether by default should send market access requests to other countries. 
NDefines.NMarket.REQUEST_AUTOMATION_AUTO_ACCEPT_PURCHASE_DEFAULT = false -- Whether by default should accept purchase requests from other countries. } 
NDefines.NMarket.MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_VALUE = 1 -- The minimum number of factories we have to put on consumer goods by value. 
NDefines.NMarket.MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_PERCENT = 0.1 -- The minimum number of factories we have to put on consumer goods in percent. 
NDefines.NMarket.CONTRACT_ESTIMATE_AVERAGE_CONVOY_COUNT_ALPHA = 0.5				-- How strong effect should have the daily convoy count on the average (1.0 means it will use only the new number as average)
NDefines.NMarket.CONTRACT_ESTIMATE_AVERAGE_DAILY_PRODUCTION_ALPHA = 0.5 		-- How strong effect should have the daily production on the average (1.0 means it will use only the new number as average)
NDefines.NMarket.CONTRACT_ESTIMATE_AVERAGE_CONVOY_COUNT_SNAP_LIMIT = 0.3		-- If the difference between current and estimated available convoy count is smaller then this value we will use the current value for calculations.
NDefines.NMarket.CONTRACT_ESTIMATE_AVERAGE_DAILY_PRODUCTION_SNAP_LIMIT = 1.5	-- If the difference between current and estimated daily production is smaller then this value we will use the current value for calculations.
NDefines.NMarket.CONTRACT_ESTIMATE_AVERAGE_CONVOY_SUNK_MULTIPLIER_ALPHA = 0.5	-- How strong effect should have the daily sunk efficiency on the average (1.0 means it will use only the new number as average)
NDefines.NMarket.CONTRACT_ESTIMATE_AVERAGE_CONVOY_SUNK_MULTIPLIER_SNAP_LIMIT = 0.05 -- If the difference between current and estimated sunk efficiency convoy count is smaller then this value we will use the current value for calculations.
NDefines.NMarket.WARNING_CONVOYS_SUNK_MAX_DAYS = 30 -- The contracts will show sunk convoy message if there was sunk convoy in this amount of days
NDefines.NTechnology.MAX_SUBTECHS = 10

-- MPR
NDefines.NMilitary.ARMOR_VS_AVERAGE = 0.1 -- 0.4
NDefines.NMilitary.SLOWEST_SPEED = 3 -- 4
NDefines.NMilitary.REINFORCE_CHANCE = 0.10 -- 0.02
NDefines.NMilitary.COMBAT_OVER_WIDTH_PENALTY = -1 -- original mod 1.5 -- vanilla 1
NDefines.NMilitary.FIELD_EXPERIENCE_SCALE = 0.009 --0.0015
NDefines.NMilitary.UNIT_EXPERIENCE_SCALE = 0.12 --1
NDefines.NMilitary.UNIT_EXPERIENCE_PER_COMBAT_HOUR = 0.0040 --0.0001
NDefines.NMilitary.TRAINING_ATTRITION = 0.01 -- 0.05
NDefines.NMilitary.ARMY_TRAINING_FUEL_MULT = 0.15 -- 1
NDefines.NSupply.COOLDOWN_DAYS_AFTER_MOVING_SUPPLY_CAPITAL = 1
NDefines.NSupply.DAYS_TO_START_GIVING_SUPPLY_AFTER_MOVING_SUPPLY_CAPITAL = 1
NDefines.NSupply.DAYS_TO_START_GIVING_FULL_SUPPLY_AFTER_MOVING_SUPPLY_CAPITAL = 1
NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 999 --500
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 999 --500
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 999 --500
NDefines.NMilitary.FIELD_EXPERIENCE_MAX_PER_DAY	= 50 --1.2
NDefines.NMilitary.INFRASTRUCTURE_MOVEMENT_SPEED_IMPACT = -0.05 -- -0.10
NDefines.NMilitary.RETREAT_SPEED_FACTOR = 0.50 -- 0.25
NDefines.NMilitary.WITHDRAWING_SPEED_FACTOR = 0.30 -- 0.15
NDefines.NMilitary.PLANNING_MAX = 0.01 -- 0.30
NDefines.NMilitary.TRAINING_MAX_LEVEL = 3 -- 2
NDefines.NMilitary.EXPERIENCE_COMBAT_FACTOR = 0.15 -- 0.25
NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 2 -- 5	
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 2 -- 5
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 1 -- 10
NDefines.NMilitary.LAND_COMBAT_STR_DAMAGE_MODIFIER = 0.040 -- 0.060
NDefines.NRaids.RAID_DEFAULT_TARGET_COOLDOWN_DAYS = 1
NDefines.NProject.BREAKTHROUGH_DAILY_TECHNOLOGY_GAIN = 35
NDefines.NProject.BREAKTHROUGH_DAILY_SCIENTIST_SKILL_GAIN = 25
NDefines.NGame.ENERGY_RESOURCE = "gas"