import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueMask from 'v-mask'
import VueScheduler from 'v-calendar-scheduler'
import 'v-calendar-scheduler/lib/main.css'

Vue.use(VueScheduler)
Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.use(VueMask)

export const API_URL = 'http://localhost:5000/api/v1/'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
