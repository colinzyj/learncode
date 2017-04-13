// 导入koa，和koa 1.x不同，在koa2中，我们导入的是一个class，因此用大写的Koa表示:
const Koa = require('koa');

//创建一个Koa对象表示web app本身:
const app = new Koa();

// 注意require('koa-router')返回的是函数:
const router = require('koa-router')();

//
const bodyParser = require('koa-bodyparser');


//test
/*
const nunjucks = require('nunjucks');

function createEnv(path,opts){
    var
        autoescape = opts.autoescape && true,
        noCache = opts.noCache || false,
        watch = opts.watch || false,
        throwOnUndefined = opts.throwOnUndefined || false,
        env = new nunjucks.Environment(
            new nunjucks.FileSystemLoader('views',{
                noCache:noCache,
                watch:watch,
            }),{
                autoescape:autoescape,
                throwOnUndefined:throwOnUndefined
            }
        );
    if(opts.filters){
        for (var f in opts.filters){
            env.addFilter(f,opts.filters[f]);
        }
    }
    return env;
}

var env=createEnv('views',{
    watch:true,
    filters:{
        hex:function(n){
            return '0x'+n.toString(16);
        }
    }
});
*/
//test




// 导入fs模块
const fs = require('fs');

// 对于任何请求，app将调用该异步函数处理请求：
app.use(async (ctx, next) => {
    console.log(`${ctx.request.method} ${ctx.request.url}`); // 打印URL
    /*if (ctx.request.url === '/hello'){
        ctx.response.type = 'text/html';
        ctx.response.body=env.render('extend.html',{header: 'Hello',body: 'bla bla bla...'});
    }*/
    await next(); // 调用下一个middleware
});

// 处理静态文件目录
let staticFiles = require('./mymodules/static-files.js');
app.use(staticFiles('/static/', __dirname + '/static'));


// add body parser
app.use(bodyParser());


const isProduction = process.env.NODE_ENV === 'production';
const templating=require('./mymodules/templating.js');

app.use(templating('view', {
    noCache: !isProduction,
    watch: !isProduction
}));




// add url-route in ./controllers:
function addMapping(router,mapping){
    for (var url in mapping){
        if (url.startsWith('GET')){
            var path = url.substring(4);
            router.get(path,mapping[url]);
            console.log(`register URL mapping: GET ${path}`);
        }else if(url.startsWith('POST')){
            var path = url.substring(5);
            router.post(path,mapping[url]);
            console.log(`register URL mapping: POST ${path}`);
        }else{
            console.log(`invalid URL: ${url}`);
        }
    }
}


function addControllers(router){
    var files = fs.readdirSync(__dirname+'/controllers');
    // 过滤出.js文件:
    var js_files = files.filter((f)=>{
        //console.log(f.endsWith('.js'));
        return f.endsWith('.js');
    },files);
    //console.log(js_files);
    // 处理每个js文件:
    for (var f of js_files){
        //console.log(f);
        console.log(`process controllers :${f}...`);
        //导入js文件
        let mapping = require(__dirname+'/controllers/'+f);
        addMapping(router,mapping);
    }
}

addControllers(router);


/*
app.use(async (ctx, next) => {
    const start = new Date().getTime(); // 当前时间
    await next(); // 调用下一个middleware
    const ms = new Date().getTime() - start; // 耗费时间
    console.log(`Time: ${ms}ms`); // 打印耗费时间
});

app.use(async (ctx, next) => {
    console.log('I am is a test');
    await next();
});
app.use(async (ctx, next) => {
    await next();
    ctx.response.type = 'text/html';
    ctx.response.body = '<h1>Hello, koa2!</h1>';
});
*/

/*
router.get('/hello/:name',async(ctx,next)=>{
    var name=ctx.params.name;
    ctx.response.body=`<h1>hello,${name}!</h1>`;
});
router.get('/',async(ctx,next)=>{
    ctx.response.body = `<h1>Index</h1>
    <form action="/signin" method="post">
        <p>Name: <input name="name" value="koa"></p>
        <p>Password: <input name="password" type="password"></p>
        <p><input type="submit" value="Submit"></p>  
    </form>`;
});

router.post('/signin',async(ctx,next)=>{
    var
        name =ctx.request.body.name || '',
        password = ctx.request.body.password || '';
    console.log(`signin with name: ${name}, password: ${password}`);
    if (name === 'koa' && password === '12345'){
        ctx.response.body = `<h1>Welcome, ${name}!</h1>`;
    }else{
        ctx.response.body = `<h1>Login failed!</h1>
        <p><a href="/">Try again</a></p>`;
    }
})
*/

//add router middleware;
app.use(router.routes());

// 在端口3000监听:
app.listen(8080);
console.log('app started...')