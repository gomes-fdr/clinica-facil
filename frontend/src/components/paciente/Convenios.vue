<template>
<div>
  <h4 class="title is-4 has-text-black has-text-centered">{{form.nome}}</h4>
  <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Identificação</label>
      </div>
      <div class="field-body">
        <div class="field">
        <div class="field has-addons">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.ps.descricao') }"
             type="text"
             placeholder="Plano de Saude"
             v-model="form.ps.descricao"
             :readonly="modal.isAddPSActive"
            >
          </p>
            <div class="control">
              <a class="button" :disabled="modal.isAddPSActive" @click.prevent="addPS">
                <i class="fas fa-plus"></i>
              </a>
            </div>
            <div class="control">
              <a class="button" >
                <i class="fas fa-question" @click.prevent="pesquisarPlano"></i>
              </a>
            </div>
        </div>
          <p v-show="validation.hasError('form.ps.descricao')" class="help is-danger">{{ validation.firstError('form.ps.descricao') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.no_carteira') }"
             type="text"
             placeholder="Numero Carteira"
             v-model="form.no_carteira"
            >
          </p>
          <p v-show="validation.hasError('form.no_carteira')" class="help is-danger">{{ validation.firstError('form.no_carteira') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.dt_validade') }"
             type="text"
             placeholder="Data Validade"
             v-mask="'##/##/####'"
             v-model="form.dt_validade"
            >
          </p>
          <p v-show="validation.hasError('form.dt_validade')" class="help is-danger">{{ validation.firstError('form.dt_validade') }}</p>
        </div>
      </div>
    </div>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <a class="button is-info" @click.prevent="gravaPSPaciente">Adicionar Convênio</a>
      </p>
    </div>
  </form>

  <b-table 
  :data="table.data"
  :columns="table.columns"
  :checked-rows.sync="table.checkedRows"
  checkable
  >
  </b-table>
  <div class="field is-grouped is-grouped-right">
    <button 
     class="button field is-danger" @click.prevent="deletePS"
     :disabled="!table.checkedRows.length"
    >
     <i class="fas fa-times"></i>
     Apagar
    </button>
  </div>
  <b-modal :active.sync="modal.isImageModalActive">
    <b-table 
    :data="modal.data"
    :loading="modal.isLoading"
    :columns="modal.columns"
    :selected.sync="modal.selected"
    @dblclick="copiaPS"
    >
    
    </b-table>

  </b-modal>
</div>
</template>
<script>
import { API_URL, eBus } from '../../main'
import axios from 'axios'
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
  name: 'Convenios',
  beforeCreate () {
    // carregaInfo () {
    console.log('Carregando infos...')
    // }
  },
  data () {
    return {
      modal: {
        data: [],
        columns: [
          {
            field: 'descricao',
            label: 'Descrição'
          }
        ],
        isLoading: false,
        selected: null,
        isImageModalActive: false,
        isAddPSActive: true
      },
      form: {
        ps: {
          id: '',
          descricao: ''
        },
        no_carteira: '',
        dt_validade: '',
        paciente_id: '',
        nome: ''
      },
      table: {
        data: [],
        columns: [
          {
            field: 'ps',
            label: 'Plano de Saúde'
          },
          {
            field: 'no_carteira',
            label: 'Numero da Carteira'
          },
          {
            field: 'dt_validade',
            label: 'Data de Validade'
          }
        ],
        checkedRows: []
      }
    }
  },
  validators: {
    'form.ps.descricao': function (value) {
      return Validator.value(value).required()
    },
    'form.no_carteira': function (value) {
      return Validator.value(value).required()
    },
    'form.dt_validade': function (value) {
      return Validator.value(value).required()
    }
  },
  mounted () {
    let vm = this
    eBus.$on('PACIENTE_ID', function (paciente) {
      if (!paciente) return
      vm.form.paciente_id = paciente.id
      vm.form.nome = paciente.nome
      vm.getPSPaciente(paciente.id)
    })
  },
  methods: {
    getPSPaciente (pacienteID) {
      console.log('Busca planos de saude de um paciente')
      if (!this.form.paciente_id) return
      let vm = this

      HTTP
      .get(`${API_URL}ps-paciente/${pacienteID}`, {})
      .then(function (response) {
        // console.log(response)
        let data = response.data
        let p = {}
        let tabData = []
        for (p in data) {
          tabData.push({
            ps: data[p].ps.descricao,
            dt_validade: moment.utc(data[p].dt_validade).format('DD/MM/YYYY'),
            no_carteira: data[p].no_carteira,
            id: data[p].id
          })
        }
        vm.table.data = tabData
      })
      .catch(function (error) {
        // console.log(error)
        vm.table.data = []
      })
    },
    pesquisarPlano () {
      console.log('Consulta planos de saude')

      let vm = this
      this.modal.isImageModalActive = true
      this.modal.isAddPSActive = false

      HTTP
      .get(`${API_URL}ps`, {})
      .then(function (response) {
        // console.log(response)
        vm.modal.data = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    copiaPS () {
      console.log('Copia planos de saude')
      this.modal.isImageModalActive = false
      this.modal.isAddPSActive = true
      this.form.ps = this.modal.selected
    },
    addPS () {
      this.modal.isAddPSActive = true
      if (!this.form.ps.descricao) return
      console.log('Adiciona plano de saude novo')

      let vm = this

      HTTP
      .post(`${API_URL}ps/${vm.form.ps.descricao}`)
      .then(function (response) {
        // console.log(response)
        vm.reset()
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    gravaPSPaciente () {
      console.log('Grava PS para paciente')
      let vm = this
      let data = {...this.form}
      let dtTmp = moment.utc(data.dt_validade, 'DD/MM/YYYY')
      data.dt_validade = dtTmp

      this.$validate()
      .then(function (response) {
        if (response) {
          // console.log(data)
          HTTP
          .post(`${API_URL}ps-paciente`, data)
          .then(function (response) {
            // console.log(response)
            vm.reset()
            vm.getPSPaciente(vm.form.paciente_id)
          })
          .catch(function (error) {
            console.log(error)
          })
        }
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    reset () {
      this.form.ps.descricao = null
      this.form.ps.id = null
      this.form.dt_validade = null
      this.form.no_carteira = null
      this.validation.reset()
    },
    deletePS () {
      console.log('Apagar PS paciente')
      // console.log(this.table.checkedRows)
      let vm = this

      // Fazer um laço no vetor de linhas da tabela
      let p = {}
      for (p in this.table.checkedRows) {
        HTTP
        .get(`${API_URL}ps-paciente/delete/${vm.table.checkedRows[p].id}`, {})
        .then(function (response) {
          // console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
      }
      this.getPSPaciente(this.form.paciente_id)
    }
  }
}
</script>

