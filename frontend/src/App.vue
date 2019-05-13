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
    this.logout()
  },
  mounted () {
  },
  methods: {
    logout () {
      clearTimeout(this.timer)
      this.timer = setTimeout(() => {
        // Log out the user
        this.$session.destroy()
        location.reload()
      }, 30 * 60 * 1000)
    }
  }
}
</script>