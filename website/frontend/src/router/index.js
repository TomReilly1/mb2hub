import { createRouter, createWebHistory } from 'vue-router';
import SearchView from '@/views/SearchView.vue';


const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('@/views/HomeView.vue'),
    },
    {
        path: '/search',
        name: 'search',
        component: SearchView,
    },
    {
        path: '/table/:concept',
        name: 'tableview',
        component: () => import('@/views/TableView.vue'),
    },
    {
        path: '/card/:concept/:id',
        name: 'cardview',
        component: () => import('@/views/CardView.vue')
    },
    {
        path: '/404',
        name: 'errorview',
        component: () => import('@/views/ErrorView.vue')
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'notfoundview',
        redirect: '/404'
    }
]


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})



export default router;
