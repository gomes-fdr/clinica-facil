<script>
import Navegacao from './components/navegacao'
import RodaPe from './components/roda-pe'
import PacienteTabs from './components/paciente/main'

export default {
  components: {
    Navegacao,
    RodaPe,
    PacienteTabs
  }
}
</script>

<template>
<div>
  <navegacao/>
  <section class="hero is-link is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <paciente-tabs/>
      </div>
    </div>
    <roda-pe/>
  </section>
</div>
</template>
<style>
  .hero-body {
    background-color: #3F51B5;
  }
  .hero-foot {
    background-color: white;
  }
</style>