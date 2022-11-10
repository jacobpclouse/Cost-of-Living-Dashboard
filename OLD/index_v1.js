var express = require('express');
var app = express();


app.get('/', function(req, res){
 res.send("Hello world!");
});


app.get('/boi', function(req, res){
    res.send("Boi");
   });
   

app.listen(3000);