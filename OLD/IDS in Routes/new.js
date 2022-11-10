var express = require('express');
var router = express.Router();

router.get('/:id', function(req, res){
    res.send('fly me to the moon ' + req.params.id);
});

router.post('/', function(req, res){
    res.send('let me dance amoung the stars');
}); 

//export this router to use in our index.js
module.exports = router;
