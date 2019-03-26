<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import auth from './auth'

export default {
  name: 'app',
  data () {
    return {
      timer: ''
    }
  },
  created: function () {
    this.timer = setTimeout(function () {
      console.log('Verifica login ')
      if (auth.getToken()) {
        if (auth.isValidJwt(auth.getToken())) {
          console.log('token valido')
        } else {
          console.log('token INVALIDO')
          auth.logout()
        }
      }
    }, 5000)
  }
}
</script>