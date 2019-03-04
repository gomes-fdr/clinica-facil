import Vue from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import SimpleVueValidation from 'simple-vue-validator';
import VueTheMask from 'vue-the-mask'

import Paciente from './Paciente.vue'
import EventBus from './plugins/event-bus'

import VueResource from 'vue-resource';

Vue.use(SimpleVueValidation);
Vue.use(Buefy)
Vue.use(EventBus)
Vue.use(VueTheMask)
Vue.use(VueResource);

new Vue({
  el: '#app',
  render: h => h(Paciente)
})
