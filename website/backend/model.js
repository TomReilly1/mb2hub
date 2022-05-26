const mongoose = require('mongoose');
const { Schema } = mongoose;

const culturesSchema = Schema(
    {
        _id: Schema.Types.ObjectId,
        id: String,
        name: String,
        isMainCulture: Boolean
    },
    {
        collection: 'Cultures'
    }
    // {
    //     _id: {
    //         type: Schema.Types.ObjectId,
    //         required: true
    //     },
    //     id: {
    //         type: String,
    //         required: true
    //     },
    //     name: {
    //         type: String,
    //         required: true
    //     },
    //     isMainCulture: {
    //         type: Boolean,
    //         required: true
    //     }
    // },
    // {
    //     collection: 'Cultures'
    // }
);

module.exports = mongoose.model('Cultures', culturesSchema);

