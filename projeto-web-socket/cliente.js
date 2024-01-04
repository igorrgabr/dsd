document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const userList = document.getElementById('user-list');

    let username = prompt('Digite seu nome:');
    let color = getRandomColor();

    const ws = new WebSocket('ws://localhost:3000');

    ws.onopen = () => {
        ws.send(JSON.stringify({ type: 'join', username, color }));
    };

    ws.onmessage = (event) => {
        const data = event.data;
    
        // Verificar se o conteúdo recebido é um Blob
        if (data instanceof Blob) {
            // Ler o conteúdo do Blob como texto
            data.text().then((text) => {
                // Tentar analisar o texto como JSON
                try {
                    const jsonData = JSON.parse(text);
                    handleWebSocketData(jsonData);
                } catch (error) {
                    console.error('Erro ao analisar JSON:', error);
                }
            });
        } else {
            // Se não for um Blob, tentar analisar como JSON imediatamente
            try {
                const jsonData = JSON.parse(data);
                handleWebSocketData(jsonData);
            } catch (error) {
                console.error('Erro ao analisar JSON:', error);
            }
        }
    };

    function handleWebSocketData(data) {
        switch (data.type) {
            case 'draw':
                drawLine(data.startX, data.startY, data.endX, data.endY, data.color);
                break;
            case 'userList':
                updateUsersList(data.users);
                break;
        }
    }

    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mouseup', stopDrawing);
    canvas.addEventListener('mousemove', draw);

    let drawing = false;
    let lastX = 0;
    let lastY = 0;

    function startDrawing(e) {
        drawing = true;
        [lastX, lastY] = [e.offsetX, e.offsetY];
    }

    function stopDrawing() {
        drawing = false;
    }

    function draw(e) {
        if (!drawing) return;

        const [startX, startY] = [lastX, lastY];
        const [endX, endY] = [e.offsetX, e.offsetY];

        drawLine(startX, startY, endX, endY, color);

        ws.send(JSON.stringify({ type: 'draw', startX, startY, endX, endY, color }));

        [lastX, lastY] = [endX, endY];
    }

    function drawLine(startX, startY, endX, endY, strokeStyle) {
        ctx.beginPath();
        ctx.moveTo(startX, startY);
        ctx.lineTo(endX, endY);
        ctx.strokeStyle = strokeStyle;
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.closePath();
    }

    function updateUsersList(users) {
        userList.innerHTML = '';
        users.forEach(user => {
            const li = document.createElement('li');
            li.style.color = user.color;
            li.textContent = user.username;
            userList.appendChild(li);
        });
    }

    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});
