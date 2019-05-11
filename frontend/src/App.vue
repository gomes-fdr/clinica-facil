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
    if (!this.$session.exists()) {
      this.$router.push('/login')
    }
  },
  created () {
  },
  mounted () {
  }
}
</script>