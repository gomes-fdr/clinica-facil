<template>
<div>
  <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Descrição</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': true}"
             type="text"
            >
          </p>
          <p v-show="true" class="help is-danger">xxx</p>
        </div>
        <b-field class="file">
            <b-upload v-model="file">
                <a class="button is-info">
                    Arquivo
                </a>
            </b-upload>
            <span class="file-name" v-if="file">
                {{ file.name }}
            </span>
        </b-field>
      </div>
    </div>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <a class="button" @click.prevent="pesquisarPlano">Salvar</a>
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
    <button class="button field is-info" @click="checkedRows = []"
      :disabled="!checkedRows.length">
      Visualizar
    </button>
  </div>
</div>
</template>
<script>
import auth from '../../auth'

export default {
  name: 'Documentos',
  beforeCreate () {
    // carregaInfo () {
    console.log('Carregando infos...')
    // }
  },
  data () {
    return {
      form: {
        dt_validade: ''
      },
      data: [
          {'descricao': 'Documento de teste', 'dt_recebimento': '12/12/2019', 'responsavel': 'Fabiano Gomes'}
      ],
      columns: [
        {
          field: 'descricao',
          label: 'Descrição'
        },
        {
          field: 'dt_recebimento',
          label: 'Data da Gravação'
        },
        {
          field: 'responsavel',
          label: 'Responsavel'
        }
      ],
      checkedRows: [],
      file: null
    }
  },
  methods: {
    pesquisarPlano () {
      console.log('Consulta planos de saude')
      console.log()
      if (auth.isValidJwt(auth.getToken())) {
        console.log('token valido')
      } else {
        console.log('token INVALIDO')
      }
    }
  }
}
</script>

