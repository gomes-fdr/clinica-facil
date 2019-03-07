<template>
<section>
  <navegacao/>
  <section class="hero is-link is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <paciente-tabs/>
      </div>
    </div>
    <roda-pe/>
  </section>
</section>
</template>

<script>
import Navegacao from './components/navegacao'
import RodaPe from './components/roda-pe'
import PacienteTabs from './components/paciente/main'

export default {
  name: 'Paciente',
  components: {
    Navegacao,
    RodaPe,
    PacienteTabs
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