<template>
<div>
  <navegacao/>
  <section class="hero is-link is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <p class="title">
          Sistema de Gestão da Clinica Darmas
        </p>
      </div>
    </div>
    <roda-pe/>
  </section>
</div>
</template>

<script>
import Navegacao from './navegacao'
import RodaPe from './roda-pe'

export default {
  name: 'App',
  components: {
    Navegacao,
    RodaPe
  },
  data() {
    return {
      authenticated: false,
    }
  },
  mounted() {
    if (!this.authenticated) {
      this.$router.replace({name: 'login'});
    }
  },
  methods: {
    setAuthenticated(status) {
        this.authenticated = status;
    },
    logout() {
        this.authenticated = false;
    }
  }
}
</script>

<style>
  .hero-body {
    background-color: #3F51B5;
  }
  .hero-foot {
    background-color: white;
  }
</style>