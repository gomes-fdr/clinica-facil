<template>
<div>
  <form>

    <section class="level">
      <div class="level-item has-text-centered">
        <div class="block">
            <b-radio v-model="formControl.radio"
                native-value="Profissional">
                Profissional
            </b-radio>
            <b-radio v-model="formControl.radio"
                native-value="Paciente">
                Paciente
            </b-radio>
            <b-radio v-model="formControl.radio" :disabled="formControl.isProfissionalDisabled"
                native-value="TodosProfissionais">
                Todos os profissionais
            </b-radio>
            <b-radio v-model="formControl.radio"
                native-value="TodosPacientes">
                Todos os pacientes
            </b-radio>
        </div>
      </div>
    </section>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Periodo</label>
      </div>
      
      <div class="field-body">
        <div class="field">
          <p class="control">
            <input 
             class="input"
             type="text"
             placeholder="Inicio"
             v-mask="'##/##/####'"
             v-model="formData.dt_inicio"
            >
          </p>
        </div>
        
        <div class="field">
          <p class="control">
            <input 
             class="input"
             type="text"
             placeholder="Fim"
             v-mask="'##/##/####'"
             v-model="formData.dt_fim"
            >
          </p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal" v-show="(formControl.radio == 'Paciente') || (formControl.radio == 'Profissional')">
        <label class="label">Horários</label>
      </div>
      <div class="field-body">
        
        <div class="field" v-if="formControl.radio == 'Paciente'">
          <div class="field has-addons">
            <p class="control is-expanded">
              <input
              class="input"
              type="text"
              placeholder="Paciente"
              >
            </p>
            <div class="control">
              <a class="button">
                <i class="fas fa-search"></i>
              </a>
            </div>
          </div>
        </div>
        <div class="field" v-if="formControl.radio == 'Profissional'">
          <div class="field has-addons">
            <p class="control is-expanded">
              <input
              class="input"
              type="text"
              placeholder="Profissional"
              :readonly="formControl.isProfissionalDisabled"
              v-model="formData.nomeProfissional"
              >
            </p>
            <div class="control">
              <a class="button" :disabled="formControl.isProfissionalDisabled">
                <i class="fas fa-search"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <a class="button is-info" @click.prevent="showCalendar">Mostar Agenda</a>
      </p>
    </div>

  </form>
  
  <b-modal :active.sync="modal.isActive">
    <vue-scheduler
      :events="formData.events"
      event-display="name"
      :disable-dialog="true"
    >
    </vue-scheduler>
  </b-modal>
</div>
</template>
<script>
var moment = require('moment')

export default {
  name: 'Consulta',
  data () {
    return {
      modal: {
        isActive: false
      },
      formControl: {
        radio: 'TodosProfissionais',
        isProfissionalDisabled: false
      },
      formData: {
        dt_inicio: '',
        dt_fim: '',
        events: [],
        nomeProfissional: ''
      }
    }
  },
  methods: {
    initApp () {
      let tmp = new Date()
      let t = moment.utc(tmp).format('DD/MM/YYYY')
      this.formData.dt_inicio = t
      this.formData.dt_fim = t

      // let profissional_id = localStorage.getItem('profissional_id')
      let profissional = localStorage.getItem('nome')
      let perfil = localStorage.getItem('perfil')

      switch (perfil) {
        case 'Psicologo':
        case 'Psiquiatra':
        case 'Nutricionista':
        case 'Fonoaudiologo':
        case 'Neurologista':
          this.formControl.radio = 'Profissional'
          this.formControl.isProfissionalDisabled = true
          this.formData.nomeProfissional = profissional
          break
        default:
          break
      }

      // TODO: Se profissional de atendimento(ex. psicologo preencher o form automático)
      // TODO: Se não, deixa selecionado 'Todos os profissionais'
      // localStorage.getItem('token')
    },
    showCalendar () {
      this.modal.isActive = true
    }
  },
  mounted () {
    this.initApp()
  }
}
</script>
