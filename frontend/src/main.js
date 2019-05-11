import Vue from 'vue'
import App from './App'
import router from './router'
import VueMask from 'v-mask'
import VueScheduler from 'v-calendar-scheduler'
import 'v-calendar-scheduler/lib/main.css'
import axios from 'axios'

import acl from './acl'
import VueSession from 'vue-session'

Vue.config.productionTip = true

Vue.prototype.$http = axios
Vue.use(VueSession)
Vue.use(VueMask)
Vue.use(VueScheduler, {
  locale: 'pt-br',
  initialView: 'week',
  availableViews: ['week', 'day'],
  labels: {
    today: 'Hoje',
    back: 'Anterior',
    next: 'Próximo',
    month: 'Mês',
    week: 'Semana',
    day: 'Dia',
    all_day: 'Todo o dia'
  },
  timeRange: [8, 20]
})

export const eBus = new Vue()

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  acl,
  render: h => h(App)
})
