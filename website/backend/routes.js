const express = require('express');
const db = require('./db');
const router = express.Router();


//--------------- ROOT ---------------//
router.get('/', (req,res) => {
    res.send('API router == success');
});

//--------------- ARMORS ---------------//
router.get('/armors', (req,res) => {
    const cols = [
        'id',
        'name',
        'culture',
        'weight',
        'type',
        'head_armor',
        'body_armor',
        'arm_armor',
        'leg_armor'
    ]
    const cols_str = cols.join();

    db.any(`SELECT ${cols_str} FROM armors;`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/armors/:id', (req,res) => {
    console.log(`SELECT * FROM armors WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM armors WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//--------------- BOWS ---------------//
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

router.get('/bows/:id', (req,res) => {
    console.log(`SELECT * FROM bows WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM bows WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//--------------- CLANS ---------------//
router.get('/clans', (req,res) => {
    const cols = [
        'id',
        'name',
        'owner',
        'kingdom',
        'culture',
        'tier',
        'is_ruling_clan'
    ]
    const cols_str = cols.join();

    db.any(`SELECT ${cols_str} FROM clans;`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/clans/:id', (req,res) => {
    console.log(`SELECT * FROM clans WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM clans WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//--------------- CULTURES ---------------//
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

//--------------- GOODS ---------------//
router.get('/goods', (req,res) => {
    db.any('SELECT * FROM goods;')
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/goods/:id', (req,res) => {
    console.log(`SELECT * FROM goods WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM goods WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//--------------- KINGDOMS ---------------//
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

    db.any(`SELECT ${cols_str} FROM kingdoms;`)
    .then(rows => {
        rows.forEach(obj => {
            console.log(obj['name']);
        });
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/kingdoms/:id', (req,res) => {
    console.log(`SELECT * FROM kingdoms WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM kingdoms WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//--------------- LORDS ---------------//
router.get('/lords', (req,res) => {
    const cols = [
        'id',
        'name',
        'culture',
        'default_group',
        'age',
        'sex'
    ]
    const cols_str = cols.join();

    db.any(`SELECT ${cols_str} FROM lords;`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/lords/:id', (req,res) => {
    console.log(`SELECT * FROM lords WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM lords WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//--------------- TOWNS ---------------//
router.get('/towns', (req,res) => {
    const cols = [
        "id",
        "name",
        "owner_id",
        "owner_name",
        "culture",
        "x_position",
        "y_position",
        "prosperity",
        "wall_level",
        "desc_text",
        "bound_village_1",
        "bound_village_2",
        "bound_village_3",
        "bound_village_4"
    ]
    const cols_str = cols.join();

    db.any(`SELECT ${cols_str} FROM towns;`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

router.get('/towns/:id', (req,res) => {
    console.log(`SELECT * FROM towns WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM towns WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});

//--------------- TROOPS ---------------//
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

router.get('/troops/:id', (req,res) => {
    console.log(`SELECT * FROM troops WHERE id = ${req.params['id']};`);

    db.one(`SELECT * FROM troops WHERE id = '${req.params['id']}';`)
    .then(rows => {
        console.log(rows);
        res.json(rows);
    })
    .catch(error => {
        console.log(error);
    })
});



module.exports = router;
