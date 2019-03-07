import Vue from 'vue'
import VueRouter from 'vue-router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import SimpleVueValidation from 'simple-vue-validator';
import VueResource from 'vue-resource';

import App from './App.vue'
import Paciente from './Paciente.vue'
import Login from './Login.vue'

import EventBus from './plugins/event-bus'

Vue.use(VueRouter)
Vue.use(Buefy)
Vue.use(SimpleVueValidation);
Vue.use(VueResource);
Vue.use(EventBus)

const routes = [
  {path: '/', component: App},
  {path: '/paciente', component: Paciente},
  {path: '/login', component: Login}
]

const router = new VueRouter({
  routes
})

const app = new Vue({
  router
}).$mount('#app')
