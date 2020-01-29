import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import PollDetail from '../components/PollDetail'
import UserDetail from '../components/UserDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/polls/:id',
    name: 'poll-detail',
    component: PollDetail
  },
  {
    path: '/users/:id',
    name: 'user-detail',
    component: UserDetail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
