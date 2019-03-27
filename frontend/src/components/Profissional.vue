<template>
<section>
  <navegacao/>
  <section class="hero is-link is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <tabs/>
      </div>
    </div>
    <roda-pe/>
  </section>
</section>
</template>

<script>
import Navegacao from './Navegacao'
import RodaPe from './RodaPe'
import Tabs from './profissional/Tabs'

export default {
  name: 'Profissional',
  components: {
    Navegacao,
    RodaPe,
    Tabs
  }
}
</script>

<style scoped>
  .hero-body {
    background-color: #3F51B5;
  }
  .hero-foot {
    background-color: white;
  }
</style>