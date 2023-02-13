require('dotenv').config()
const db = require('../db')
const statusCodes = require('../data/statusCodes.json')
const { handleMissingError } = require('../composables/handleMissingErrors')
const { checkForRankings } = require('../composables/checkForRankings')


exports.getSingleItem = async (req, res, next) => {
    const l_concept = req.conceptId
    const l_id = req.itemId

    const sqlStr = `SELECT * FROM ${l_concept} WHERE id = '${l_id}';`
    try {
        const data = await db.one(sqlStr)
        if (data) {
            req.cardData = data
            checkForRankings(req, res, next)
        } else {
            res.status(480).send(statusCodes.CODE_480)
        }
    } catch (err) {
        handleMissingError(err, res)
    }
}
