/* API Gateway */

// doc
const swaggerJSDoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');
//

// lib
const express = require('express');
const axios = require('axios');
const cors = require('cors');
const CryptoJS = require('crypto-js');
//

const app = express();
const PORT = 1234;

app.use(cors());

// Definição Swagger Doc
const swaggerOptions = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'API Gateway para Marvel e Giphy',
            version: '1.0.0',
            description: 'Documentação da API Gateway que integra a Marvel API e a Giphy API.'
        },
        servers: [
            {
                url: `http://localhost:${PORT}`,
                description: 'Servidor local',
            },
        ],
    },
    apis: ['gateway-js'],
};
const swaggerSpec = swaggerJSDoc(swaggerOptions);
//

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

app.get('/', (req, res) => {
    res.send('API Gateway está rodando!');
});

app.listen(PORT, () => {
    console.log(`Servidor está rodando na porta ${PORT}`);
});

// Integração APIs
const PUBLIC_MARVEL_API_KEY = '057d11d69f444d996536e0bc90bb3cff';
const PRIVATE_MARVEL_API_KEY = '299f6311f8851063dcb3f154f1ebb1b0d678dde3';
const GIPHY_API_KEY = 'SgmY5JmTOPkRYXh4ytP4ZXB5KlUvNi3s';

const timestamp = Date.now().toString();
const hash = CryptoJS.MD5(timestamp + PRIVATE_MARVEL_API_KEY + PUBLIC_MARVEL_API_KEY).toString();

/**
 * @swagger
 * /char/{charName}:
 *   get:
 *     description: Obtém informações sobre um personagem da Marvel e Gifs relacionados da Giphy.
 *     parameters:
 *       - name: charName
 *         description: Nome do personagem da Marvel.
 *         in: path
 *         required: true
 *         type: string
 *     responses:
 *       200:
 *         description: Sucesso. Retorna informações do personagem da Marvel e Gifs relacionados.
 *       500:
 *         description: Erro interno do servidor.
 */
app.get('/char/:charName', async (req, res) => {
    try {
        const charName = req.params.charName;

        // consulta Marvel API
        const marvelResponse = await axios.get(
          `https://gateway.marvel.com/v1/public/characters?name=${charName}&apikey=${PUBLIC_MARVEL_API_KEY}&ts=${timestamp}&hash=${hash}`
        );
        const charData = marvelResponse.data.data.results;

        // consulta Giphy API
        const giphyResponse = await axios.get(
            `https://api.giphy.com/v1/gifs/search?q=${charName}&api_key=${GIPHY_API_KEY}`
        );
        const gifs = charData[0] ? giphyResponse.data.data : '';

        const response = {
            charData: charData,
            gifs: gifs
        };
        res.json(response);

    } catch (error) {
        console.error(error);
        res.status(500).json({error: 'Erro ao processar a requisição!'});
    }
});