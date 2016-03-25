'''
Этот модуль содержит функции для отправки и получения входящих сообщений
из модуля dongle системы asterisk

'''
import os, io, datetime

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

		sms_file.close()
		return result
		
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

		ussd_file.close()
		return result
		
	else:
		return False

def get_sms_outbox():
	'''
	Возвращает исходящие смс сообщения как словарь вида
	{'date': дата сообщения, 'number': номер получателя,'text': текст сообщения}
	'''

	if os.path.exists('sms_outbox.txt'):
		result = list()
		sms_outbox_file = open('sms_outbox.txt','rt',encoding='utf8')
		for sms_str in sms_outbox_file.readlines():
			res = {}
			res['date'] = sms_str.split('--:--')[0]
			res['number'] = sms_str.split('--:--')[1]
			res['text'] = sms_str.split('--:--')[2]
			result.append(res)

		sms_outbox_file.close()
		return result

	else:
		return False

def get_ussd_outbox():
	'''
	Возвращает исходящие ussd сообщения как словарь вида
	{'date': дата сообщения,'channel':  GSM канал с которого пришло сообщение,'text': текст сообщения}
	'''
	if os.path.exists('ussd_outbox.txt'):
		result = list()
		ussd_outbox_file = open('ussd_outbox.txt','rt',encoding='utf8')
		for ussd_str in ussd_outbox_file.readlines():
			res = {}
			res['date'] = ussd_str.split('--:--')[0]
			res['channel'] = ussd_str.split('--:--')[1]
			res['text'] = ussd_str.split('--:--')[2]
			result.append(res)

		ussd_outbox_file.close()
		return result

	else:
		return False


def send_sms(number,text,channel='GSM1'):
	'''
	Отправляет смс сообщение на указанный номер с указанного канала,
	если сообщение было успешно отправлено возвращает True, иначе False
	'''
	if not os.system('asterisk -rx "dongle  ussd'+channel+' '+number+' '+text+'"'):
		sms_outbox_file = open('sms_outbox.txt','a',encoding='utf8')
		sms_str = str(datetime.datetime.now())+'--:--'+number+'--:--'+text
		sms_outbox_file.write(sms_str+'\n')
		sms_outbox_file.close()
		return True
	else:
		return False

def send_ussd(text,channel='GSM1'):
	'''
	Отправляет ussd сообщение с указанного канала,
	если сообщение было успешно отправлено возвращает True, иначе False
	'''
	if not os.system('asterisk -rx "dongle  ussd'+channel+' '+text+'"'):
		ussd_outbox_file = open('ussd_outbox.txt','a',encoding='utf8')
		ussd_str = str(datetime.datetime.now())+'--:--'+channel+'--:--'+text
		ussd_outbox_file.write(ussd_str+'\n')
		ussd_outbox_file.close()
		return True
	else:
		return False