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
            >
          </p>
            <div class="control">
              <a class="button is-right" >
                <i class="fas fa-search"></i>
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
</div>
</template>
<script>
export default {
  name: 'Convenios',
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
    }
  }
}
</script>

