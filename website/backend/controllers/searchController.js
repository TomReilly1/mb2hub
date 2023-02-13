require('dotenv').config()
const db = require('../db')
const statusCodes = require('../data/statusCodes.json')
const { handleMissingError } = require('../composables/handleMissingErrors')


exports.querySearch = async (req, res) => {
    const l_search = req.query.searchstr

    if (!l_search) {
        res.status(465).send(statusCodes.CODE_465)
    }

    if (l_search.match(/^[a-z ]+$/i) === null) { 
        // searchStr contains char other than alphabet and space
        res.status(466).send(statusCodes.CODE_466)
    }

    const santzStr = l_search.replace(/[^a-z ]/gi, '').toLowerCase()
    console.log(santzStr)
    const sqlStr = `SELECT * FROM mb2_global_view WHERE name ILIKE '%${santzStr}%' ORDER BY name LIMIT 30;`
    try {
        const data = await db.any(sqlStr)
        if (data) {
            
            res.json(data)
        } else {
            res.status(480).send(statusCodes.CODE_480)
        }
    } catch (err) {
        handleMissingError(err, res)
    }
}