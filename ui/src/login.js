import Vue from 'vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import Login from './Login.vue'

Vue.use(Buefy)

new Vue({
  el: '#app',
  render: h => h(Login)
})
