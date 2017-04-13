'use strict';

var 
    port = 8080,
    fs   = require('fs'),
    url  = require('url'),
    path = require('path'),
    http = require('http');

var root = path.resolve(process.argv[2] || '.')

console.log('Static root dir: ' + root);

var server = http.createServer(function(request,response){
    var pathname = url.parse(request.url).pathname;
    var filepath = path.join(root,'webapps',pathname)
    console.log(filepath)
    fs.stat(filepath,function(err,stats){
        if (!err && stats.isFile()){
            console.log('200:'+request.url);
            response.writeHead(200);
            fs.createReadStream(filepath).pipe(response);
        }else if(!err && stats.isDirectory()){
            var filepath_new=path.join(filepath,'index.html')
            var filepath_new_stat=fs.statSync(filepath_new)
            if (filepath_new_stat.isFile()){
                console.log('200:'+request.url+'index.html');
                response.writeHead(200);
                fs.createReadStream(filepath_new).pipe(response);
            }

        }else{
           console.log('404:'+request.url);
           response.writeHead(404);
           response.end("404notfounc"); 
        }
    });
});

server.listen(port);
console.log('running...')