const express = require('express');
require('dotenv').config();
const db = require('./db');
const router = express.Router();
const { MeiliSearch } = require('meilisearch');
const dataCols = require('./datacols.json');


//--------------- ROOT ---------------//
router.get('/', (req,res) => {
    res.send('Main API router --> success');
});

//--------------- SEARCH ---------------//
router.get('/search', async (req,res) => {
    console.log('req query searchstr == ' + req.query.searchstr);
    const temp = req.query.searchstr;
    const santzStr = temp.replace(/[^a-z ]/gi, '');
    console.log('santzStr == ' + santzStr);


    const client = new MeiliSearch({
        host: `http://127.0.0.1:7700`,
        apiKey: process.env.MASTER_KEY,
    });

    const indx = client.index('mb2_reduced');

    const response = await indx.search(santzStr, {
        limit: 5
    });

    console.log(response);
    res.json(response);
});

//--------------- CONCEPTS ---------------//
router.get('/:concept', (req,res) => {
    let flag = false;
    let cols;

    console.log(req.params.concept);

    for (let i of dataCols) {
        if (i.concept === req.params.concept) {
            cols = i.data;
            flag = true;
            break;
        }
    }

    if (flag === false) {
        console.error('NOT FOUND');
        res.redirect('/error');
    }

    const cols_str = cols.join();

    db.any(`SELECT ${cols_str} FROM ${req.params.concept};`)
    .then(rows => {
        // console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/:concept/:id', (req,res) => {
    console.log(req.params.concept);
    console.log(req.params.id);


    let flag = false;
    let cols;


    for (let i of dataCols) {
        if (i.concept === req.params.concept) {
            cols = i.data;
            flag = true;
            break;
        }
    }


    if (flag === false) {
        console.error('NOT FOUND');
        res.redirect('/error');
    }


    const cols_str = cols.join();


    db.one(`SELECT ${cols_str} FROM ${req.params.concept} WHERE id = '${req.params['id']}';`)
    .then(rows => {
        // console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});


router.get('/error', (req,res) => {
    res.send('404 (ERROR) not found')
})

module.exports = router;
