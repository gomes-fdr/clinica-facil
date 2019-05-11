<template>
<div>
  <form>
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Controle de Consulta</p>
      </header>
      <section class="modal-card-body">
        <p class=" has-text-black has-text-centered">Profissional: {{ event.name }}</p>
        <p class=" has-text-black has-text-centered">{{  date  }}</p>
        <br>
        <form>
          <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Paciente</label>
          </div>
          
          <div class="field-body">
            <div class="field">
              <div class="field has-addons">
                <p class="control is-expanded">
                  <input
                  class="input"
                  :class="{'is-danger': validation.hasError('form.paciente.nome') }"
                  type="text"
                  placeholder="Nome"
                  v-model="form.paciente.nome"
                  >
                </p>
                  <div class="control">
                    <a class="button is-right" @click.prevent="pesquisaPaciente">
                      <i class="fas fa-search"></i>
                    </a>
                  </div>
              </div>
              <p v-show="validation.hasError('form.paciente.nome')" class="help is-danger">{{ validation.firstError('form.paciente.nome') }}</p>
            </div>
            
            <div class="field">
              <b-select 
              placeholder="Convênio"
              expanded
              v-model="form.convenio"
              >
                <option
                v-for="c in apiConvenios"
                :value="c"
                :key="c.id"
                >
                {{ c.descricao }}
                </option>
              </b-select>
              <p v-show="validation.hasError('form.convenio')" class="help is-danger">{{ validation.firstError('form.convenio') }}</p>
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

  <b-modal :active.sync="modal.isActive">
    <b-table 
    :data="modal.data"
    :loading="modal.isLoading"
    :columns="modal.columns"
    :selected.sync="modal.selected"
    @dblclick="copiaPaciente"
    >
    </b-table>
  </b-modal>

</div>
</template>
<script>
import SimpleVueValidation from 'simple-vue-validator'

var moment = require('moment')

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório'
  }
})

export default {
  name: 'ControleConsulta',
  props: ['event'],
  data () {
    return {
      date: '',
      apiConvenios: [],
      form: {
        dataMarcacao: null,
        confirmacao_consulta_sms: false,
        compareceu: false,
        paciente: {
          id: '',
          nome: ''
        },
        quem_marcou_id: '',
        horario_id: '',
        convenio: []
      },
      modal: {
        isLoading: false,
        isActive: false,
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
    }
  },
  validators: {
    'form.paciente.nome': function (value) {
      return Validator.value(value).required()
    },
    'form.convenio': function (value) {
      return Validator.value(value).required()
    }
  },
  mounted () {
    this.initApp()
  },
  methods: {
    initApp () {
      this.date = `${moment.utc(this.event.date).format('dddd, DD MMMM YYYY')} das ${this.event.startTime} as ${this.event.endTime}`
      this.form.horario_id = this.event.horario_id
      this.form.quem_marcou_id = localStorage.getItem('profissional_id')
    },
    salvarConsulta () {
      console.log('Salvar NOVA consulta')

      // TODO: SALVAR CONSULTA NO BANCO
      // TODO: Enviar SMS para o paciente, se o celular estiver preenchido

      this.$validate()
      .then(response => {
        if (response) {
          let data = this.form
          data.dataMarcacao = new Date()
          this.$http
          .post(`${process.env.API_URL}agenda/consulta`, data)
          .then(response => {
            if (response) {
              this.$toast.open({
                message:
                  'CONSULTA salav com sucesso',
                type: 'is-success',
                position: 'is-bottom'
              })
              this.$parent.close()
            }
          })
          .catch(error => {
            // console.log(error)
            this.$toast.open({
              message:
                'FALHA ao gravar uma CONSULTA',
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
        }
      })
      .catch(error => {})
    },
    pesquisaPaciente () {
      console.log('Pesquisa paciente')
      if (!this.form.paciente.nome.length) {
        return
      }

      this.$http
      .get(`${process.env.API_URL}paciente/nome/${this.form.paciente.nome}`)
      .then(response => {
        // console.log(response)
        if (response) {
          this.modal.data = response.data
          this.modal.isActive = true
        }
      })
      .catch(error => {
        // console.log(error)
        this.$toast.open({
          message:
            'NENHUM PACIENTE encontrado.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
      .finally(() => {
        this.modal.isLoading = false
      })
    },
    copiaPaciente () {
      console.log('Copia paciente')
      this.$http
      .get(`${process.env.API_URL}paciente/nome-completo/${this.modal.selected.nome}`)
      .then(response => {
        // console.log(response)
        let paciente = response.data
        // console.log(paciente)
        this.form.paciente.id = paciente.id
        this.form.paciente.nome = paciente.nome
        this.getPSPaciente(this.form.paciente.id)
      })
      .catch(error => {
        console.log(error)
      })
      .finally(() => {
        this.modal.isLoading = false
      })
      this.modal.isActive = false
    },
    getPSPaciente (pacienteID) {
      console.log('Busca planos de saude de um paciente')
      this.$http
      .get(`${process.env.API_URL}ps-paciente/${pacienteID}`)
      .then(response => {
        console.log(response.data)
        let convenios = response.data

        convenios.forEach(c => {
          let convenio = {
            id: '',
            descricao: ''
          }
          convenio.id = c.id
          convenio.descricao = c.ps.descricao
          this.apiConvenios.push(convenio)
        })
      })
      .catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

