var express = require('express');
var app = express();


app.get('/', function(req, res){
    res.send("Welcome to the index");
   });


app.get('/hello', function(req, res){
 res.send("Hello world!");
});


app.post('/hello', function(req, res){
    res.send("Kablamo");
   });
   

app.all('/all', function(req, res){
    res.send("YOU HAVE NO POWER HERE!");
   });

app.listen(3000);