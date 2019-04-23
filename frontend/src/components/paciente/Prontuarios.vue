<template>
<div>
  <div class="columns">
    <div class="column">
       <b>Paciente:  <span>{{form.nome}}</span></b>
    </div>
    <div class="column">
       <b>Idade: <span>{{form.idade}}</span></b> anos
    </div>
    <div class="column">
      <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Atendimento</label>
          </div>
          <p class="control is-expanded">
            <input 
             class="input"
             :class="{'is-danger': validation.hasError('form.dt_atendimento') }"
             type="text"
             placeholder="dd/mm/aaaa"
             v-model="form.dt_atendimento"
             v-mask="'##/##/####'"
            >
          </p>
          <p v-show="validation.hasError('form.dt_atendimento')" class="help is-danger">{{ validation.firstError('form.dt_atendimento') }}</p>
        </div>
    </div>
  </div>
  <section>
    <textarea class="textarea" placeholder="Texto do prontuário" rows="10"></textarea>
  </section>
  <br>
  <div class="field is-grouped is-grouped-right">
    <p class="control">
      <button type="reset" class="button" @click.prevent="getProntuarioLegado">Visualizar Legado</button>
    </p>
    <p class="control">
      <a class="button" :disabled="bGravar" @click.prevent="visualizarHistorico(form.id)">Visualizar Histórico</a>
    </p>
    <p class="control">
      <button class="button" :disabled="submitted" @click.prevent="salavrEvolucao(form.id)">Salvar Evolução</button>
    </p>
  </div>

<!-- Modal com os dados de prontuário legado -->
  <section>
    <b-modal :active.sync="isCardModalActive" :width="800" scroll="keep">
      <div class="card">
        <div class="card-content">
          <div class="media">
            <div class="media-content">
                <p class="title is-4">John Smith</p>
                <p class="subtitle is-6">@johnsmith</p>
            </div>
          </div>

          <div class="content">
              {{form.prontuarioLegado}}
          </div>
        </div>
      </div>
    </b-modal>
  </section>

</div>
</template>
<script>
import SimpleVueValidation from 'simple-vue-validator'
import { API_URL, eBus } from '../../main'
import axios from 'axios'

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
  name: 'Prontuarios',
  data () {
    return {
      form: {
        id: '',
        nome: '',
        idade: '',
        dt_atendimento: '',
        prontuarioLegado: ''
      },
      isCardModalActive: false,
      submitted: true,
      bGravar: true
    }
  },
  validators: {
    'form.dt_atendimento': function (atendimento) {
      if (this.validation.isTouched('form.dt_atendimento')) {
        this.submitted = false
        return Validator.value(atendimento).required()
      }
    }
  },
  methods: {
    getProntuarioLegado () {
      if (!this.form.id) {
        console.log('ID de paciente em branco')
        return
      }
      console.log('Prontuário legado')
      let vm = this
      HTTP
        .get(`${API_URL}paciente/prontuario-legado/${vm.form.id}`, {
        })
        .then(function (response) {
          // console.log(response.data)
          vm.form.prontuarioLegado = response.data['conteudo']
          vm.isCardModalActive = true
        })
      .catch(function (error) {
        // console.log(error)
        vm.$toast.open({
          message:
            'NENHUM PRONTUÁRIO encontrado.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
      .finally(function () {
        vm.isImageModalActive = false
      })
    },
    salavrEvolucao (pacienteID) {
      if (!pacienteID) return
      console.log('Salvar evolução')
    },
    visualizarHistorico (pacienteID) {
      if (!pacienteID) return
      console.log('Visualizar histórico')
    }
  },
  mounted () {
    let vm = this
    eBus.$on('PACIENTE_ID', function (paciente) {
      if (!paciente) return
      let birthday = moment.utc(paciente.dt_nascimento, 'DD/MM/YYYY')
      let age = Math.abs(birthday.diff(moment(), 'years'))
      vm.form.id = paciente.id
      vm.form.nome = paciente.nome
      vm.form.idade = age
      vm.bGravar = false
    })
  }
}
</script>

