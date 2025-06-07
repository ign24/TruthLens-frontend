import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => HomeView
  },
  {
    path: '/translator',
    name: 'translator',
    component: () => import('../views/TranslatorView.vue')
  },
  {
    path: '/voice-assistant',
    name: 'voice-assistant',
    component: () => import('../views/VoiceAssistantView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router