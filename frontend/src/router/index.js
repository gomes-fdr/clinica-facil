import Vue from 'vue'
import Router from 'vue-router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import SimpleVueValidation from 'simple-vue-validator'

const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/paciente', component: 'Paciente' },
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
