const express = require('express');
const db = require('./db');
const router = express.Router();

// NOTE: exclude any dummy armor
const SQL_STR = "SELECT * FROM armor WHERE id NOT LIKE '%dummy%' ORDER BY head_ar DESC LIMIT 20;"

// Get Armor
router.get('/armor', async (req, res) => {
    await db.any(SQL_STR)
    .then(rows => {
        console.log('Fetched Armor Successfully');
        res.json(rows);
    })
    .catch(error => {
        console.log('Fetch Armor Unsuccessful');
        console.log(error)
    })
})



// Get Troops

// Get Weapons

// Get Horses


module.exports = router;

