const Cultures = require('./model');

const getCultures = async (req, res) => {
    try {
        const cltr = await Cultures.find({});
        res.json(cltr);
        console.log(cltr);
    } catch (error) {
        res.status(500).json({message: error});
        console.log('ERROR');
    }
}

const getCultureId = async (req, res) => {
    const cultureId = await Cultures.find({'id': req.params.id});
    console.log(req.params.id);
    res.json(cultureId);

}

// const postCultureId = async (req, res) => {
//     const cultureId = await Cultures.find({'id': req.params.id});
//     console.log(req.params.id);
//     res.json(cultureId);

// }


module.exports = {
    getCultures,
    getCultureId,
}
