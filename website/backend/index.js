const express = require('express')
const app = express()
require('dotenv').config()
const cors = require('cors')
const helmet = require('helmet')
const indexRouter = require('./routers/indexRouter')


app.use(cors())
app.use(helmet())

app.use('/api', indexRouter)

app.get('*', (req, res) => {
    res.status(404).json({message: 'unkown route'})
})


module.exports = app
