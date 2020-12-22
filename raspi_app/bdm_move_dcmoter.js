var rpio = require('rpio');
 
var LED_PIN = 40; // GPIO21
 
rpio.open(LED_PIN_1, rpio.OUTPUT, rpio.LOW);
rpio.open(LED_PIN_2, rpio.OUTPUT, rpio.LOW);
rpio.open(LED_PIN_3, rpio.OUTPUT, rpio.LOW);
 
for (var i = 0; i < 1000; i++ ) {
    rpio.write(LED_PIN, rpio.HIGH);
    rpio.msleep(500);
    rpio.write(LED_PIN, rpio.LOW);
    rpio.msleep(500);
}