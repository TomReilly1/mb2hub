const app = require("./index")

const port = process.env.EXPRESS_PORT
app.listen(port, () => {
    console.log(`App listening on port ${port}`)
})
