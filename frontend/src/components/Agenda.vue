<template>
  <div>
    <navegacao/>
    <section class="hero is-link is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <vue-scheduler/>
        </div>
      </div>
      <roda-pe/>
    </section>
  </div>
</template>

<script>
import Navegacao from './Navegacao'
import RodaPe from './RodaPe'

export default {
  name: 'App',
  components: {
    Navegacao,
    RodaPe
  }
}
</script>

<style>
.hero-body {
  background-color: #3f51b5;
}
.hero-foot {
  background-color: white;
}
</style>