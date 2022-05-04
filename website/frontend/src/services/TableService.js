const PATH = '/home/salam/json'
// const PATH = '../data'

export default class TableService {

    async getArmorData() {
        return await require(`${PATH}/armors.json`);
    }

    async getBowsAndCrossbowsData() {
        return await require(`${PATH}/bows_and_crossbows.json`);
    }

    async getNpcsData() {
        return await require(`${PATH}/npcs.json`);
    }

    async getKingdomsData() {
        return await require(`${PATH}/kingdoms.json`);
    }

    async getCulturesData() {
        return await require(`${PATH}/cultures.json`);
    }

}
