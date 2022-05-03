export default class TableService {

    // async getArmorData() {
    //     return await fetch('http://localhost:5100/api/armor')
    //     .then(res => res.json())
    // }

    async getArmorData() {
        const response = await fetch('http://localhost:5100/api/armor', {
            method: 'GET',
            mode: 'cors',
            credentials: 'same-origin'
        });

        if (response.ok) { 
            let json = await response.json();
            return json;
        } else {
            alert("HTTP-Error: " + response.status);
        }
    }

    async getBowsAndCrossbowsData() {
        return await fetch('http://localhost:5100/api/bows')
        .then(res => res.json())
        .catch(e => console.log(e));
    }

    async getNpcsData() {
        return await fetch('http://api.mb2hub.com/api/npcs')
        .then(res => res.json())
        .catch(e => {
            console.log('ERROR IN FETCH:')
            console.log(e)
        });
    }
}
