var express = require('Express');
var app = express();
var things = require('./things.js');
var new1 = require('./new.js');

//both index.js and things.js should be in same directory
app.use('/things', things);

app.use('/new',new1);

app.use('/', things)
app.listen(3000);