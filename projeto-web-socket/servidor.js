const WebSocket = require('ws');
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('WebSocket server is running.');
});

const wss = new WebSocket.Server({ server });

wss.on('connection', (ws) => {
  console.log('Cliente conectado.');

  ws.on('message', (message) => {
    console.log('Mensagem recebida:', message);

    if (fs.existsSync(message)) {
      const fileStream = fs.createReadStream(message);
      fileStream.on('data', (chunk) => {
        // Envie os dados do arquivo como um Buffer
        ws.send(chunk);
      });

      fileStream.on('end', () => {
        // Feche a conexão após o envio completo do arquivo
        ws.send('Fechando conexão. Arquivo enviado com sucesso.');
        ws.close();
      });
    } else {
      ws.send('Arquivo não encontrado.');
    }
  });

  ws.on('close', () => {
    console.log('Cliente desconectado.');
  });
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Servidor HTTP e WebSocket ouvindo na porta ${PORT}`);
});
