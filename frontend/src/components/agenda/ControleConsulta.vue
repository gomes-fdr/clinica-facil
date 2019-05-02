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
              v-model="form.convenios"
              >
                <option
                v-for="c in apiConvenios"
                :value="c.descricao"
                :key="c.id"
                >
                {{ c.descricao }}
                </option>
              </b-select>
              <p v-show="validation.hasError('form.convenios')" class="help is-danger">{{ validation.firstError('form.convenios') }}</p>
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
import axios from 'axios'
import { API_URL } from '../../main'
import SimpleVueValidation from 'simple-vue-validator'

var moment = require('moment')

const HTTP = axios.create({
  baseURL: API_URL,
  headers: { Authorization: `Bearer: ${localStorage.getItem('token')}` }
})
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
        paciente: {
          id: '',
          nome: ''
        },
        convenios: []
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
    'form.convenios': function (value) {
      return Validator.value(value).required()
    }
  },
  mounted () {
    this.initApp()
  },
  methods: {
    initApp () {
      this.date = `${moment.utc(this.event.date).format('dddd, DD MMMM YYYY')} das ${this.event.startTime} as ${this.event.endTime}`
    },
    salvarConsulta () {
      console.log('Salvar NOVA consulta')

      // TODO: SALVAR CONSULTA NO BANCO
      // TODO: Enviar SMS para o paciente, se o celular estiver preenchido

      this.$validate()
      .then(response => {})
      .catch(error => {})
    },
    pesquisaPaciente () {
      console.log('Pesquisa paciente')
      if (!this.form.paciente.nome.length) {
        return
      }

      let vm = this
      HTTP
        .get(`${API_URL}paciente/nome/${vm.form.paciente.nome}`, {
        })
      .then(function (response) {
        // console.log(response)
        if (response) {
          vm.modal.data = response.data
          vm.modal.isActive = true
        }
      })
      .catch(function (error) {
        // console.log(error)
        vm.$toast.open({
          message:
            'NENHUM PACIENTE encontrado.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
      .finally(function () {
        vm.modal.isLoading = false
      })
    },
    copiaPaciente () {
      console.log('Copia paciente')
      let vm = this
      HTTP
      .get(`${API_URL}paciente/nome-completo/${vm.modal.selected.nome}`)
      .then(function (response) {
        // console.log(response)
        let paciente = response.data
        // let t = moment.utc(tmp.dt_nascimento).format('DD/MM/YYYY')
        // tmp.dt_nascimento = t
        // console.log(tmp)
        // vm.form = tmp
        // vm.bNovo = true
        // vm.bAtualizar = false
        // let data = {
        //   id: vm.form.id,
        //   nome: vm.form.nome,
        //   dt_nascimento: vm.form.dt_nascimento
        // }
        // console.log(paciente)
        vm.form.paciente.id = paciente.id
        vm.form.paciente.nome = paciente.nome
        vm.getPSPaciente(vm.form.paciente.id)
      })
      .catch(function (error) {
        console.log(error)
      })
      .finally(function () {
        vm.modal.isLoading = false
      })
      this.modal.isActive = false
    },
    getPSPaciente (pacienteID) {
      console.log('Busca planos de saude de um paciente')
      let vm = this

      HTTP
      .get(`${API_URL}ps-paciente/${pacienteID}`, {})
      .then(function (response) {
        // console.log(response.data)
        let convenios = response.data

        convenios.forEach(c => {
          let convenio = {
            id: '',
            descricao: ''
          }
          convenio.id = c.id
          convenio.descricao = c.ps.descricao
          vm.apiConvenios.push(convenio)
        })
      })
      .catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

