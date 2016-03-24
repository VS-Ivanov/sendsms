<html>
<head>
<meta http-equiv="Content-Type" content="text/html"; charset="utf-8">
<meta http-equiv="Refresh" content="40" />
<title>send-sms</title>
</head>
<body bgcolor="#84b0fd" text="#030303" link="#9abcde" charset="utf-8" >
<form method="post" action="sms.php">
<p>SIM:
<select name="select" size="1">
<option value="GSM2">GSM2</option>
<option value="GSM1">GSM1</option>
</select>
</p>
<p>Телефонный номер:
<input type = "text" name = "namber"  size="30"></p>
<p><b>Отправить:</b><br>
<input type="radio" name="com" value="ussd">USSD<br>
<input type="radio" name="com" value="sms">SMS<br><br>
</p>
<p><b>Текс сообщения</b><br>
<textarea name="message" rows="5" cols="50"></textarea></p>
<p><input type="submit" name="submint" value="Отправить">
<input type="reset" value="Очистить"</p>
</form>
<p>Входящие SMS/USSD сообщения</p>
<iframe src="http://192.168.16.14/sms.txt" width="980" height="250"></iframe>
<iframe src="http://192.168.16.14/ussd.txt" width="980" height="250"></iframe>
</body>
</html>
