'use strict';

var fs = require('fs');

var rs = fs.createReadStream('test.file.txt','utf-8');

rs.on('data',function(chunck){
    console.log('DATA:')
    console.log(chunck);
});
rs.on('data',function(chunck){
    console.log('DATA2:')
    console.log(chunck);
});
rs.on('end',function(){
    console.log('END');
})

rs.on('error',function(err){
    console.log('ERROR:'+err)
})