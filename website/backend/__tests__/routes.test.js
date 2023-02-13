const request = require("supertest")
const app = require("../index")
const {testBowItem, testBowConcept} = require('../data/test_data')
const statusCodes = require('../data/statusCodes.json')


describe("Test unkown paths", () => {
    test("It should respond with a 404 status code", async () => {
        const response = await request(app).get("/unkown")
        expect(response.statusCode).toBe(404)
        expect(response.body['message']).toBe('unkown route')
    })
    test("It should respond with a 404 status code", async () => {
        const response = await request(app).get("/api/concept/bows/unkown")
        expect(response.statusCode).toBe(404)
    })
    test("It should respond with a 404 status code", async () => {
        const response = await request(app).get("/api/concept/bows/item/composite_steppe_bow/unkwon")
        expect(response.statusCode).toBe(404)
    })
})

describe("Test unmatched paths", () => {
    test("It should respond with a 470 status code", async () => {
        const response = await request(app).get("/api/concept/unkown")
        expect(response.statusCode).toBe(470)
        expect(response.text).toBe(statusCodes[470])

    })
    test("It should respond with a 471 status code", async () => {
        const response = await request(app).get("/api/concept/bows/item/unkown")
        expect(response.statusCode).toBe(471)
        expect(response.text).toBe(statusCodes[471])
    })

})

describe("Test the root path '/'", () => {
    test("It should respond with a 200 status code", async () => {
        const response = await request(app).get("/api")
        expect(response.statusCode).toBe(200)
    })
    test("It should response the proper text data", async () => {
        const response = await request(app).get("/api")
        expect(response.text).toBe('API ROOT')
    })
})

describe("Test the path '/concept/:concept'", () => {
    // should respond with json of array of concept items
    // should respond with 200 status code
    // should specify json in content type header
    test("It should respond with a 200 status code", async () => {
        const response = await request(app).get("/api/concept/bows")
        expect(response.statusCode).toBe(200)
    })
    test("It should respond with json as content-type header", async () => {
        const response = await request(app).get("/api/concept/bows")
        expect(response.headers['content-type']).toEqual(expect.stringContaining('json'))
    })
    test("It should respond with a json array of concept items", async () => {
        const response = await request(app).get("/api/concept/bows")
        expect(response.body[0]).toMatchObject(testBowConcept[0])
        expect(response.body[0]['speed_rating']).toBeDefined()
        expect(typeof response.body[0]['speed_rating']).toBe('number')
    })
})

describe("Test the path '/concept/:concept/item/:id'", () => {
    // should respond with json object of a concept item
    // should respond with 200 status code
    // should specify json in content type header
    test("It should respond with a 200 status code", async () => {
        const response = await request(app).get("/api/concept/bows/item/crossbow_g")
        expect(response.statusCode).toBe(200)
    })
    test("It should respond with json as content-type header", async () => {
        const response = await request(app).get("/api/concept/bows/item/crossbow_g")
        expect(response.headers['content-type']).toEqual(expect.stringContaining('json'))
    })
    test("It should respond with a json object that contains cardData and rankData", async () => {
        const response = await request(app).get("/api/concept/bows/item/crossbow_g")
        expect(response.body['cardData']).toBeDefined()
        expect(response.body['rankData']).toBeDefined()
        expect(response.body['rankData']['attributes']).toBeDefined()
        expect(response.body['rankData']['attributes']['speed_rating']).toBeDefined()
        expect(response.body['rankData']['attributes']['speed_rating']['standard']).toBeDefined()
        expect(response.body['rankData']['attributes']['speed_rating']['percent']).toBeDefined()
        expect(response.body['rankData']['totalRecords']).toBe(28)
    })
    test("It should respond with a json object of a bow item", async () => {
        const response = await request(app).get("/api/concept/bows/item/crossbow_g")
        expect(response.body).toMatchObject(testBowItem)
        expect(response.body['cardData']['speed_rating']).toBe(80)
    })
})



// describe("Test the path '/search'", () => {
//     test("It should respond with a 200 status code", async () => {
//         const response = await request(app).get("/api/search?searchstr=banne")
//         expect(response.statusCode).toBe(200)
//     })
//     test("It should respond with json as content-type header", async () => {
//         const response = await request(app).get("/api/search?searchstr=banne")
//         expect(response.headers['content-type']).toEqual(expect.stringContaining('json'))
//     })
//     test("It should respond with a json array of concept items", async () => {
//         const response = await request(app).get("/api/search?searchstr=banne")
//         expect(response.body[0]['speed_rating']).toBeDefined()
//     })
// })


// describe("Test the path '/rankings/:concept/:id'", () => {
//     test("It should respond with a 200 status code", async () => {
//         const response = await request(app).get("/api/rankings/bows/composite_steppe_bow")
//         expect(response.statusCode).toBe(200)
//     })
//     test("It should respond with json as content-type header", async () => {
//         const response = await request(app).get("/api/rankings/bows/composite_steppe_bow")
//         expect(response.headers['content-type']).toEqual(expect.stringContaining('json'))
//     })
//     test("It should respond with a json array of concept items", async () => {
//         const response = await request(app).get("/api/rankings/bows/composite_steppe_bow")
//         expect(response.body[0]['speed_rating']).toBeDefined()
//     })
// })

