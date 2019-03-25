<template>
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
             :class="{'is-danger': validation.hasError('form.endereco.rua')}"
             type="text"
             placeholder="Rua"
             v-model="form.rua"
            >
          </p>
          <p v-show="validation.hasError('form.endereco.rua') " class="help is-danger">{{ validation.firstError('form.endereco.rua') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('form.endereco.numero')}"
             type="text"
             placeholder="Numero"
             v-model="form.endereco.numero"
            >
          </p>
          <p v-show="validation.hasError('form.endereco.numero') " class="help is-danger">{{ validation.firstError('form.endereco.numero') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input" type="text" placeholder="Complemento">
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
            :class="{'is-danger': validation.hasError('form.endereco.cidade')}"
            type="text"
            placeholder="Cidade"
            v-model="form.endereco.cidade"
            >
          </p>
          <p v-show="validation.hasError('form.endereco.cidade') " class="help is-danger">{{ validation.firstError('form.endereco.cidade') }}</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input 
             class="input"
             :class="{'is-danger': validation.hasError('form.endereco.estado')}"
             type="text"
             placeholder="Estado"
             v-model="form.endereco.estado"
            >
          </p>
          <p v-show="validation.hasError('form.endereco.estado') " class="help is-danger">{{ validation.firstError('form.endereco.estado') }}</p>
        </div>
        <div class="field">
        <div class="field has-addons">
          <p class="control is-expanded has-icons-right">
            <input class="input"
             type="text"
              placeholder="CEP"
              v-model="form.endereco.cep"
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

    <div class="field is-grouped is-grouped-right">
      <div class="control is-grouped-right">
        <b-switch type="is-info">Envio de SMS?</b-switch>
        <b-switch type="is-info" v-model="form.adultoInapto">Adulto com Responsável?</b-switch>
      </div>
    </div>
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button type="reset" class="button" @click.prevent="reset">Limpar</button>
      </p>
      <p class="control">
        <a class="button">Novo</a>
      </p>
      <p class="control">
        <button class="button" @click.prevent="submit">Atualizar</button>
      </p>
    </div>
  </form>
</template>

<script>
import SimpleVueValidation from 'simple-vue-validator'
import auth from '../../auth'

var moment = require('moment')

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
        endereco: {
          cep: '',
          rua: '',
          numero: '',
          complemento: '',
          cidade: '',
          estado: ''
        },
        envio_sms: false,
        adultoInapto: false
      },
      isFetching: false,
      data: [],
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
      return Validator.value(value).required()
    },
    'form.responsavel': function (value) {
      if (this.form.adultoInapto) {
        return Validator.value(value).required()
      }
    },
    'form.t_responsavel': function (value) {
      return Validator.value(value).required()
    },
    'form.endereco.cep': function (value) {
      return Validator.value(value).required()
    },
    'form.endereco.rua': function (value) {
      return Validator.value(value).required()
    },
    'form.endereco.numero': function (value) {
      return Validator.value(value).required()
    },
    'form.endereco.cidade': function (value) {
      return Validator.value(value).required()
    },
    'form.endereco.estado': function (value) {
      return Validator.value(value).required()
    }
  },
  methods: {
    submit () {
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
        } else {
          vm.$toast.open({
            message:
              'Formulário inválido! Verifique o preenchimento dos campos',
            type: 'is-danger',
            position: 'is-bottom'
          })
        }
      })
    },
    copyEndereco (endereco) {
      // console.log('Copiando endereco...');
      this.form.endereco = endereco
      // console.log(JSON.stringify(this.form.endereco));
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
      this.$http
        .get(`http://localhost:5000/api/v1/paciente/cpf/${cpf}`, {
          headers: { Authorization: `b: ${auth.getToken()}` }
        })
        .then(function (response) {
          if (response.data) {
            vm.form = response.data
            vm.bAtualizar = false
            vm.bNovo = true
          }
        })
        .catch(error => {
          console.log(error.response.status)

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
      if (!this.form.endereco.cep.length) {
        this.data = []
        console.log('Nada enviado...')
        return
      }
      var cep = this.form.endereco.cep
      cep = cep.replace('.', '')
      cep = cep.replace('-', '')

      this.$http
        .get(`https://viacep.com.br/ws/${cep}/json`)
        .then(function (response) {
          if (response.data) {
            // console.log(response.body);
            vm.form.endereco.rua = response.data.logradouro
            vm.form.endereco.cidade = response.data.localidade
            vm.form.endereco.estado = response.data.uf
          }
        })
        .catch(function (error) {
          vm.erroCep()
        })
        .finally(() => {
          vm.isFetching = false
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
      this.form.endereco.cep = ''
      this.form.endereco.rua = ''
      this.form.endereco.numero = ''
      this.form.endereco.complemento = ''
      this.form.endereco.cidade = ''
      this.form.endereco.estado = ''
      this.form.envio_sms = ''
      this.form.adultoInapto = false
      this.isFetching = false
      this.data = []
      this.bNovo = true
      this.bAtualizar = true
      this.validation.reset()
    },
    pesquisarNome () {
      console.log('Pesquisar paciente')
    }
  },
  computed: {
    isChild () {
      let birthday = moment(this.form.dt_nascimento, 'DD/MM/YYYY')
      if (birthday.isValid()) {
        let age = Math.abs(birthday.diff(moment(), 'years'))
        if (age > 18) {
          return false || !this.form.adultoInapto
        } else {
          return false
        }
      }
    },
    hasCelPhone () {
      if (this.form.t_celular) {
        return true
      }
    }
  }
}
</script>
