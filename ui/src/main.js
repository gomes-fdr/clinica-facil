import Vue from 'vue'
import VueRouter from 'vue-router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import SimpleVueValidation from 'simple-vue-validator';
import VueResource from 'vue-resource';

import App from './components/App'
import Paciente from './components/Paciente'
import Login from './components/Login'

import EventBus from './plugins/event-bus'
import auth from './auth'

Vue.use(VueRouter)
Vue.use(Buefy)
Vue.use(SimpleVueValidation);
Vue.use(VueResource);
Vue.use(EventBus)

function requireAuth (to, from, next) {
  if (!auth.loggedIn()) {
    next({
      path: '/login',
      query: { redirect: to.fullPath }
    })
  } else {
    next()
  }
}

const routes = [
  {path: '/', component: App, beforeEnter: requireAuth},
  {path: '/paciente', component: Paciente, beforeEnter: requireAuth},
  {path: '/login', component: Login},
  {path: '/logout',
    beforeEnter (to, from, next) {
      auth.logout()
      next('/')
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

const app = new Vue({
  router
}).$mount('#app')
