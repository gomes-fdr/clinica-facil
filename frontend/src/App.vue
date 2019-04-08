<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import auth from './auth'
import router from './router'

export default {
  name: 'app',
  data () {
    return {
      timer: '',
      bChecked: false
    }
  },
  created () {
    if (auth.isValidJwt(auth.getToken()) === false) {
      // Para tokens antigos
      delete localStorage.token
      router.push('login')
    }
  },
  mounted: function () {
    this.timer = setInterval(function () {
      if (auth.isValidJwt(auth.getToken()) === false) {
        auth.logout()
      }
    }, 1000 * 60 * 30)
  }
}
</script>