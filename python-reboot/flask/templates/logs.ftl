﻿<html>
<head>
    <meta charset="utf-8">
</head>
<body>
	<table>
	<thead>
		<tr>
			<td>ip</td>
			<td>count</td>
			<td>status</td>
			<td>url</td>
		</tr>
	</thead>
	<tbody>
		{% for log in logs %}
		<tr>			
			<td>{{log[0]}}</td>
			<td>{{log[1]}}</td>
			<td>{{log[2]}}</td>
			<td>{{log[3]}}</td>			
		</tr>
		{% endfor %}
	</tbody>
	</table>
</body>
</html>
