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
import Navegacao from './Navegacao'
import RodaPe from './RodaPe'
import PacienteTabs from './paciente/Tabs'

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