<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<META HTTP-EQUIV="Refresh" Content="3; URL=http://192.168.16.14/send-sms.php"/>
<title>sms</title>
</head>
<body bgcolor="#84b0fd" text="#030303" link="#9abcde">
<?php
$g=$_POST['namber'];
$j=$_POST['message'];
$f=$_POST['com'];
$s=$_POST['select'];
//это условие работает так если вели число ,работает дальше иначе, выход из условия
if (($g=="") ) {echo "Пустая строка";} else
if (is_string($g)){ $l=$g;} 
else {
    echo "номер не указан";
    echo '<hr>';} 
if ($f=="ussd") {`asterisk -rx "dongle  ussd $s  $g"`;} 
else if ($f=="sms") {`asterisk -rx "dongle sms $s $g $j"` ;}
exit
?>
</body>
</html>
