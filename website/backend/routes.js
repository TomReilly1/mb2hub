const express = require('express');
const router = express.Router();
const { getCultures, getCultureId } = require('./controller');


router.get('/cultures', getCultures)

router.get('/cultures/:id', getCultureId)





module.exports = router;

