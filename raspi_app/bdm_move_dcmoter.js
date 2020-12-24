const express = require('express');
const app = express();

const rpio = require('rpio');
const LED_PIN21 = 40; // GPIO21
rpio.open(LED_PIN_21, rpio.OUTPUT, rpio.LOW);

app.use(express.static('public'));


app.get('/', (req, res) => {
  res.render('hello.ejs');
});


app.get('/index', (req, res) => {
  res.render('index.ejs');
  for (var i = 0; i < 1000; i++ ) {
    rpio.write(LED_PIN21, rpio.HIGH);
    rpio.msleep(500);
    rpio.write(LED_PIN21, rpio.LOW);
    rpio.msleep(500);
 }
});


app.listen(3000);