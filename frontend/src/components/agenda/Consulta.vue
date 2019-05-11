<template>
<div>
  <form>

    <section class="level">
      <div class="level-item has-text-centered">
        <div class="block">
            <b-radio v-model="formControl.radio" :disabled="formControl.isProfissionalDisabled"
                native-value="Especialidade">
                Por Especialidade
            </b-radio>
            <b-radio v-model="formControl.radio" :disabled="formControl.isProfissionalDisabled"
                native-value="TodosProfissionais">
                Todos os profissionais
            </b-radio>
            <b-radio v-model="formControl.radio"
                native-value="Profissional">
                Profissional
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
             :class="{'is-danger': validation.hasError('formData.dt_inicio') }"
             type="text"
             placeholder="Inicio"
             v-mask="'##/##/####'"
             v-model="formData.dt_inicio"
            >
          </p>
        <p v-show="validation.hasError('formData.dt_inicio')" class="help is-danger">{{ validation.firstError('formData.dt_inicio') }}</p>
        </div>
        
        <div class="field">
          <p class="control">
            <input 
             class="input"
             :class="{'is-danger': validation.hasError('formData.dt_fim') }"
             type="text"
             placeholder="Fim"
             v-mask="'##/##/####'"
             v-model="formData.dt_fim"
            >
          </p>
          <p v-show="validation.hasError('formData.dt_fim')" class="help is-danger">{{ validation.firstError('formData.dt_fim') }}</p>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal" v-show="(formControl.radio == 'Especialidade') || (formControl.radio == 'Profissional')">
        <label class="label">Horários</label>
      </div>
      <div class="field-body">
        
        <div class="field" v-if="formControl.radio == 'Paciente'">
          <div class="field has-addons">
            <p class="control is-expanded">
              <input
              class="input"
              :class="{'is-danger': validation.hasError('formData.nomePaciente') }"
              type="text"
              placeholder="Paciente"
              v-model="formData.nomePaciente"
              >
            </p>
            <div class="control">
              <a class="button">
                <i class="fas fa-search"></i>
              </a>
            </div>
          </div>
          <p v-show="validation.hasError('formData.nomePaciente')" class="help is-danger">{{ validation.firstError('formData.nomePaciente') }}</p>
        </div>
        <div class="field" v-if="formControl.radio == 'Especialidade'">
          <b-select 
          placeholder="Especialidade"
          expanded
          v-model="formData.especialidade"
          >
            <option
            v-for="e in apiEspecialidade"
            :value="e.id"
            :key="e.id"
            >
              {{e.descricao}}
            </option>
          </b-select>
        </div>
        <div class="field" v-if="formControl.radio == 'Profissional'">
          <div class="field has-addons">
            <p class="control is-expanded">
              <input
              class="input"
              :class="{'is-danger': validation.hasError('formData.nomeProfissional') }"
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
          <p v-show="validation.hasError('formData.nomeProfissional')" class="help is-danger">{{ validation.firstError('formData.nomeProfissional') }}</p>
        </div>
      </div>
    </div>
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <a class="button is-info" :disabled="false" @click.prevent="consultasMarcadas">Consultas Marcadas</a>
      </p>
      <p class="control">
        <a class="button is-info" @click.prevent="showCalendar">Horários Vagos</a>
      </p>
    </div>

  </form>
  
  <b-modal :active.sync="modal.calendario.isActive">
    <vue-scheduler
      :events="events"
      event-display="name"
      @event-clicked="eventClicked"
      :disable-dialog="true"
      :initialDate = "dataInicial"
    >
    </vue-scheduler>
  </b-modal>

  <b-modal :active.sync="modal.agenda.isActive">
    <controle-consulta
      :event="event"
    >
    </controle-consulta>
  </b-modal>
</div>
</template>

<script>
import SimpleVueValidation from 'simple-vue-validator'
import axios from 'axios'
import ControleConsulta from './ControleConsulta'

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório'
  }
})

var moment = require('moment')

