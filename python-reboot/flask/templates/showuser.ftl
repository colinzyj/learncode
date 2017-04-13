<html>
<head>
    <meta charset="utf-8">
</head>
<body>
	<table>
	<thead>
		<tr>
			<td>username</td>
			<td>phonenum</td>
		</tr>
	</thead>
	<tbody>
		{% for user in users %}
		<tr>			
			<td>{{user}}</td>
            {% if users[user]['phonenum'] =='' %}
			<td>未填写</td>
            {% else %}
            <td>{{users[user]['phonenum']}}</td>
            {% endif %}
		</tr>
		{% endfor %}
	</tbody>
	</table>
</body>
</html>
