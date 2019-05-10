<template>
<div>
  <p class=" has-text-black has-text-centered">Sala: {{formHorario.local.descricao}}</p>
  <p class=" has-text-black has-text-centered">Profissional: {{formHorario.profissional.nome}}</p>
  <form>

      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Horário</label>
        </div>
        <div class="field-body">
          <div class="field">
          <div class="field has-addons">
            <p class="control is-expanded">
              <input
              class="input"
              :class="{'is-danger': validation.hasError('formHorario.local.descricao') }"
              type="text"
              placeholder="Onde? (Sala)"
              v-model="formHorario.local.descricao"
              :readonly="modal.local.isAdd"
              >
            </p>
              <div class="control">
                <a class="button" :disabled="modal.local.isAdd">
                  <i class="fas fa-plus" @click.prevent="addSala" ></i>
                </a>
              </div>
              <div class="control">
                <a class="button" >
                  <i class="fas fa-question" @click.prevent="pequisaSala"></i>
                </a>
              </div>
          </div>
          <p v-show="validation.hasError('formHorario.local.descricao')" class="help is-danger">{{ validation.firstError('formHorario.local.descricao') }}</p>
          </div>
          <div class="field">
            <div class="field has-addons">
              <p class="control is-expanded">
                <input
                class="input"
                :class="{'is-danger': validation.hasError('formHorario.profissional.nome') }"
                type="text"
                placeholder="Quem? (Profissional)"
                v-model="formHorario.profissional.nome"
                >
              </p>
              <div class="control">
                <a class="button">
                  <i class="fas fa-search" @click.prevent="pesquisaProfissional"></i>
                </a>
              </div>
            </div>
            <p v-show="validation.hasError('formHorario.profissional.nome')" class="help is-danger">{{ validation.firstError('formHorario.profissional.nome') }}</p>
          </div>
          <div class="field">
            <div class="field has-addons">
              <p class="control is-expanded">
                <input
                class="input"
                :class="{'is-danger': validation.hasError('formHorario.duracao') }"
                type="text"
                placeholder="Duração (Minutos)"
                v-model="formHorario.duracao"
                >
              </p>
            </div>
            <p v-show="validation.hasError('formHorario.duracao')" class="help is-danger">{{ validation.firstError('formHorario.duracao') }}</p>
          </div>
        </div>
      </div>
      <hr>
        <div class="field is-grouped is-grouped-right">
          <p class="control">
            <a class="button is-info" :disabled="hasEvent" :key="componentKey" @click.prevent="salvarAgendas">Salvar Agenda</a>
          </p>
          <p class="control">
            <a class="button is-danger" :disabled="hasEvent" @click.prevent="apagarAgenda">Apagar Agenda</a>
          </p>
          <p class="control">
            <a class="button is-info" @click.prevent="eventCalendar">Montar Agenda</a>
          </p>
        </div>
  </form>

<b-modal :active.sync="modal.calendar.isActive">
    <vue-scheduler
      :events="events"
      :event-dialog-config="dialogConfig"
      event-display="name"
      @event-clicked="eventClicked"
      @time-clicked="timeClicked"
      :key="componentKey"
      :disable-dialog="true"
    >
    </vue-scheduler>
</b-modal>

<b-modal :active.sync="modal.local.isActive">
  <b-table 
    :data="modal.local.data"
    :loading="modal.local.isLoading"
    :columns="modal.local.columns"
    :selected.sync="modal.local.selected"
    @dblclick="copiaSala"
    >
    </b-table>
</b-modal>

<b-modal :active.sync="modal.profissional.isActive">
  <b-table 
  :data="modal.profissional.data"
  :loading="modal.profissional.isLoading"
  :columns="modal.profissional.columns"
  :selected.sync="modal.profissional.selected"
  @dblclick="copiaProfissional"
  >
  
  </b-table>

</b-modal>

 

</div>
</template>
<script>
import { remove } from 'lodash'
import SimpleVueValidation from 'simple-vue-validator'
import axios from 'axios'

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório',
    integer: 'Somente numeros',
    between: 'Valores entre 1 e 60'
  }
})

const HTTP = axios.create({
  baseURL: process.env.API_URL,
  headers: { Authorization: `Bearer: ${localStorage.getItem('token')}` }
})

