const rankingsJson = require('../data/rankings.json')

exports.checkForRankings = async (req, res, next) => {
    let hasRankings = false
    for (const field in req.cardData) {
        if (rankingsJson.includes(field)) {
            hasRankings = true
            break
        }
    }

    if (hasRankings) {
        next()
    } else {
        const output = {cardData: req.cardData}
        res.json(output)
    }  
}
