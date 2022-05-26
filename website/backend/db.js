const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        const conn = await mongoose.connect(process.env.MONGO_URI);

        console.log(`MongoDB Connected: ${conn.connection.collections}`);

        for (let i in conn.connection.collections) {
            console.log(i);
        }
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
}

module.exports = connectDB;
