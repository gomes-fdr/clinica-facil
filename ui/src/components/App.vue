<script>
import Navegacao from './navegacao'
import RodaPe from './roda-pe'

export default {
  name: 'App',
  components: {
    Navegacao,
    RodaPe
  }
}
</script>

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
<style>
  .hero-body {
    background-color: #3F51B5;
  }
  .hero-foot {
    background-color: white;
  }
</style>