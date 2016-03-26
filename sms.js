// содержит функции для отправки и получения sms и ussd сообщений
// через модуль dongle asterisk

var SMS_OUTBOX_FILE = "./sms_outbox.txt";
var SMS_INBOX_FILE = "./sms.txt";
var USSD_INBOX_FILE = "./ussd.txt"
var USSD_OUTBOX_FILE = "./ussd_outbox.txt";

module.exports = {

	// возвращает массив sms или ussd сообщений вида
    // {date:дата сообщения, number: номер сообщения, text: текст сообщения}
	get : function(){

		return {date:'26.03.2016',number:'8-800-888',text:'test message'};

	},

	send : function(){
		// отправляет sms или ussd сообщение с указанного канала на указанный номер
		// в случае успеха возвращает True или False в случае неудачи
		
		return SMS_INBOX_FILE;
		//return message_encode();
		//return true;
	}

}

var message_decode = function(){
	// декадирует сообщение из исходного формата в словарь
	return "decoded message";
}

var message_encode = function(){
	// кодирует сообщение из словаря в формат для сохранения
	return "encoded message";
}
