require('dotenv').config()
const db = require('../db')
const statusCodes = require('../data/statusCodes.json')
const { handleMissingError } = require('../composables/handleMissingErrors')

exports.getRankings = async (req, res) => {
    const l_concept = req.conceptId
    const l_id = req.itemId

    console.log(l_concept)

    try {
        let rankings_view_name = ''
        if (l_concept == 'armors') {
            console.log('IS ARMOR')
            const armorType = req.cardData['type'].slice(0, -5).toLowerCase()
            rankings_view_name = armorType + '_armor_rankings_view'
        } else {
            rankings_view_name = l_concept + '_rankings_view'
        }

        console.log(rankings_view_name)
        const rankSqlStr = `SELECT * FROM ${rankings_view_name} WHERE id = '${l_id}';`
        const data = await db.one(rankSqlStr)

        if (!data) {
            res.status(480).send(statusCodes[480])
        }

        let rankings = {
            attributes: {},
            totalRecords: 0
        }

        for (let key in data) {
            if (key == 'id' || key == 'name') {
                continue
            }
            
            // deconstruct the key to get the field name and the type of rank
            const strArr = key.split('_')
            const rankType = strArr.slice(-2, -1)[0]
            const fieldName = strArr.slice(0, -2).join('_')

            if (rankings.attributes[fieldName] === undefined) {
                rankings.attributes[fieldName] = {}
            }

            try {
                if (typeof data[key] === 'string') {
                    rankings.attributes[fieldName][rankType] = parseInt(data[key])
                } else {
                    rankings.attributes[fieldName][rankType] = data[key]
                }
            } catch (error) {
                throw Error('Error: could not assign rank to field')
            }
        }

        const countSqlStr = `SELECT COUNT(*) FROM ${rankings_view_name};`
        const count_total = await db.one(countSqlStr)
        if (count_total === 0) {
            res.status(480).send(statusCodes[480])
        }
        rankings.totalRecords = parseInt(count_total.count)

        // console.log(rankings)

        output = {
            cardData: req.cardData,
            metaData: req.metaData,
            rankData: rankings
        }

        res.json(output)
    } catch (err) {
        handleMissingError(err, res)
    }
}
