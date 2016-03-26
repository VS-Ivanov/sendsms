var express = require('/express');

var app = express();

app.get('/',function(req,res){
	res.send('Hello from send sms!');
})

app.listen(3000,function(req,res){
	console.log('Sendsms running on 3000 port...');
})