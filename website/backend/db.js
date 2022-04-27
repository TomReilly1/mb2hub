const express = require('express');
const pgp = require('pg-promise')();

require('dotenv').config()


const user = process.env.MB2_DB_USER;
const pass = process.env.MB2_DB_PASS;
const ip = process.env.MB2_DB_IP;
const port = process.env.MB2_DB_PORT;
const db_name = process.env.MB2_DB_NAME;


const db = pgp(`postgres://${user}:${pass}@${ip}:${port}/${db_name}`
);


module.exports = db;
