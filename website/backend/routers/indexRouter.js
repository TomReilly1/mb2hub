const indexRouter = require("express").Router()
const conceptCntrl = require('../controllers/conceptController')
const itemCntrl = require('../controllers/itemController')
const rankingsCntrl = require('../controllers/rankingsController')
const searchCnrtl = require('../controllers/searchController')
const { checkValidConcept, checkValidId } = require('../composables/routeCheckers')


indexRouter.get('/', (req, res) => res.send('API ROOT'))

indexRouter.get('/search', searchCnrtl.querySearch)

indexRouter.get('/concept/:concept', checkValidConcept, conceptCntrl.getConcept)

indexRouter.get(
    '/concept/:concept/item/:id',
    checkValidConcept,
    checkValidId,
    itemCntrl.getSingleItem,
    rankingsCntrl.getRankings
)

indexRouter.get('*', (req, res) => {
    res.status(404).json({message: 'unkown route'})
})


module.exports = indexRouter
