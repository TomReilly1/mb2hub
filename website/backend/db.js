const pgp = require('pg-promise')();
require('dotenv').config()


const host = process.env.MB2_DB_HOST;
const port = process.env.MB2_DB_PORT;
const db_name = process.env.MB2_DB_NAME;
const user = process.env.MB2_DB_USER;


const conn_obj = {
    host: host,
    port: port,
    database: db_name,
    user: user,
};


const db = pgp(conn_obj);


module.exports = db;
