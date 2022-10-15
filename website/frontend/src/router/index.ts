import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
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
})

export default router
