/*
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
*/

var http = require("http");
var fs = require("fs");

var server = http.createServer();
server.on("request", getJs);
server.listen(8080);
console.log("Server running …");

function getJs(req, res) {
  var url = req.url;
  console.log(url);
  if ("/" == url) {
    fs.readFile("./js.html", "UTF-8", function (err, data) {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.write(data);
      res.end();
    });
  } else if ("/test.js" == url) {
    fs.readFile("./test.js", "UTF-8", function (err, data) {
      res.writeHead(200, {"Content-Type": "text/plain"});
      res.write(data);
      res.end();
    });
  }
}

