const express = require('express');
const app = express();
require('dotenv').config();
const apiRouter = require('./routes');
const cors = require('cors');
const helmet = require('helmet');


app.use(cors());
app.use(helmet());

app.use('/api', apiRouter);


app.get('/', (req, res) => {
  res.send('Hello World!');
});


const port = process.env.EXPRESS_PORT;
app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
