const swaggerJSDoc = require('swagger-jsdoc');

const options = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'Marvel Explorer',
            version: '1.0.0',
            description: 'Documentação Marvel API e Giphy API.',
        },
        servers: [
            {
                url: 'http://localhost:1234',
                description: 'Local Development Server',
            }
        ]
    },
    apis: ['gateway.js'],
};

const swaggerSpec = swaggerJSDoc(options);

module.exports = swaggerSpec;