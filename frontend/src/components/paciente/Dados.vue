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
             :class="{'is-danger': validation.hasError('form.nome') }"
             type="text"
             placeholder="Nome"
             v-model="form.nome"
            >
          </p>
            <div class="control">
              <a class="button is-right" @click.prevent="pesquisarNome">
                <i class="fas fa-search"></i>
              </a>
            </div>
        </div>
          <p v-show="validation.hasError('form.nome')" class="help is-danger">{{ validation.firstError('form.nome') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.email') }"
             type="text"
             placeholder="Email"
             v-model="form.email"
            >
          </p>
          <p v-show="validation.hasError('form.email')" class="help is-danger">{{ validation.firstError('form.email') }}</p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal"></div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input 
             class="input"
             :class="{'is-danger': validation.hasError('form.dt_nascimento') }"
             type="text"
             placeholder="Data de Nascimento"
             v-model="form.dt_nascimento"
             v-mask="'##/##/####'"
            >
          </p>
          <p v-show="validation.hasError('form.dt_nascimento')" class="help is-danger">{{ validation.firstError('form.dt_nascimento') }}</p>
        </div>
        <div class="field">
        <div class="field has-addons">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.cpf') }"
             type="text"
             placeholder="CPF"
             v-model="form.cpf"
             v-mask="'###########'"
            >
          </p>
          <div class="control">
            <a class="button  is-right" @click.prevent="pesquisarCPF">
              <i class="fas fa-search"></i>
            </a>
          </div>
        </div>
          <p v-show="validation.hasError('form.cpf')" class="help is-danger">{{ validation.firstError('form.cpf') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.rg') }"
             type="text"
             placeholder="Identidade"
             v-model="form.rg"
             v-mask="'##########'"
            >
          </p>
          <p v-show="validation.hasError('form.rg')" class="help is-danger">{{ validation.firstError('form.rg') }}</p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal"></div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.filiacao')}"
             type="text"
             placeholder="Filiação"
             v-model="form.filiacao"
            >
          </p>
          <p v-show="validation.hasError('form.filiacao') " class="help is-danger">{{ validation.firstError('form.filiacao') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             type="text"
             placeholder="Profissão"
             v-model="form.profissao"
            >
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.responsavel')}"
             type="text"
             placeholder="Responsável"
             v-model="form.responsavel"
             :disabled="isChild"
            >
          </p>
          <p v-show="validation.hasError('form.responsavel') " class="help is-danger">{{ validation.firstError('form.responsavel') }}</p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Telefones</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             type="text"
             placeholder="Telefone Celular"
             v-model="form.t_celular"
             v-mask="'###########'"
            >
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             type="text"
             placeholder="Telefone Fixo"
             v-model="form.t_fixo"
             v-mask="'##########'"
            >
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.t_responsavel')}"
             type="text"
             placeholder="Telefone Responsável"
             v-model="form.t_responsavel"
             v-mask="'###########'"
             :disabled="isChild"
            >
          </p>
          <p v-show="validation.hasError('form.t_responsavel') " class="help is-danger">{{ validation.firstError('form.t_responsavel') }}</p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Endereço</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.rua')}"
             type="text"
             placeholder="Rua"
             v-model="form.rua"
            >
          </p>
          <p v-show="validation.hasError('form.rua') " class="help is-danger">{{ validation.firstError('form.rua') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.numero')}"
             type="text"
             placeholder="Numero"
             v-model="form.numero"
            >
          </p>
          <p v-show="validation.hasError('form.numero') " class="help is-danger">{{ validation.firstError('form.numero') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input 
            class="input"
            type="text" placeholder="Complemento"
            v-model="form.complemento"
            >
          </p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal"></div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input 
            class="input"
            :class="{'is-danger': validation.hasError('form.cidade')}"
            type="text"
            placeholder="Cidade"
            v-model="form.cidade"
            >
          </p>
          <p v-show="validation.hasError('form.cidade') " class="help is-danger">{{ validation.firstError('form.cidade') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input 
             class="input"
             :class="{'is-danger': validation.hasError('form.estado')}"
             type="text"
             placeholder="Estado"
             v-model="form.estado"
            >
          </p>
          <p v-show="validation.hasError('form.estado') " class="help is-danger">{{ validation.firstError('form.estado') }}</p>
        </div>
        <div class="field">
        <div class="field has-addons">
          <p class="control is-expanded has-icons-right">
            <input class="input"
             type="text"
              placeholder="CEP"
              v-model="form.cep"
              v-mask="'########'"
            >
          </p>
          <div class="control">
            <a class="button  is-right" @click.prevent="pesquisarCEP">
              <i class="fas fa-search"></i>
            </a>
          </div>
        </div>
        </div>
      </div>
    </div>

     <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Observações</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             type="text"
             placeholder="Observações do paciente"
             v-model="form.observacoes"
            >
          </p>
        </div>
      </div>
    </div>

    <div class="field is-grouped is-grouped-right">
      <div class="control is-grouped-right">
        <b-switch type="is-info" v-model="form.envioSMS">Envio de SMS?</b-switch>
        <b-switch type="is-info" v-model="form.adultoInapto">Adulto com Responsável?</b-switch>
      </div>
    </div>
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button type="reset" class="button" @click.prevent="reset">Limpar</button>
      </p>
      <p class="control">
        <a class="button" :disabled="bNovo" @click.prevent="novoPaciente">Novo</a>
      </p>
      <p class="control">
        <button class="button" :disabled="bAtualizar" @click.prevent="atualizarPaciente">Atualizar</button>
      </p>
    </div>
  </form>
  <b-modal :active.sync="isImageModalActive">
    <b-table 
    :data="tabPaciente.data"
    :loading="tabPaciente.isLoading"
    :columns="tabPaciente.columns"
    :selected.sync="tabPaciente.selected"
    @dblclick="copiaPaciente"
    >
    
    </b-table>

  </b-modal>
</div>
</template>

<script>
import SimpleVueValidation from 'simple-vue-validator'
import auth from '../../auth'
import { eBus } from '../../main'
import axios from 'axios'
import _ from 'lodash'

var moment = require('moment')

const HTTP = axios.create({
  baseURL: process.env.API_URL,
  headers: { Authorization: `Bearer: ${localStorage.getItem('token')}` }
})

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório',
    email: 'Formato de e-mail inválido',
    length: 'Tamanho do campo inválido'
  }
})

export default {
  name: 'Dados',
  data () {
    return {
      isImageModalActive: false,
      tabPaciente: {
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
      form: {
        nome: '',
        email: '',
        dt_nascimento: '',
        rg: '',
        cpf: '',
        filiacao: '',
        profissao: '',
        responsavel: '',
        t_celular: '',
        t_fixo: '',
        t_responsavel: '',
        cep: '',
        rua: '',
        numero: '',
        complemento: '',
        cidade: '',
        estado: '',
        observacoes: '',
        envioSMS: false,
        adultoInapto: false
      },
      isFetching: false,
      bNovo: true,
      bAtualizar: true
    }
  },
  validators: {
    'form.nome': function (value) {
      return Validator.value(value).required()
    },
    'form.email': function (value) {
      return Validator.value(value).email()
    },
    'form.dt_nascimento': function (value) {
      return Validator.value(value).required()
    },
    'form.rg': function (value) {
      return Validator.value(value).length(10)
    },
    'form.cpf': function (value) {
      return Validator.value(value)
        .required()
        .length(11)
    },
    'form.filiacao': function (value) {
      return Validator.value(value)
    },
    'form.responsavel': function (value) {
      if (this.form.adultoInapto) {
        return Validator.value(value).required()
      }
    },
    'form.t_responsavel': function (value) {
      if (this.form.adultoInapto) {
        return Validator.value(value).required()
      }
    },
    'form.cep': function (value) {
      return Validator.value(value).required()
    },
    'form.rua': function (value) {
      return Validator.value(value).required()
    },
    'form.numero': function (value) {
      return Validator.value(value).required()
    },
    'form.cidade': function (value) {
      return Validator.value(value).required()
    },
    'form.estado': function (value) {
      return Validator.value(value).required()
    }
  },
  methods: {
    copiaPaciente () {
      console.log('Copia Paciente')
      // this.form.cpf = `${this.tabPaciente.selected.cpf}`
      if (!this.tabPaciente.selected.nome) {
        return
      }
      let vm = this
      HTTP
      .get(`${process.env.API_URL}paciente/nome-completo/${vm.tabPaciente.selected.nome}`)
      .then(function (response) {
        // console.log(response)
        let tmp = response.data
        let t = moment.utc(tmp.dt_nascimento).format('DD/MM/YYYY')
        tmp.dt_nascimento = t
        // console.log(tmp)
        vm.form = tmp
        vm.bNovo = true
        vm.bAtualizar = false
        let data = {
          id: vm.form.id,
          nome: vm.form.nome,
          dt_nascimento: vm.form.dt_nascimento
        }
        eBus.$emit('PACIENTE_ID', data)
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
        vm.tabPaciente.isLoading = false
      })
      this.isImageModalActive = false
    },
    pesquisarCPF () {
      console.log('Pesquisar CPF')
      if (!this.form.cpf.length) {
        return
      }
      var vm = this
      var cpf = this.form.cpf
      cpf = cpf.replace('.', '')
      cpf = cpf.replace('.', '')
      cpf = cpf.replace('-', '')
      HTTP
        .get(`${process.env.API_URL}paciente/cpf/${cpf}`, {
        })
        .then(function (response) {
          if (response.data) {
            let tmp = response.data
            let t = moment.utc(tmp.dt_nascimento).format('DD/MM/YYYY')
            tmp.dt_nascimento = t
            // console.log(tmp)
            vm.form = tmp
            vm.bAtualizar = false
            vm.bNovo = true
          }
        })
        .catch(error => {
          // console.log(error.response.status)

          if (error.response.status === 440) {
            this.$toast.open({
              duration: 5000,
              message: 'SESSÃO expirou',
              type: 'is-danger',
              position: 'is-bottom'
            })
            setTimeout(function () {
              auth.logout()
            }, 5000)
          } else {
            this.$toast.open({
              duration: 5000,
              message: 'PACIENTE não encontrado',
              type: 'is-warning',
              position: 'is-bottom'
            })
          }
          vm.bNovo = false
          vm.bAtualizar = true
        })
        .finally(() => {
          vm.isFetching = false
        })
    },
    pesquisarCEP () {
      var vm = this
      if (!this.form.cep.length) {
        this.data = []
        console.log('Nada enviado...')
        return
      }
      var cep = this.form.cep
      cep = cep.replace('.', '')
      cep = cep.replace('-', '')

      const instance = axios

      instance
        .get(`https://viacep.com.br/ws/${cep}/json`)
        .then(function (response) {
          if (response.data) {
            // console.log(response.body);
            vm.form.rua = response.data.logradouro
            vm.form.cidade = response.data.localidade
            vm.form.estado = response.data.uf
          }
        })
        .catch(function (error) {
          vm.erroCep()
        })
    },
    erroCep () {
      this.$toast.open({
        duration: 5000,
        message: 'CEP não encontrado',
        type: 'is-warning',
        position: 'is-bottom'
      })
    },
    reset () {
      this.form.nome = ''
      this.form.email = ''
      this.form.dt_nascimento = ''
      this.form.rg = ''
      this.form.cpf = ''
      this.form.filiacao = ''
      this.form.profissao = ''
      this.form.responsavel = ''
      this.form.t_celular = ''
      this.form.t_fixo = ''
      this.form.t_reponsavel = ''
      this.form.cep = ''
      this.form.rua = ''
      this.form.numero = ''
      this.form.complemento = ''
      this.form.cidade = ''
      this.form.estado = ''
      this.form.observacoes = ''
      this.form.envioSMS = false
      this.form.adultoInapto = false
      this.isFetching = false
      this.data = []
      this.bNovo = true
      this.bAtualizar = true
      this.validation.reset()
    },
    pesquisarNome: _.debounce(function () {
      console.log('Pesquisar paciente')
      if (!this.form.nome.length) {
        return
      }
      let vm = this
      vm.tabPaciente.isLoading = true
      HTTP
        .get(`${process.env.API_URL}paciente/nome/${vm.form.nome}`, {
        })
      .then(function (response) {
        // console.log(response)
        vm.tabPaciente.data = response.data
        vm.isImageModalActive = true
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
        vm.tabPaciente.isLoading = false
      })
    }, 500),
    novoPaciente () {
      console.log('Novo Profissional')
      let vm = this
      let data = {}

      this.$validate()
      .then(function (response) {
        // console.log(response)
        if (response === true) {
          data = {...vm.form}
          delete data.id
          let dtTmp = moment(vm.form.dt_nascimento, 'DD/MM/YYYY')
          data.dt_nascimento = dtTmp
          // console.log(JSON.stringify(data))
          vm.$http
          .post(`${process.env.API_URL}paciente`, data)
          .then(function (response) {
            console.log(response)
            vm.$toast.open({
              message: 'SUCESSO! PACIENTE gravado.',
              type: 'is-success',
              position: 'is-bottom'
            })
          })
          .catch(function (error) {
            // console.log(error)
            vm.$toast.open({
              message:
                'FALHA ao inserir novo PACIENTE!',
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
        } else {
          vm.$toast.open({
            message:
              'FORMULÁRIO INCOMPLETO',
            type: 'is-danger',
            position: 'is-bottom'
          })
        }
      })
    },
    atualizarPaciente () {
      if (this.validaForm() === false) return
      console.log('Atualizar Paciente')
      let vm = this
      // let data = this.form

      let data = {...this.form} // clonar objeto sem referencias
      let dtTmp = moment.utc(data.dt_nascimento, 'DD/MM/YYYY')
      data.dt_nascimento = dtTmp

      // console.log(JSON.stringify(data))

      HTTP
      .post(`${process.env.API_URL}paciente/${this.form.cpf}`, data)
      .then(function (response) {
        // console.log(response)
        vm.$toast.open({
          message: 'SUCESSO! Dados atualizados.',
          type: 'is-success',
          position: 'is-bottom'
        })
      })
      .catch(function (error) {
        vm.$toast.open({
          message:
            'FALHA ao atualizar PACIENTE!',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
    },
    validaForm () {
      var vm = this
      // this.$bus.$emit('submit');
      this.$validate().then(function (success) {
        if (success) {
          // console.log('Validou, enviando...');
          // console.log(JSON.stringify(vm.form));
          vm.$toast.open({
            message: 'Formulário preenchido com sucesso!',
            type: 'is-success',
            position: 'is-bottom'
          })
          return true
        } else {
          vm.$toast.open({
            message:
              'Formulário inválido! Verifique o preenchimento dos campos',
            type: 'is-danger',
            position: 'is-bottom'
          })
        }
        return false
      })
    }
  },
  computed: {
    isChild () {
      let birthday = moment.utc(this.form.dt_nascimento, 'DD/MM/YYYY')
      if (birthday.isValid()) {
        let age = Math.abs(birthday.diff(moment(), 'years'))
        if (age >= 18) {
          return false || !this.form.adultoInapto
        } else {
          return false
        }
      }
    }
  }
}
</script>
