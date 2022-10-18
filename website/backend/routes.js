const express = require('express')
require('dotenv').config()
const db = require('./db')
const router = express.Router()


//--------------- ROOT ---------------//
router.get('/', (req,res) => {
    res.send('API router --> success')
})

//--------------- SEARCH ---------------//
router.get('/search', async (req,res) => {
    const l_search = req.query.searchstr
    if (l_search.match(/^[a-z ]+$/i) === null) { 
        // searchStr contains char other than alphabet and space
        res.status(480).send('480 (ERROR) not found')
    }
    const santzStr = l_search.replace(/[^a-z ]/gi, '')
    const qryStr = `SELECT * FROM mb2_global_view WHERE name ILIKE '%${santzStr}%' ORDER BY name LIMIT 30;`

    db.any(qryStr)
    .then(rows => {
        console.log(rows)
        res.json(rows)
    })
    .catch((e) => {
        console.log(e)
        res.status(470).send('470 (ERROR) no match')
    })
})

//--------------- CONCEPTS ---------------//
router.get('/:concept', async (req,res) => {
    const l_concept = req.params.concept

    if (l_concept.match(/^[a-z]+$/) === null) { 
        // :concept contains char other than lowercase alphabet
        res.status(460).send('460 (ERROR) not found')
    }

    db.any(`SELECT * FROM ${l_concept};`)
    .then(rows => {
        console.log(rows)
        res.json(rows)
    })
    .catch((e) => {
        console.log(e)
        res.status(470).send('470 (ERROR) no match')
    })
})


router.get('/:concept/:id', (req,res) => {
    const l_concept = req.params.concept

    if (l_concept.match(/^[a-z]+$/) === null) {
        // :concept contains char other than lowercase alphabet
        res.status(460).send('460 (ERROR) not found')
    }
    const l_id = req.params.id;
    if (l_id.match(/^[0-9A-Za-z_]+$/) === null) {
        // :id contains char other than alphanumeric or underscore
        res.status(460).send('460 (ERROR) not found')
    }

    db.one(`SELECT * FROM ${l_concept} WHERE id = '${l_id}';`)
    .then(rows => {
        res.json(rows)
    })
    .catch(() => {
        res.status(470).send('470 (ERROR) no match')
    })
})



module.exports = router
