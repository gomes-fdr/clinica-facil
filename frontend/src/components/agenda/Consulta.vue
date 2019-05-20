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
                <i class="fas fa-question"></i>
              </a>
            </div>
          </div>
          <p v-show="validation.hasError('formData.nomePaciente')" class="help is-danger">{{ validation.firstError('formData.nomePaciente') }}</p>
        </div>
        <b-field 
         v-if="formControl.radio == 'Especialidade'"
         :type="{'is-danger': validation.hasError('formData.especialidade') }"
         :message= "validation.firstError('formData.especialidade')"
         >
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
        </b-field>
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
              <a class="button" :disabled="formControl.isProfissionalDisabled" @click.prevent="pesquisarNome">
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
        <a class="button is-info" :disabled="false" @click.prevent="showCalendarioConsultas">Consultas Marcadas</a>
      </p>
      <p class="control">
        <a class="button is-info" @click.prevent="showCalendarioHorarios">Horários Vagos</a>
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
      :paciente="paciente"
      :modo="modo"
    >
    </controle-consulta>
  </b-modal>

  <b-modal :active.sync="modal.profissional.isActive">
    <b-table 
    :data="table.data"
    :loading="table.isLoading"
    :columns="table.columns"
    :selected.sync="table.selected"
    @dblclick="copiaProfissional"
    >
    
    </b-table>

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
        },
        profissional: {
          isActive: false
        }
      },
      table: {
        isLoading: false,
        data: [],
        columns: [
          {
            field: 'nome',
            label: 'Nome'
          },
          {
            field: 'cpf',
            label: 'CPF'
          }
        ],
        selected: null
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
        especialidade: '',
        profissional_id: ''
      },
      events: [],
      event: {
        date: null,
        startTime: '',
        endTime: '',
        name: null,
        horario_id: null,
        profissional_id: null
      },
      paciente: {
        id: null,
        nome: null,
        ps: {
          id: 1,
          descricao: null
        }
      },
      modo: ''
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
    'formData.especialidade': function (value) {
      if (this.formControl.radio === 'Especialidade') {
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

      // let profissional_id = this.$session.get('profissional_id')
      let profissional = this.$session.get('nome')
      let perfil = this.$session.get('perfil')

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
    },
    copiaProfissional () {
      console.log('Copia Profissional')
      if (!this.table.selected.nome) {
        return
      }
      this.$http
      .get(`${process.env.API_URL}profissional/nome-completo/${this.table.selected.nome}`)
      .then(response => {
        this.formData.profissional_id = response.data.id
        this.formData.nomeProfissional = response.data.nome
        // this.showCalendarioHorarios()
      })
      .catch(error => {
        // console.log(error)
        this.$toast.open({
          message:
            'NENHUM PROFISSIONAL encontrado.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
      .finally(() => {
        this.table.isLoading = false
      })
      this.modal.profissional.isActive = false
    },
    showCalendarioHorarios () {
      let selecao = ''
      let profissionalID = ''
      let especialidadeID = ''
      let url = ''
      this.events = []

      if ((this.formControl.radio === 'TodosProfissionais') || (this.formControl.radio === 'Profissional')) {
        selecao = 'profissional'
        if (this.formControl.radio === 'TodosProfissionais') {
          profissionalID = '*'
        } else if (this.formControl.radio === 'Profissional') {
          if ((this.$session.get('perfil') === 'Administracao') || (this.$session.get('perfil') === 'Recepcao')) {
            profissionalID = this.formData.profissional_id
          } else {
            profissionalID = this.$session.get('profissional_id')
          }
        }
        url = `agenda/horario/profissional?selecao=${selecao}&profissional_id=${profissionalID}&dt_inicio=${this.formData.dt_inicio}&dt_fim=${this.formData.dt_fim}&livre=true`
      } else if (this.formControl.radio === 'Especialidade') {
        selecao = 'especialidade'
        especialidadeID = this.formData.especialidade
        url = `agenda/horario/profissional?selecao=${selecao}&especialdade_id=${especialidadeID}&dt_inicio=${this.formData.dt_inicio}&dt_fim=${this.formData.dt_fim}&livre=true`
      }

      this.$validate()
      .then(response => {
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
              this.modo = null
              this.paciente.nome = ''
              this.paciente.id = ''

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
    showCalendarioConsultas () {
      let url = ''
      let profissionalID = ''
      this.events = []

      if ((this.$session.get('perfil') === 'Administracao') || (this.$session.get('perfil') === 'Recepcao')) {
        profissionalID = this.formData.profissional_id
      } else {
        profissionalID = this.$session.get('profissional_id')
      }

      switch (this.formControl.radio) {
        case 'Especialidade':
          console.log('Consultas Marcadas por Especialidade')
          url = `agenda/consulta?selecao=especialidade&especialidade_id=${this.formData.especialidade}&dt_ini=${this.formData.dt_inicio}&dt_fim=${this.formData.dt_fim}`
          break
        case 'TodosProfissionais':
          console.log('Consultas Marcadas Todos os profissionais')
          url = `agenda/consulta?selecao=t_profissional&dt_ini=${this.formData.dt_inicio}&dt_fim=${this.formData.dt_fim}`
          break
        case 'Profissional':
          console.log('Consultas Marcadas por Profissional')
          url = `agenda/consulta?selecao=profissional&profissional_id=${profissionalID}&dt_ini=${this.formData.dt_inicio}&dt_fim=${this.formData.dt_fim}`
          break
        default:
          return
      }
      this.$validate()
      .then(response => {
        if (response) {
          console.log('Calendario de Consultas')
          this.$http
          .get(`${process.env.API_URL}${url}`)
          .then(response => {
            let data = response.data
            console.log(data)
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
              event.id = e.id
              event.date = moment(e.horario.dt_dia.split('T')[0], 'YYYY-MM-DD').toDate()
              event.startTime = e.horario.hora_ini
              event.endTime = e.horario.hora_fim
              event.name = e.horario.profissional.nome
              event.profissional_id = e.horario.profissional.id
              // event.horario_id = e.id
              this.modo = 'consulta'
              this.paciente.nome = e.paciente.nome
              this.paciente.ps.descricao = e.plano_saude_paciente.ps.descricao
              this.events.push(event)
              // TODO: ALTERAR O cONSULTAsCHEMA PARA ACESSAR OS DADOS DE HORARIO, PARA ADICIONAR EM EVENTO
            })
            this.modal.calendario.isActive = true
          })
          .catch(error => {
            if (error) {
              this.$toast.open({
                message:
                  'NENHUMA CONSULTA encontrada',
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
    pesquisarNome () {
      console.log('Pesquisa PROFISSIONAL por nome')
      if (!this.formData.nomeProfissional.length) {
        return
      }
      this.table.isLoading = true
      this.$http
      .get(`${process.env.API_URL}profissional/nome/${this.formData.nomeProfissional}`)
      .then(response => {
        this.table.data = response.data
        this.modal.profissional.isActive = true
      })
      .catch(error => {
        this.$toast.open({
          message:
            'NENHUM PROFISSIONAL encontrado com esse nome.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
      .finally(() => {
        this.table.isLoading = false
      })
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
