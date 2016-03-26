var express = require('express');
var bodyParser = require('body-parser'); // нужно для получения параметров post запроса


var index_page = function(req, res){
	// нужно передавать массив в шаблон, иначе шаблонизатор не сработает
  var mes1 = {date:'26.03.2016',number:'8-800-888',text:'test message'};
  var mes = [mes1];
  
  var mtitle, mcount; // количество сообщения и заголовок таблицы

  switch(req.param('mes')){
  	case 'sms_inbox':
  	mtitle = 'Входящие SMS сообщения:';
  	break;

  	case 'sms_outbox':
  	mtitle = 'Исходящие SMS сообщения:';
  	break;

  	case 'ussd_inbox':
  	mtitle = 'Входящие USSD сообщения:';
  	break;

  	case 'ussd_outbox':
  	mtitle = 'Исходящие USSD сообщения:';
  	break;

  	default:
  	mtitle = 'Входящие SMS сообщения:';
  }
  res.render('index',{title:'Send sms',mes:mes,mtitle:mtitle});
}


var send_page = function(req, res){
	// res.send('Run send page!');
	res.render('send',{title:'Send sms'});
}

var about_page = function(req, res){
	// res.send('Run about page!');
	res.render('about',{title:'О программе'});
}

var send_message = function(req, res){
	// берем полученные параметры из post запроса
	res.send('Ты отправил сообщение на номер - '+req.body.number);
	// res.send('Message sended...');
}

var app = express();

//подключаем каталог со статическими файлами
app.use(express.static('static'));

//используем bodyparser
app.use( bodyParser.json() );
app.use(bodyParser.urlencoded({
})); 

//подключаем движок для рендеринга ejs
var ejs = require('ejs');
// app.engine('ejs',ejs);
app.set('view engine','ejs');

app.get('/',index_page);
app.get('/index',index_page);
app.get('/send',send_page);
app.get('/about',about_page);
app.post('/send',send_message);

app.listen(3000,function(req,res){
	console.log('Sendsms running on 3000 port...');
})