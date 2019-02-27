<script>
import Navegacao from './components/navegacao'
export default {
  components: {
    Navegacao
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
  </section>
  <footer class="footer">
    <div class="content has-text-centered">
      <p>
        <strong>Clinica Fácil</strong> por <a href="https://gomes-fdr.github.io">Fabiano Gomes</a>
      </p>
    </div>
  </footer>
</div>
</template>
<style>
  .hero-body {
    background-color: #3F51B5;
  }
</style>