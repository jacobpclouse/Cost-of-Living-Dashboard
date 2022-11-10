var express = require('express');
var router = express.Router();

router.get('/', function(req, res){
    res.send('fly me to the moon');
});

router.post('/', function(req, res){
    res.send('let me dance amoung the stars');
}); 

//export this router to use in our index.js
module.exports = router;
