<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8' />
    <title>Flask Learn</title>
</head>
<body>
    <table>
        <thead>
            <tr>
                <td>姓名</td>
                <td>年龄</td>
                <td>电话</td>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>{{user[0]}}</td>
                <td>{{user[1]}}</td>
                <td>{{user[2]}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>