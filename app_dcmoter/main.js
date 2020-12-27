const electron = require("electron");
const express = require("express");
const exapp = express();
const router = express.Router();
const elapp = electron.app;
exapp.use(express.static("public"));
exapp.listen(3000, "127.0.0.1");

elapp.on("ready", function () {
  var main = new electron.BrowserWindow({width: 800, height: 600});
  main.on("closed", electron.app.quit);
  main.webContents.openDevTools();
  main.loadURL("http://127.0.0.1:3000/");
});

exapp.get("/index", (req, res)=>{
  //res.render("hello.ejs");
  var {PythonShell} = require('python-shell');
  PythonShell.run('bdm_move_dcmoter_gpio20.py', null, function (err, data) {
    if (err) throw err;
    console.log(data)
    console.log('finished');
  });
});
