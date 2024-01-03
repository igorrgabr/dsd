const WebSocket = require('ws');
const http = require('http');
const fs = require('fs');

// Criar um servidor HTTP para lidar com solicitações iniciais
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('WebSocket server is running.');
});

// Criar um servidor WebSocket associado ao servidor HTTP
const wss = new WebSocket.Server({ server });

// Evento de conexão com o cliente WebSocket
wss.on('connection', (ws) => {
  console.log('Cliente conectado.');

  // Evento de recebimento de mensagem do cliente
  ws.on('message', (message) => {
    console.log('Mensagem recebida:', message);

    // Se a mensagem for um caminho de arquivo, transmita o arquivo
    if (fs.existsSync(message)) {
      const fileStream = fs.createReadStream(message);
      fileStream.pipe(ws);
    } else {
      // Se não for um caminho de arquivo válido, envie uma mensagem de erro
      ws.send('Arquivo não encontrado.');
    }
  });

  // Evento de fechamento da conexão com o cliente
  ws.on('close', () => {
    console.log('Cliente desconectado.');
  });
});

// Inicie o servidor HTTP
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Servidor HTTP e WebSocket ouvindo na porta ${PORT}`);
});
