<template>
  <form>
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Novo Horário</p>
      </header>
      <section class="modal-card-body">
       <p  class="modal-card-body">{{ profissional }}</p>
      </section>
      <footer class="modal-card-foot">
        <button class="button" type="button" @click="$parent.close()">Fechar</button>
        <button class="button is-primary" @click.prevent="salvarEvento">Salvar</button>
      </footer>
    </div>
  </form>
</template>
<script>
export default {
  name: 'NovoEvento',
  props: ['dt_inicio', 'dt_fim', 'livre', 'local', 'profissional'],
  methods: {
    salvarEvento () {
      console.log('Salvar NOVO evento')
    }
  }
}
</script>

