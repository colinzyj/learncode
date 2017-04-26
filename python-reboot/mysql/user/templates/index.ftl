<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8' />
    <title>Flask Learn</title>
    <style typy="text/css" >
        .errmsg{
            color:red;
            }
        .success{
            color:green;
        }
    </style>
</head>
<body>
    <input class="btn_login" type="button" value="用户登录"/>
    <input class="btn_register" type="button" value="用户注册"/>
    
    <form id="login" action="/login/" method="post">
        {% if loginerr %}
            <div class="errmsg">{{loginerr}}</div>
        {%endif%}
        用户名：<input type="text" name="username" value="{{loginusername}}" /><br/>
        密码：<input type="password" name="password" value="{{loginpassword}}" /><br/>
        <input type="submit" value="登录"/>
    </form>
    <form class="register" action="/register/" method="post">
        {% if registermsg %}
            <div class="
                {% if registerstatus %}
                    success
                {%else%}
                    errmsg
                {% endif %}
            ">{{registermsg}}</div>
        {% endif %}
        用户名：<input type="text" name="username" value="{{username}}"/><br/>
        密码：<input type="password" name="password" /><br/>
        年龄：<input type="text" name="age" value="{{age}}"/><br/>
        电话：<input type="text" name="telephone" value="{{telephone}}"/><br/>
        <input type="submit" value="注册"/>
    </form>
    <script type="text/javascript" src="/static/js/jquery.1.7.1.min.js"></script>
    <script type="text/javascript">
        jQuery(document).ready(function(){
            {% if registermsg %}
                jQuery(".register").show();
                jQuery("#login").hide();
            {% else %}
                jQuery("#login").show();
                jQuery(".register").hide();
            {% endif %}
            jQuery(".btn_register").bind('click',function(){
                jQuery(".register").show();
                jQuery("#login").hide();                
            });
            jQuery(".btn_login").bind('click',function(){
                jQuery("#login").show();
                jQuery(".register").hide();
            });
        });
    </script>
</body>
</html>