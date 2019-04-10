<template>
  <div id="app">
    {{ $acl.get }}
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
      timer: ''
    }
  },
  created () {
    if (auth.isValidJwt(auth.getToken()) === false) {
      // Para tokens antigos
      delete localStorage.token
      router.push('login')
    }
    localStorage.perfil = auth.getProfile()
    localStorage.setItem('perfil', 'Psicologo')
    this.$acl.change(localStorage.getItem('perfil'))
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