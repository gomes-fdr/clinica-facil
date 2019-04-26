<template>
  <div>
    <navegacao/>
    <section class="hero is-link is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="container">
          <tabs/>
        </div>
      </div>
      <roda-pe/>
    </section>
  </div>
</template>

<script>
import Navegacao from './Navegacao'
import RodaPe from './RodaPe'
import Tabs from './agenda/Tabs'

// <vue-scheduler/>

export default {
  name: 'App',
  components: {
    Navegacao,
    RodaPe,
    Tabs
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