var WebSocketClient = require('websocket').client;
var client = new WebSocketClient();
var api_gateway = 'wss://{YOUR-API-ID}.execute-api.{YOUR-REGION}.amazonaws.com/prod'

var message = '{ \"message\": \"sendmessage\", \"data\": \"Hello World!\" }';
var custom_headers = { 
  "authorization": "098765",
  "tenant_id": "007-nodejs",
  "customer_name": "nodejs-client"
};

client.on('connect', function(connection) {
    console.log('WebSocket Client Connected');
    connection.send(message)
    connection.close()
});

client.connect(api_gateway, null, null, custom_headers, null);
