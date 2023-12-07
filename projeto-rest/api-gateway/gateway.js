/* API Gateway */

// lib
const express = require('express');
const axios = require('axios');
const cors = require('cors');
const CryptoJS = require('crypto-js');
//

// doc
const swaggerUi = require('swagger-ui-express');
const swaggerSpec = require('./swaggerConfig');
//

const app = express();
const PORT = 1234;

app.use(cors());

/**
 * @swagger
 * /:
 *   get:
 *     summary: Retorna uma mensagem indicando que o API Gateway está rodando.
 *     responses:
 *       200:
 *         description: OK
 */
app.get('/', (req, res) => {
    res.send('API Gateway está rodando!');
});

app.listen(PORT, () => {
    console.log(`Servidor está rodando na porta ${PORT}`);
});

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

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
 *     summary: Retorna dados de um personagem da Marvel e GIFs relacionados.
 *     parameters:
 *       - in: path
 *         name: charName
 *         schema:
 *           type: string
 *         required: true
 *         description: Nome do personagem da Marvel.
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             example:
 *               charData: { Marvel Character Data }
 *               gifs: { Giphy GIFs Data }
 *       500:
 *         description: Erro interno do servidor
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