/*
Copyright (c) 2022 officialmugi
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Generates files for Hearts of Iron 4 radio stations: an asset file for the sound files, a localisation file, a gui file for the station and a playlist. 

usage: node radiostationgenerator.js
Run this file in a folder for a radio station that contains only two subfolders, one titled "War" that contains music to be played during war and the other titled "Peace" that contains music to be played during peace. The output files will be named after the folder this file is executed in. 

Example: Place the js file in a folder named EXAMPLE, this folder contains two subfolders War and Peace that each have music files. When executed, this file will output EXAMPLE.asset (containing the music files), EXAMPLE_l_english.yml (Uses filenames for the localisation), EXAMPLE_soundtrack (adding the music files to a radio station) and music_station_EXAMPLE.gui that implements the station itself. The graphics for a station will need to be handled separately.

To do:
*Handle folders which contain only war or peace music
*Read music names from metadata or a json file
*Handle graphics for music stations
*/

const peaceFolder = './Peace/';
const warFolder = './War/';
const fs = require('fs');
const path = require('path');
const cwd = path.basename(path.resolve(process.cwd()));

var asset = [];
var soundtrack = [];
var localisation = [];
var station = ['guiTypes = {', '	containerWindowType = {'];

asset.push("##### " + cwd, "");
soundtrack.push('music_station = "' + cwd + '"', "", "# PEACE SONGS ##################", "");
localisation.push("\ufeffl_english:", " " + cwd + '_TITLE:0 "' + cwd + '"');
station.push( '		name = "' + cwd + '_faceplate"', '		position = { x =0 y=0 }', '		size = { width = 590 height = 46 }', '', '		iconType ={', '			name ="musicplayer_header_bg"', '			spriteType = "GFX_musicplayer_header_bg"', '			position = { x= 0 y = 0 }', '			alwaystransparent = yes', '		}', '', '		instantTextboxType = {', '			name = "track_name"', '			position = { x = 72 y = 20 }', '			font = "hoi_20b"', '			text = "Roger Pontare - Nar vindarna viskar mitt namn"', '			maxWidth = 450', '			maxHeight = 25', '			format = center', '		}', '', '		instantTextboxType = {', '			name = "track_elapsed"', '			position = { x = 124 y = 30 }', '			font = "hoi_18b"', '			text = "00:00"', '			maxWidth = 50', '			maxHeight = 25', '			format = center', '		}', '', '		instantTextboxType = {', '			name = "track_duration"', '			position = { x = 420 y = 30 }', '			font = "hoi_18b"', '			text = "02:58"', '			maxWidth = 50', '			maxHeight = 25', '			format = center', '		}', '', '		buttonType = {', '			name = "prev_button"', '			position = { x = 220 y = 20 }', '			quadTextureSprite ="GFX_musicplayer_previous_button"', '			buttonFont = "Main_14_black"', '			Orientation = "LOWER_LEFT"', '			clicksound = click_close', '			pdx_tooltip = "MUSICPLAYER_PREV"', '		}', '', '		buttonType = {', '			name = "play_button"', '			position = { x = 263 y = 20 }', '			quadTextureSprite ="GFX_musicplayer_play_pause_button"', '			buttonFont = "Main_14_black"', '			Orientation = "LOWER_LEFT"', '			clicksound = click_close', '		}', '', '		buttonType = {', '			name = "next_button"', '			position = { x = 336 y = 20 }', '			quadTextureSprite ="GFX_musicplayer_next_button"', '			buttonFont = "Main_14_black"', '			Orientation = "LOWER_LEFT"', '			clicksound = click_close', '			pdx_tooltip = "MUSICPLAYER_NEXT"', '		}', '', '		extendedScrollbarType = {', '			name = "volume_slider"', '			position = { x = 100 y = 45}', '			size = { width = 75 height = 18 }', '			tileSize = { width = 12 height = 12}', '			maxValue =100', '			minValue =0', '			stepSize =1', '			startValue = 50', '			horizontal = yes', '			orientation = lower_left', '			origo = lower_left', '			setTrackFrameOnChange = yes', '', '			slider = {', '				name = "Slider"	', '				quadTextureSprite = "GFX_scroll_drager"', '				position = { x=0 y = 1 }', '				pdx_tooltip = "MUSICPLAYER_ADJUST_VOL"', '			}', '', '			track = {', '				name = "Track"', '				quadTextureSprite = "GFX_volume_track"', '				position = { x=0 y = 3 }', '				alwaystransparent = yes', '				pdx_tooltip = "MUSICPLAYER_ADJUST_VOL"', '			}', '		}', '', '		buttonType = {', '			name = "shuffle_button"', '			position = { x = 425 y = 20 }', '			quadTextureSprite ="GFX_toggle_shuffle_buttons"', '			buttonFont = "Main_14_black"', '			Orientation = "LOWER_LEFT"', '			clicksound = click_close', '		}', '	}', '', '	containerWindowType={', '		name = "' + cwd + '_stations_entry"', '		size = { width = 162 height = 130 }', '		', '		checkBoxType = {', '			name = "select_station_button"', '			position = { x = 0 y = 0 }', '			quadTextureSprite = "GFX_' + cwd + '_album_art"', '			clicksound = decisions_ui_button', '		}', '	}', '}');

fs.readdirSync(peaceFolder).forEach(file => {
	var hoi4name = cwd + "_" + file.split('.').slice(0, -1).join('.').toLowerCase().replace(/\W/g, '');
	asset.push("music = {", '	name = "' + hoi4name + '"', '	file = "' + cwd + "/Peace/" + file + '"', "	volume = 0.80", "}", "");
	soundtrack.push("music = {", '	song = "' + hoi4name + '"', "", "	chance = {", "		modifier = {", "			factor = 1", "			has_war = no", "		}", "	}", "}", "");
	localisation.push(" " + hoi4name + ":0 " + '"' + file.split('.').slice(0, -1).join('.') + '"');
});

soundtrack.push("# WAR SONGS ####################", "");

fs.readdirSync(warFolder).forEach(file => {
	var hoi4name = cwd + "_" + file.split('.').slice(0, -1).join('.').toLowerCase().replace(/\W/g, '');
	asset.push("music = {", '	name = "' + hoi4name + '"', '	file = "' + cwd + "/War/" + file + '"', "	volume = 0.80", "}", "");
	soundtrack.push("music = {", '	song = "' + hoi4name + '"', "", "	chance = {", "		modifier = {", "			factor = 1", "			has_war = yes", "		}", "	}", "}", "");
	localisation.push(" " + hoi4name + ":0 " + '"' + file.split('.').slice(0, -1).join('.') + '"');
});

var stream = fs.createWriteStream(cwd + "_soundtrack.txt");
stream.once('open', function(fd) {
	for (gamer of soundtrack) {
		stream.write(gamer + "\n");
	}
	stream.end();
});

var streamer = fs.createWriteStream(cwd + ".asset");
streamer.once('open', function(fd) {
	for (gamer of asset) {
		streamer.write(gamer + "\n");
	}
	streamer.end();
});

var streamest = fs.createWriteStream(cwd + "_l_english.yml");
streamest.once('open', function(fd) {
	for (gamer of localisation) {
		streamest.write(gamer + "\n");
	}
	streamest.end();
});

var streamboy = fs.createWriteStream("music_station_" + cwd + ".gui");
streamboy.once('open', function(fd) {
	for (gamer of station) {
		streamboy.write(gamer + "\n");
	}
	streamboy.end();
});