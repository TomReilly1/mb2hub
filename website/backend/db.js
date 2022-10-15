const pgp = require('pg-promise')()
require('dotenv').config()


const host = process.env.MB2_DB_HOST
const port = process.env.MB2_DB_PORT
const db_name = process.env.MB2_DB_NAME
const user = process.env.MB2_DB_USER
const password = process.env.MB2_DB_PASS


const conn_obj = {
    host: host,
    port: port,
    database: db_name,
    user: user,
    password: password
};


const db = pgp(conn_obj)


module.exports = db
