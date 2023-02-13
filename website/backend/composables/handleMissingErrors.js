const statusCodes = require('../data/statusCodes.json')

exports.handleMissingError = (err, res) => {
    console.error(err)

    if (err.code === '42P01') {
        res.status(470).send(statusCodes[470])
    } else if (err.code === 0) {
        res.status(471).send(statusCodes[471])
    } else {
        res.status(499).send('499 (ERROR) unkown error')
    }
}
