import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import CulturesView from "@/views/CulturesView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
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
  {
    path: '/skills',
    name: 'skills',
    component: () => import('../views/SkillsView.vue')
  },
  {
    path: '/kingdoms',
    name: 'kingdoms',
    component: () => import('../views/KingdomsView.vue')
  },
  {
    path: '/cultures',
    name: 'cultures',
    component: CulturesView
  },
  {
    path: '/lords',
    name: 'lords',
    component: () => import('../views/LordsView.vue')
  },
  {
    path: '/clans',
    name: 'clans',
    component: () => import('../views/ClansView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
