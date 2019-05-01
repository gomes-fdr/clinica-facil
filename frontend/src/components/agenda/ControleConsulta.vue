<template>
  <form>
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Controle de Consulta</p>
      </header>
      <section class="modal-card-body">
        <p class=" has-text-black has-text-centered">Profissional</p>
        <p class=" has-text-black has-text-centered">Horário</p>
        <br>
        <form>
          <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Paciente</label>
          </div>
          
          <div class="field-body">
            <div class="field">
              <p class="control">
                <input 
                class="input"
                type="text"
                placeholder="Nome"
                >
              </p>
            </div>
            
            <div class="field">
              <p class="control">
                <input 
                class="input"
                type="text"
                placeholder="Plano de Saúde"
                >
              </p>
            </div>
          </div>
        </div>
        </form>
      </section>
      <footer class="modal-card-foot">
        <div class="field is-grouped is-grouped-right">
          <button class="button is-danger" :disabled="true">Confirmar Ausência</button>
          <button class="button is-danger" :disabled="true">Apagar Consulta</button>
          <button class="button is-info" :disabled="true">Confirmar Presença</button>
          <button class="button is-info" @click.prevent="salvarConsulta">Salvar Consulta</button>
        </div>
      </footer>
    </div>
  </form>
</template>
<script>
export default {
  name: 'ControleConsulta',
  props: ['dt_inicio', 'dt_fim', 'livre', 'local', 'profissional'],
  methods: {
    salvarConsulta () {
      console.log('Salvar NOVA consulta')
    }
  }
}
</script>

