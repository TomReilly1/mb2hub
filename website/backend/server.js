const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const compression = require('compression');

const app = express();


// Middleware
app.use(bodyParser.json());
app.use(cors());
app.options('*', cors())
app.use(compression())


// Router
const apiRouter = require('./api');
app.use('/api/', apiRouter);


// Port
const PORT = 5100;

app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`)
});