export default {
  name: 'Horarios',
  validators: {
    'formHorario.local.descricao': function (value) {
      return Validator.value(value).required()
    },
    'formHorario.profissional.nome': function (value) {
      return Validator.value(value).required()
    },
    'formHorario.duracao': function (value) {
      return Validator.value(value).required()
      .integer()
      .between(1, 60)
    }
  },
  data () {
    return {
      espera: {
        isLoading: false
      },
      formHorario: {
        local: {
          descricao: ''
        },
        profissional: {
          nome: ''
        },
        duracao: ''
      },
      componentKey: 0,
      modal: {
        calendar: {
          isActive: false
        },
        local: {
          isActive: false,
          isLoading: false,
          isAdd: true,
          data: [],
          columns: [
            {
              field: 'descricao',
              label: 'Descricao'
            }
          ],
          selected: null
        },
        profissional: {
          isLoading: false,
          isActive: false,
          isAdd: true,
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
        }
      },
      modalNovoEvento: {
        isAddEventActive: false,
        form: {
          dt_inicio: null,
          dt_fim: null,
          livre: true,
          local: null,
          profissional: null
        }
      },
      dialogConfig: {
        title: 'Novo Horário',
        createButtonLabel: 'Adciona Horário',
        enableTimeInputs: true,
        fields: [
          {
            fields: [
              {
                name: 'hora',
                label: 'Hora',
                type: 'time'
              },
              {
                name: 'duracao',
                label: 'Duração'
              }
            ]
          },
          {
            name: 'repete',
            label: 'No. de vezes no dia',
            value: '1',
            required: true
          },
          {
            label: 'Consulta',
            fields: [
              {
                name: 'sala',
                label: 'Sala'
              },
              {
                name: 'profissional',
                label: 'Profissional'
              }
            ]
          }
        ]
      },
      events: [],
      bEnviarAgenda: true
    }
  },
  methods: {
    eventClicked (event) {
      console.log('Evento selecionado')
      remove(this.events, event)

      // Para forçar a renderização do calendário
      this.componentKey += 1
    },
    eventCreated (event) {
      console.log('Event created')
      console.log(event)
    },
    timeClicked (dateWithTime) {
      console.log('Time clicked')
      // console.log('Date: ' + dateWithTime.date)
      // console.log('Time: ' + dateWithTime.time)

      this.modalNovoEvento.form.profissional = 'Gudi Lack'

      let dtDia = dateWithTime.date
      let horaIni = `${dateWithTime.time}:00`
      let horaFim = null
      let livre = true
      let local = this.formHorario.local.id
      let profissional = this.formHorario.profissional
      let duracao = Number(this.formHorario.duracao)
      let event = null

      console.log(typeof duracao)

      if (duracao < 60) {
        horaFim = `${dateWithTime.time}:${duracao}`
      } else if (duracao === 60) {
        horaFim = `${dateWithTime.time + 1}:00`
      } else {
        return
      }
      if (dateWithTime.time === null) {
        console.log('O dia inteiro')
      } else {
        event = {
          date: dtDia,
          startTime: horaIni,
          endTime: horaFim,
          livre: livre,
          local_id: local,
          name: profissional.nome,
          profissional_id: profissional.id,
          duracao: duracao
        }
        this.events.push(event)
      }

      // this.modalNovoEvento.isAddEventActive = true

    },
    eventCalendar () {
      let vm = this
      this.$validate()
      .then(function (response) {
        if (response) {
          console.log('Calendario de eventos')
          vm.modal.calendar.isActive = true
        }
      })
      .catch(function (error) {})
    },
    forceRerender () {
      this.componentKey += 1
    },
    salvarAgenda (event) {
      console.log('Salva agenda no banco')
      // let data = event
      HTTP
      .post('agenda/horario', event)
      .then(function (response) {
        console.log(response)
        // vm.modal.local.data = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    salvarAgendas () {
      this.events.forEach((event) => {
        this.salvarAgenda(event)
      })
      this.apagarAgenda()
    },
    apagarAgenda () {
      console.log('Apaga agenda local')
      this.events = []
    },
    pequisaSala () {
      console.log('Pesquisa Sala')
      let vm = this
      this.modal.local.isActive = true
      this.modal.local.isAdd = false

      HTTP
      .get(`${process.env.API_URL}agenda/sala`, {})
      .then(function (response) {
        // console.log(response)
        vm.modal.local.data = response.data
      })
      .catch(function (error) {
        console.log(error.response)
      })

    },
    addSala () {
      if (!this.formHorario.local) return
      console.log('Adiciona sala')
      let vm = this

      HTTP
      .post(`${process.env.API_URL}agenda/sala/${vm.formHorario.local.descricao}`)
      .then(function (response) {
        // console.log(response)
        // vm.reset()
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    copiaSala () {
      console.log('Copia sala')
      this.modal.local.isActive = false
      this.modal.local.isAdd = true
      this.formHorario.local = this.modal.local.selected
    },
    pesquisaProfissional () {
      console.log('Pesquisa profissional')
      if (!this.formHorario.profissional) return
      let vm = this

      this.modal.profissional.isActive = true

      HTTP
      .get(`${process.env.API_URL}profissional/nome/${vm.formHorario.profissional.nome}`, {
      })
      .then(function (response) {
        // console.log(response)
        vm.modal.profissional.data = response.data
        // vm.isImageModalActive = true
      })
      .catch(function (error) {
        // console.log(error)
        vm.$toast.open({
          message:
            'NENHUM PROFISSIONAL encontrado com esse nome.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
    },
    copiaProfissional () {
      console.log('Copia profissional')
      if (!this.modal.profissional.selected) {
        return
      }
      this.formHorario.profissional = this.modal.profissional.selected
      this.modal.profissional.isActive = false
    }
  },
  computed: {
    hasEvent () {
      this.componentKey += 1
      if (this.events.length) {
        return false
      }
      return true
    }
  }
}
</script>

