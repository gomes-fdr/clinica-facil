import Vue from 'vue'
import Router from 'vue-router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import SimpleVueValidation from 'simple-vue-validator'
import auth from '../auth'
// import { AclRule } from 'vue-acl'

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
  {
    path: '/',
    component: 'Home',
    beforeEnter: requireAuth,
    meta: {
      rule: 'isAdministracao'
    }
  },
  {
    path: '/agenda',
    component: 'Agenda',
    beforeEnter: requireAuth,
    meta: {
      rule: 'isAdministracao'
    }
  },
  {
    path: '/paciente',
    component: 'Paciente',
    beforeEnter: requireAuth,
    meta: {
      rule: 'isAdministracao'
    }
  },
  {
    path: '/profissional',
    component: 'Profissional',
    beforeEnter: requireAuth,
    meta: {
      rule: 'isAdministracao'
    }
  },
  {
    path: '/login',
    component: 'Login',
    meta: {
      rule: 'isPublico'
    }
  },
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
