import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';

import 'primevue/resources/primevue.min.css'    //core css
import 'primeicons/primeicons.css'              //icons
import 'primevue/resources/themes/bootstrap4-dark-blue/theme.css'


const app = createApp(App);


app.use(PrimeVue, {ripple: true});
app.use(router);


app.mount('#app');
