var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'application/json'});
  res.end(JSON.stringify({
    "message": "Hello Madrid Devops!",
    "wat": Array(16).join('wat' - 1) + ' Batman!'
  }));
}).listen(1337, '0.0.0.0');
