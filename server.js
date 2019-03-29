// All we need

var express = require('express');
var bodyParser = require('body-parser');
var port = process.env.port || 3000;
var path = require('path');


var app = express();
app.use(express.static(path.join(__dirname, 'public')));
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// BodyParser configure
app.use(bodyParser.urlencoded({
    extended:true
}));
app.use(bodyParser.json());

// Setup templating engine
app.set('view engine', 'ejs'); // setup EJS for templating


// Adding routes
require('./app/routes.js')(app);
app.listen(port);

console.log('The magic happens on port '+port);
