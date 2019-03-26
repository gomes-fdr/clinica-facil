<template>
<div>
  <div class="columns">
    <div class="column">
      Paciente:
    </div>
    <div class="column">
      Idade:
    </div>
    <div class="column">
      Data do Atendimento:
    </div>
    <div class="column">
      <div class="field">
          <p class="control is-expanded">
            <input 
             class="input"
             :class="{'is-danger': true }"
             type="text"
             placeholder="dd/mm/aaaa"
             v-model="form.dt_atendimento"
             v-mask="'##/##/####'"
            >
          </p>
          <p v-show="true" class="help is-danger">xxx</p>
        </div>
    </div>
  </div>
  <section>
    <textarea class="textarea" placeholder="10 lines of textarea" rows="10"></textarea>
  </section>
  <br>
  <div class="field is-grouped is-grouped-right">
    <p class="control">
      <button type="reset" class="button" @click="isCardModalActive = true">Visualizar Legado</button>
    </p>
    <p class="control">
      <a class="button" disabled>Visualizar Histórico</a>
    </p>
    <p class="control">
      <button class="button" disabled>Salvar Evolução</button>
    </p>
  </div>

<!-- Modal com os dados de prontuário legado -->
  <section>
    <b-modal :active.sync="isCardModalActive" :width="640" scroll="keep">
      <div class="card">
        <div class="card-content">
          <div class="media">
            <div class="media-content">
                <p class="title is-4">John Smith</p>
                <p class="subtitle is-6">@johnsmith</p>
            </div>
          </div>

          <div class="content">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
              Phasellus nec iaculis mauris. <a>@bulmaio</a>.
              <a>#css</a> <a>#responsive</a>
              <br>
              <small>11:09 PM - 1 Jan 2016</small>
          </div>
        </div>
      </div>
    </b-modal>
  </section>

</div>
</template>
<script>
export default {
  name: 'Prontuario',
  data () {
    return {
      form: {
        dt_atendimento: ''
      },
      isCardModalActive: false
    }
  }
}
</script>

