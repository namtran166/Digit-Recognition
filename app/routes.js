const fs = require('fs');
const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');
const PNG = require('png-js');
const Jimp = require('jimp');
const getPixels = require('get-pixels');


module.exports = (app) => {
    app.use(function (req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
    });

    app.get('/', async (req, res, next) => {
        // const model = await tf.loadModel('http://localhost:3000/model.json');
        res.render('index.ejs');
    });

    app.post('/upload', async (req, res, next) => {
        // const model = await tf.loadModel('http://localhost:3000/model.json');
        console.log(req.body);
    });

}