import Vue from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import SimpleVueValidation from 'simple-vue-validator';

import Paciente from './Paciente.vue'



Vue.use(SimpleVueValidation);
Vue.use(Buefy)

new Vue({
  el: '#app',
  render: h => h(Paciente)
})
