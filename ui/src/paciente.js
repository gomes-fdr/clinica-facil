import Vue from 'vue'
import Buefy from 'buefy'
import Vuelidate from 'vuelidate'
import 'buefy/dist/buefy.css'

import Paciente from './Paciente.vue'

Vue.use(Buefy)
Vue.use(Vuelidate)

new Vue({
  el: '#app',
  render: h => h(Paciente)
})
