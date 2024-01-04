const WebSocket = require('ws');
const http = require('http');
const express = require('express');
const path = require('path');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const PORT = process.env.PORT || 3000;

const users = [];

wss.on('connection', (ws) => {
    let user = {};

    ws.on('message', (message) => {
        const data = JSON.parse(message);

        switch (data.type) {
            case 'join':
                user = { id: ws._socket.remoteAddress, username: data.username, color: data.color };
                users.push(user);
                broadcastUserList();
                break;
            case 'draw':
                broadcast(message);
                break;
        }
    });

    ws.on('close', () => {
        users.splice(users.indexOf(user), 1);
        broadcastUserList();
    });
});

function broadcast(message) {
    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(message);
        }
    });
}

function broadcastUserList() {
    const userListMessage = JSON.stringify({ type: 'userList', users });
    broadcast(userListMessage);
}

app.use(express.static(path.join(__dirname, 'public')));

server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
