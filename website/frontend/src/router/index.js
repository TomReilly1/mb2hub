import { createRouter, createWebHistory } from 'vue-router';


const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('@/views/HomeView.vue'),
    },
    {
        path: '/news',
        name: 'news',
        component: () => import('@/views/NewsView.vue'),
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
