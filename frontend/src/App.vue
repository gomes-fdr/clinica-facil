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
  mounted: function () {
    this.timer = setInterval(function () {
      if (!auth.isValidJwt(auth.getToken())) {
        auth.logout()
      }
    }, 1000 * 60 * 30)
  }
}
</script>