import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';
import Dialog from 'primevue/dialog';
import Button from "primevue/button";
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';

import 'primevue/resources/primevue.min.css'    //core css
import 'primeicons/primeicons.css'              //icons
import 'primevue/resources/themes/bootstrap4-dark-blue/theme.css'


const app = createApp(App);


app.use(PrimeVue, {ripple: true});
app.use(router);


app.component('Dialog', Dialog);
app.component('Button', Button);
app.component('DataTable', DataTable);
app.component('Column', Column);
app.component('ColumnGroup', ColumnGroup);
app.component('Row', Row);


app.mount('#app');
