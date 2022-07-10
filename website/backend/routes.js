const express = require('express');
require('dotenv').config();
const db = require('./db');
const router = express.Router();
const { MeiliSearch } = require('meilisearch');


//--------------- ROOT ---------------//
router.get('/', (req,res) => {
    res.send('API router --> success');
});

//--------------- SEARCH ---------------//
router.get('/search', async (req,res) => {
    const temp = req.query.searchstr;
    const santzStr = temp.replace(/[^a-z ]/gi, '');

    const client = new MeiliSearch({
        host: `http://127.0.0.1:7700`,
        apiKey: process.env.MASTER_KEY,
    });

    const indx = client.index('mb2_reduced');

    const response = await indx.search(santzStr, {
        limit: 5
    });


    res.json(response);
});

//--------------- CONCEPTS ---------------//
router.get('/:concept', async (req,res) => {
    const l_concept = req.params.concept;
    if (l_concept.match(/^[a-z]+$/) === null) { 
        // :concept contains char other than lowercase alphabet
        res.status(460).send('460 (ERROR) not found');
    }


    db.any(`SELECT * FROM ${l_concept};`)
    .then(rows => {
        res.json(rows);
    })
    .catch(() => {
        res.status(470).send('470 (ERROR) no match');
    })
});


router.get('/:concept/:id', (req,res) => {
    const l_concept = req.params.concept;
    if (l_concept.match(/^[a-z]+$/) === null) {
        // :concept contains char other than lowercase alphabet
        res.status(460).send('460 (ERROR) not found');
    }
    const l_id = req.params.id;
    if (l_id.match(/^[0-9A-Za-z_]+$/) === null) {
        // :id contains char other than alphanumeric or underscore
        res.status(460).send('460 (ERROR) not found');
    }


    db.one(`SELECT * FROM ${l_concept} WHERE id = '${l_id}';`)
    .then(rows => {
        res.json(rows);
    })
    .catch(() => {
        res.status(470).send('470 (ERROR) no match');
    })
});



module.exports = router;
