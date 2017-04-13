'use strict';

var fs = require('fs');

try {
    var data = fs.readFileSync('cd.png')
} catch (error) {
    console.log(error)
}

try {
    var stat=fs.statSync('test.file.txt')
} catch (err) {
    console.log(err)
} 
console.log('isfile:'+stat.isFile())
console.log('isDirectory:'+stat.isDirectory())
console.log('size: ' + stat.size);
console.log('birth time: ' + stat.birthtime);
console.log('modified time: ' + stat.mtime.getDate());
