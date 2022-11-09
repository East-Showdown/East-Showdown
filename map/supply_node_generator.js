/*
Copyright (c) 2022 officialmugi and the Southern Victory team
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Generates a supply_nodes.txt file for use in the NSB update, primarily intended for use with custom maps that need supply nodes generated. Generates a supply node at each end of a railway. Requires node.js.

usage: node supply_node_generator.js

Example: Run this file in the same folder as the railways.txt file. If errors are produced, check that there are no trailing spaces or empty lines.
*/

var fs = require('fs');

var railways = fs.readFileSync('railways.txt').toString().split("\n");

var array = [12831, 4709]; //Add any provinces you want to have supply hubs here, modify these for your mod

const remove = [4904, 13804] // Add any provinces you wish to NOT have supply hubs, modify these for your mod

railways.forEach(line => {
	var integers = line.split(" ");
	array.push(parseInt(integers[2]));
	array.push(parseInt(integers[integers.length - 1]));
});

array.sort(function(a, b) {
	return a - b;
});

array = array.filter(function(elem, pos) {
    return array.indexOf(elem) == pos;
});

var file = fs.createWriteStream('supply_nodes.txt');

file.on('error', function(err) {
	/* Don't care about error handling tbh */
});

array.forEach(function(a) {
	if (!remove.includes(a)) {
		file.write("1 " + a + '\r\n');
	}
});

file.end();

