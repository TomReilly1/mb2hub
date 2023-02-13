require('dotenv').config()
const db = require('../db')
const statusCodes = require('../data/statusCodes.json')
const { handleMissingError } = require('../composables/handleMissingErrors')


exports.getConcept = async (req, res) => {
    const concept = req.conceptId

    const sqlStr = `SELECT * FROM ${concept};`
    try {
        const data = await db.many(sqlStr)
        if (data) {
            res.json(data)
        } else {
            res.status(480).send(statusCodes[480])
        }
    } catch (err) {
        handleMissingError(err, res)
    }
}
