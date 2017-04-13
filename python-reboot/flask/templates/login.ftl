<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <form action='/validate' method='POST'>
	{% if error %}
	<span style='color:red'>{{error}}</span></br>
	{% endif %}
    名字<input type='text' name='username' value="username"/><br />
    密码<input type='password' name='password'/><br />
    <input type="submit" value="登录"/><br />
    </form>
</body>
</html>
