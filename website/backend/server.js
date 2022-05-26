const express = require('express');
const dotenv = require('dotenv').config();
const connectDB = require('./db')
const port = process.env.PORT || 5000;


// Initiate Express
const app = express();

// Initiate Server
connectDB();

// Router
app.use('/api', require('./routes'));

// Run Server
app.listen(port, () => console.log(`Server started on port ${port}`))
