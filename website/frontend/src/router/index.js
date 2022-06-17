import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/table/:concept',
    name: 'tableview',
    component: () => import('../views/TableView.vue'),
  },
  {
    path: '/card/:concept/:id',
    name: 'cardview',
    component: () => import('../views/CardView.vue')
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})



export default router;
