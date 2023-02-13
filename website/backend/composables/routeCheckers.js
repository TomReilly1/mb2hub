const statusCodes = require('../data/statusCodes.json')


exports.checkValidId = async (req, res, next) => {
    const l_id = req.params.id
    if (!l_id) {
        res.status(461).send(statusCodes[461])
    }
    else if (l_id.match(/^[0-9a-zA-Z_]+$/) === null) {
        res.status(460).send(statusCodes[460])
    } else {
        req.itemId = l_id
        next()
    }
}

exports.checkValidConcept = async (req, res, next) => {
    const l_concept = req.params.concept
    if (!l_concept) {
        res.status(461).send(statusCodes[461])
    }
    if (l_concept.match(/^[a-z_]+$/) === null) {
        res.status(460).send(statusCodes[460])
    } else {
        req.conceptId = l_concept
        next()
    }
}
