import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


import PrimeVue from 'primevue/config'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primevue/resources/themes/bootstrap4-dark-blue/theme.css'


import '../style.css'

const app = createApp(App)


app.use(router)
app.use(PrimeVue, {ripple: true})


app.mount('#app')
