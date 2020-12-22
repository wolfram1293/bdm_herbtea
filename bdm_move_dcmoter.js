var rpio = require('rpio');
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
 
var LED_PIN = 40; // GPIO21

rpio.open(LED_PIN, rpio.OUTPUT, rpio.LOW);

for (var i = 0; i < 1000; i++ ) {
    rpio.write(LED_PIN, rpio.HIGH);
    rpio.msleep(500);
    rpio.write(LED_PIN, rpio.LOW);
    rpio.msleep(500);
}
