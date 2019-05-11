<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      timer: ''
    }
  },
  beforeCreate () {

  },
  created () {
    // if (auth.isValidJwt(auth.getToken()) === false) {
    //   router.push('login')
    // }
  },
  mounted () {
    // this.timer = setInterval(function () {
    //   if (auth.isValidJwt(auth.getToken()) === false) {
    //     auth.logout()
    //   }
    // }, 1000 * 60 * 30)
  }
}
</script>