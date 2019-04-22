import Vue from 'vue'
import App from './App'
import router from './router'
import VueMask from 'v-mask'
import VueScheduler from 'v-calendar-scheduler'
import 'v-calendar-scheduler/lib/main.css'

import acl from './acl'

Vue.use(VueScheduler)
Vue.config.productionTip = false
Vue.use(VueMask)
Vue.config.productionTip = false

export const API_URL = 'http://localhost:5000/api/v1/'
export const eBus = new Vue()

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  acl,
  render: h => h(App)
})
