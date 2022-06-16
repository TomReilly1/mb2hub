const express = require('express');
const db = require('../db');
const router = express.Router();
const pgdb = require('../db');

//----- ROOT -----//
router.get('/', (req,res) => {
    res.send('API router == success');
});

//----- ARMORS -----//
router.get('/armors', (req,res) => {
    db.any('SELECT id,name,culture,weight,type,head_armor,body_armor,arm_armor,leg_armor FROM armors;')
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//----- BOWS -----//
router.get('/bows', (req,res) => {
    const cols = [
        'id',
        'name',
        'culture',
        'weight',
        'type',
        'subtype',
        'difficulty',
        'speed_rating',
        'missile_speed',
        'accuracy',
        'damage',
        'fire_on_mount',
        'reload_on_mount'
    ]
    const cols_str = cols.join();

    db.any(`SELECT ${cols_str} FROM bows;`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//----- CLANS -----//
router.get('/clans', (req,res) => {
    db.any('SELECT id,name,owner,kingdom,culture,tier,is_ruling_clan FROM clans;')
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//----- CULTURES -----//
router.get('/cultures', (req,res) => {
    db.any('SELECT * FROM cultures;')
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/cultures/:id', (req,res) => {
    console.log(`SELECT * FROM cultures WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM cultures WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//----- KINGDOMS -----//
router.get('/kingdoms', (req,res) => {
    const cols = [
        'id',
        'name',
        'title',
        'ruler_title',
        'culture',
        'primary_banner_color',
        'secondary_banner_color',
        'label_color',
        'color_1',
        'color_2',
        'alternative_color_1',
        'alternative_color_2',
        'desc_text'
    ]
    const cols_str = cols.join();

    function handleColorHexes(color) {
        if (color.length === 8) {
            return color.substring(2);
        }
        else if (color.length === 10) {
            return color.substring(4);
        }
        else {
            console.log('no color changes');
            return color;
        }
    }

    db.any(`SELECT ${cols_str} FROM kingdoms;`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//----- LORDS -----//
router.get('/lords', (req,res) => {
    db.any('SELECT id,name,culture,default_group,age,sex FROM lords;')
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//----- TROOPS -----//
router.get('/troops', (req,res) => {
    const cols = [
        'id',
        'name',
        'culture',
        'default_group',
        'occupation',
        'level',
        'upgrade_target_1',
        'upgrade_target_2',
        'one_handed',
        'two_handed',
        'polearm',
        'bow',
        'crossbow',
        'throwing',
        'riding',
        'athletics'
    ]
    const cols_str = cols.join();

    db.any(`SELECT ${cols_str} FROM troops;`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});


module.exports = router;
