import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/armor',
    name: 'armor',
    component: () => import('../views/ArmorView.vue')
  },
  {
    path: '/bows',
    name: 'bows',
    component: () => import('../views/BowsView.vue')
  },
  {
    path: '/troops',
    name: 'troops',
    component: () => import('../views/TroopsView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
