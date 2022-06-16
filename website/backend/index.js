const express = require('express');
const app = express();
require('dotenv').config();
const apiRouters = require('./routers/routes');
var cors = require('cors');


app.use(cors());


app.use('/api', apiRouters);


app.get('/', (req, res) => {
  res.send('Hello World!');
});


const port = process.env.EXPRESS_PORT;
app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