export default {
  name: 'Consulta',
  components: {
    ControleConsulta
  },
  data () {
    return {
      apiEspecialidade: [],
      modal: {
        calendario: {
          isActive: false
        },
        agenda: {
          isActive: false
        }
      },
      formControl: {
        radio: 'Especialidade',
        isProfissionalDisabled: false
      },
      formData: {
        dt_inicio: '',
        dt_fim: '',
        nomeProfissional: '',
        nomePaciente: '',
        especialidade: ''
      },
      events: [],
      event: {
        date: null,
        startTime: '',
        endTime: '',
        name: null,
        horario_id: null,
        profissional_id: null
      }
    }
  },
  validators: {
    'formData.dt_inicio': function (value) {
      return Validator.value(value).required()
    },
    'formData.dt_fim': function (value) {
      return Validator.value(value).required()
    },
    'formData.nomeProfissional': function (value) {
      if (this.formControl.radio === 'Profissional') {
        return Validator.value(value).required()
      }
    },
    'formData.nomePaciente': function (value) {
      if (this.formControl.radio === 'Paciente') {
        return Validator.value(value).required()
      }
    }
  },
  methods: {
    initApp () {
      let tmp = new Date()
      let tmp2 = moment.utc(tmp, 'DD/MM/YYYY').add(1, 'days')
      this.formData.dt_inicio = moment.utc(tmp).format('DD/MM/YYYY')
      this.formData.dt_fim = moment.utc(tmp2).format('DD/MM/YYYY')

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
      let selecao = ''
      let profissionalID = ''
      let especialidadeID = ''
      let url = ''
      this.events = []

      if ((this.formControl.radio === 'TodosProfissionais') || (this.formControl.radio === 'Profissionais')) {
        selecao = 'profissional'
        if (this.formControl.radio === 'TodosProfissionais') profissionalID = '*'
        else if (this.formControl.radio === 'Profissionais') profissionalID = localStorage.getItem('profissional_id')
        url = `agenda/horario/profissional?selecao=${selecao}&profissional_id=${profissionalID}&dt_inicio=${this.formData.dt_inicio}&dt_fim=${this.formData.dt_fim}&livre=true`
      } if (this.formControl.radio === 'Especialidade') {
        selecao = 'especialidade'
        especialidadeID = this.formData.especialidade
        url = `agenda/horario/profissional?selecao=${selecao}&especialdade_id=${especialidadeID}&dt_inicio=${this.formData.dt_inicio}&dt_fim=${this.formData.dt_fim}&livre=true`
      }

      this.$validate()
      .then(function (response) {
        if (response) {
          console.log('Calendario de eventos')
          this.$http
          .get(`${process.env.API_URL}${url}`)
          .then(response => {
            let data = response.data
            data.forEach(e => {
              let event = {
                date: null,
                startTime: '',
                endTime: '',
                name: null,
                horario_id: null,
                profissional_id: null
              }
              // console.log('data do evento: ' + e.dt_dia.split('T')[0])
              // console.log(typeof e.dt_dia)
              event.date = moment(e.dt_dia.split('T')[0], 'YYYY-MM-DD').toDate()
              event.startTime = e.hora_ini
              event.endTime = e.hora_fim
              event.name = e.profissional.nome
              event.profissional_id = e.profissional.id
              event.horario_id = e.id
              this.events.push(event)
            })
            this.modal.calendario.isActive = true
          })
          .catch(error => {
            // console.log(error.response.status)
            // if (error.response.status === 404) {
            if (error) {
              this.$toast.open({
                message:
                  'NENHUM HORARIO encontrado',
                type: 'is-danger',
                position: 'is-bottom'
              })
            }
          })
        }
      })
      .catch(error => {
        console.log(error)
      })
    },
    consultasMarcadas () {
      console.log('Consultas Marcadas')
    },
    eventClicked (event) {
      // console.log(event)
      this.event = event
      this.modal.agenda.isActive = true
    },
    carregaEspecialidades () {
      console.log('Carregando as especialidades...')
      this.$http
      .get(`${process.env.API_URL}agenda/especialidades`)
      .then(response => {
        this.apiEspecialidade = response.data
      })
      .catch(error => {})
    },
    enviaSMS () {
      console.log('Envia SMS')

      const msg = {
        sendSmsRequest: {
          from: 'Fargos Sistemas',
          to: '5551995489581',
          schedule: '2019-05-09T20:49:00',
          msg: 'Sistema darmas sabe mandar SMS',
          callbackOption: 'NONE',
          id: '004',
          aggregateId: '49548',
          flashSms: false
        }
      }

      // msg.sendSmsRequest.schedule = moment.utc()

      let ZENVIA = axios.create({
        baseURL: 'https://api-rest.zenvia.com/services',
        auth: {
          username: 'fdrgomes.smsonline',
          password: 'O6m9MzWkQG'
        },
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'CrossDomain': true
        }
      })

      // console.log(JSON.stringify(msg))

      ZENVIA
      .post('/send-sms', msg)
      .then(response => {
        console.log(response.data)
      })
      .catch(error => {
        // console.log(error)
      })
    }
  },
  mounted () {
    this.initApp()
  },
  created () {
    this.carregaEspecialidades()
  },
  computed: {
    dataInicial () {
      let dtTmp = moment.utc(this.formData.dt_inicio, 'DD/MM/YYYY').toDate()
      return dtTmp
    }
  }
}
</script>
