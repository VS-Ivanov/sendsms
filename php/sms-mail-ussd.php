<?php

// путь до файла с смс
$file_name = '/var/log/asterisk/ussd.txt';

// если размер файла больше 0 переходим к его обрботке
if (filesize($file_name)>0) {

	// открываем файл для чтения и записи
	$fobj = fopen($file_name,"r+");
	$text = fread($fobj, filesize($file_name));
	// в файл смс записываются в следуюшем формате
	// дата и время -%- datacard -%- номер отправителя -%- текст смс
	// формат и разделитель можно сменить в конфиг файле
	// преобразовываем содержимое в массив используя -%- как разделитель
	$text1 = explode( "", $text);
	// делим массив а части по 4 элемента
	//$array = array_chunk($text1, );
	// рисуем таблицу в которой будут выводится наши смс
	///$mes1 = "<table border='1' bordercolor='#000000' cellspacing='0' cellpadding='2'>";
	///$mes2 = "<tr align='center' valign='middle
///'><td width='160'>Дата и время сообщения</td><td width='140'>Номер отправителя</td><td width='230'>Сообщение</td></tr>";
    //$tt = $text "\n";
	///for ($i = 0; $i <= count($array)-2; $i++)
	//	{
    //	$sms = $array[$i];
	//	$sms1[] = "<tr valign='middle
///'><td align='center'>".$sms[0]."</td><td align='center'>".$sms[2]."</td><td align='left'>".$sms[3]."</td></tr>";
///	}
//
///	for ($mes3 = '', $j = 0; $j <= count($sms1); $j++)
///		{
///		$mes3 = $mes3.$sms1[$j];
///	}
///
///	$mes4 = "</table>";

	// Теперь перейдем к отправке
	// отправлять будем используя встроенную функцию mail()

	// получаем текущую дату
	$date = date("d.m.Y");
	// получаем текущее время
	$time = date("H:i:s");
	// адрес куда будем отправлять письмо
	$to  = "sirok2@mail.ru";
	// тема письма
	$subject = "New SMS Message(s) - ".$date." - ".$time;
	// текст письма
	$message = $text;
	// дополнительные заголовки письма
	// кодировка письма
	$headers  = "Content-type: text/html; charset=utf-8 \r\n";
	// отправитель письма
	$headers .= "From: SMS Gate <sirok2@mail.ru>\r\n";

	// отправляем письмо, если отправка прошла успешно
	// выводим сообщение иочищаем файл с смс
	if (mail($to, $subject, $message, $headers)) {
		echo "Soobshenie ojidaet otpravki";
		ftruncate ($fobj, 0);
	} else {
		// если ошибка выводим это сообщение
		echo "Oshibka pri otpravke";
	}

	// закрываем файл
	fclose($file_name);

}

// если файл пустой выводим это сообщение
else { echo "Sms soobshenii net..."; }

?>
