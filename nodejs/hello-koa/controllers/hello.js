
//var env=require('../mymodules/env.js');
var fn_hello = async(ctx,next)=>{
    var name=ctx.params.name;
    //ctx.response.body=`<h1>hello,${name}!</h1>`;
    ctx.response.body=env.render('extend.html',{header: 'Hello',body: 'bla bla bla...'});
};


module.exports={
    'GET /hello/:name':fn_hello
};