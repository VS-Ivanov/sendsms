'''
Этот модуль содержит функции для отправки и получения входящих сообщений
из модуля dongle системы asterisk

'''
import os, io

def get_sms_inbox():
	'''
	Возвращает входящие смс сообщения как словарь вида
	{'date': дата сообщения, 'number': номер отправителя,'text': текст сообщения}
	'''
	if(os.path.exists('sms.txt')):
		sms_file = open('sms.txt','tr',encoding='utf8')
		result = list()

		for filestr in sms_file.readlines():
			res = {}
			res['date'] = filestr.split('— —')[0].rstrip().strip('‘')
			res['number'] = filestr.split('— —')[1].split(': ')[0].lstrip()
			res['text'] = filestr.split('— —')[1].split(': ')[1].strip('’\n')
			result.append(res)

		return result
		sms_file.close()
	else: 
		return False;

def get_ussd_inbox():
	'''
	Возвращает входящие ussd сообщения как словарь вида
	{'date': дата сообщения,'channel':  GSM канал на который пришло сообщение,'text': текст сообщения}
	'''
	if(os.path.exists('ussd.txt')):
		ussd_file = open('ussd.txt','tr',encoding='utf8')
		result = list()

		for filestr in ussd_file.readlines():
			res = {}
			res['date'] = filestr.split(' — ')[0]
			res['channel'] = filestr.split(' — ')[1].split(': ')
			res['text'] = filestr.split(' — ')[1].split(': ')[1].rstrip()
			result.append(res)

		return result
		ussd_file.close()
	else:
		return False

def get_sms_outbox():
	'''
	Возвращает исходящие смс сообщения как словарь вида
	{'date': дата сообщения, 'number': номер получателя,'text': текст сообщения}
	'''
	return False

def get_ussd_outbox():
	'''
	Возвращает исходящие ussd сообщения как словарь вида
	{'date': дата сообщения,'channel':  GSM канал с которого пришло сообщение,'text': текст сообщения}
	'''
	return False

def send_sms(channel='GSM1',number,text):
	'''
	Отправляет смс сообщение на указанный номер с указанного канала,
	если сообщение было успешно отправлено возвращает True, иначе False
	'''
	return False

def send_ussd(channel='GSM1',text):
	'''
	Отправляет ussd сообщение с указанного канала,
	если сообщение было успешно отправлено возвращает True, иначе False
	'''
	return False