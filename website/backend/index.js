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


// app.all('*', (req,res) =>{
//   res.status(404).send('<h1>404 (ALL) Page not found</h1>')
// })
app.use((req, res, next) => {
    res.status(404).send("Sorry can't find that!")
})



const port = process.env.EXPRESS_PORT || 4000;
app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});
