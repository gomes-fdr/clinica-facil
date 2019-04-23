<template>
<div>
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
             :class="{'is-danger': true}"
             type="text"
             placeholder="Plano de Saude"
             v-model="form.ps"
            >
          </p>
            <div class="control">
              <a class="button" :disabled="modal.isAddPSActive" @click.prevent="addPS">
                <i class="fas fa-plus"></i>
              </a>
            </div>
            <div class="control">
              <a class="button" >
                <i class="fas fa-search" @click.prevent="pesquisarPlano"></i>
              </a>
            </div>
        </div>
          <p v-show="true" class="help is-danger">xxx</p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': true}"
             type="text"
             placeholder="Numero Carteira"
            >
          </p>
          <p v-show="true" class="help is-danger">xxx</p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': true}"
             type="text"
             placeholder="Data Validade"
             v-mask="'##/##/####'"
             v-model="form.dt_validade"
            >
          </p>
          <p v-show="true" class="help is-danger">xxx</p>
        </div>
      </div>
    </div>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <a class="button" @click.prevent="pesquisarPlano">Novo</a>
      </p>
    </div>
  </form>

  <b-table 
  :data="data"
  :columns="columns"
  :checked-rows.sync="checkedRows"
  checkable
  >
  </b-table>
  <div class="field is-grouped is-grouped-right">
    <button class="button field is-danger" @click="checkedRows = []"
      :disabled="!checkedRows.length">
      <i class="fas fa-times"></i>
      <span>Apagar</span>
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

const HTTP = axios.create({
  baseURL: API_URL,
  headers: { Authorization: `Bearer: ${localStorage.getItem('token')}` }
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
        dt_validade: '',
        ps: ''
      },
      data: [
        {'plano_saude': 'Particular', 'numero_carteira': '', 'data_validade': '12/12/2008'},
        {'plano_saude': 'Unimed', 'numero_carteira': '4567', 'data_validade': '12/12/2008'}
      ],
      columns: [
        {
          field: 'plano_saude',
          label: 'Plano de Saúde'
        },
        {
          field: 'numero_carteira',
          label: 'Numero da Carteira'
        },
        {
          field: 'data_validade',
          label: 'Data de Validade'
        }
      ],
      checkedRows: []
    }
  },
  methods: {
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
    },
    addPS () {
      console.log('Adiciona plano de saude novo')

      let vm = this
      this.modal.isAddPSActive = true

      HTTP
      .post(`${API_URL}ps/${vm.form.ps}`)
      .then(function (response) {
        console.log(response)
        // vm.modal.data = response.data
      })
      .catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

