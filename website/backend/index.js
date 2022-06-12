const express = require('express')
require('dotenv').config()

const app = express()


app.get('/', (req, res) => {
  res.send('Hello World!')
})


const port = 3000;
app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
