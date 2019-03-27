import Vue from 'vue'
import Router from 'vue-router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import SimpleVueValidation from 'simple-vue-validator'
import auth from '../auth'

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

const routerOptions = [
  { path: '/', component: 'Home', beforeEnter: requireAuth },
  { path: '/agenda', component: 'Agenda', beforeEnter: requireAuth },
  { path: '/paciente', component: 'Paciente', beforeEnter: requireAuth },
  { path: '/login', component: 'Login' },
  { path: '*', component: 'NotFound' }
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
Vue.use(Buefy)
Vue.use(SimpleVueValidation)
export default new Router({
  routes,
  mode: 'history'
})
