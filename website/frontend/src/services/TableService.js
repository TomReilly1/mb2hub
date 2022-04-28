export default class TableService {

    async getArmorData() {
        return fetch('http://localhost:5100/api/armor')
        .then(res => res.json())
    }

    async getBowsAndCrossbowsData() {
        return fetch('http://localhost:5100/api/bows')
        .then(res => res.json())
    }

//     getProductsSmall() {
// 		return fetch('demo/data/products-small.json').then(res => res.json()).then(d => d.data);
// 	}

// 	getProducts() {
// 		return fetch('demo/data/products.json').then(res => res.json()).then(d => d.data);
//     }

//     getProductsWithOrdersSmall() {
// 		return fetch('demo/data/products-orders-small.json').then(res => res.json()).then(d => d.data);
// 	}
}
