const express = require('express');
const db = require('./db');
const router = express.Router();

// NOTE: exclude any dummy armor
const armor_sql = "SELECT * FROM armor WHERE id NOT LIKE '%dummy%' ORDER BY head_ar DESC LIMIT 20;"

// Get Armor
router.get('/armor', async (req, res) => {
    await db.any(armor_sql)
    .then(rows => {
        console.log('Fetched Armor Successfully');
        res.json(rows);
    })
    .catch(error => {
        console.log('Fetch Armor Unsuccessful');
        console.log(error)
    })
})

// Get Bows and Crossbows
const bows_sql = "SELECT * FROM bows_and_crossbows ORDER BY difficulty DESC LIMIT 20;"
router.get('/bows', async (req, res) => {
    await db.any(bows_sql)
    .then(rows => {
        console.log('Fetched Bows and Crossbows Successfully');
        res.json(rows);
    })
    .catch(error => {
        console.log('Fetch Bows and Crossbows Unsuccessful');
        console.log(error)
    })
})


// Get Troops
const npcs_sql = "SELECT * FROM npcs ORDER BY culture, level DESC LIMIT 20;"
router.get('/npcs', async (req, res) => {
    await db.any(npcs_sql)
    .then(rows => {
        console.log('Fetched Npcs Successfully');
        res.json(rows);
    })
    .catch(error => {
        console.log('Fetch Npcs Unsuccessful');
        console.log(error)
    })
})


// Get Weapons

// Get Horses


module.exports = router;

