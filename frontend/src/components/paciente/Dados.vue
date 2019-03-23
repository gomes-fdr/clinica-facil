<template>
  <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Identificação</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input is-danger" type="text" placeholder="Nome">
            <a class="icon is-small is-right">
              <i class="fas fa-search"></i>
            </a>
          </p>
          <p class="help is-danger">This field is required</p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Email">
          </p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal"></div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input class="input is-danger" type="text" placeholder="Data de Nascimento">
          </p>
          <p class="help is-danger">This field is required</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input is-danger" type="text" placeholder="CPF">
            <a class="icon is-small is-right">
              <i class="fas fa-search"></i>
            </a>
          </p>
          <p class="help is-danger">This field is required</p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input" type="text" placeholder="Identidade">
          </p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal"></div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Nome da mãe">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input" type="text" placeholder="Profissão">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input is-danger" type="text" placeholder="Responsável">
          </p>
          <p class="help is-danger">This field is required</p>
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
            <input class="input" type="text" placeholder="Telefone Celular">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input" type="text" placeholder="Telefone Fixo">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input is-danger" type="text" placeholder="Telefone Responsável">
          </p>
          <p class="help is-danger">This field is required</p>
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
            <input class="input" type="text" placeholder="Rua">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input" type="text" placeholder="Numero">
          </p>
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
            <input class="input" type="text" placeholder="Cidade">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input" type="text" placeholder="Estado">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input class="input is-danger" type="text" placeholder="CEP">
            <a class="icon is-small is-right">
              <i class="fas fa-search"></i>
            </a>
          </p>
          <p class="help is-danger">This field is required</p>
        </div>
      </div>
    </div>
    <div class="field is-grouped is-grouped-right">
      <div class="control is-grouped-right">
        <b-switch type="is-info">Envio de SMS?</b-switch>
        <b-switch type="is-info">Adulto com Responsável?</b-switch>
      </div>
    </div>
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button type="reset" class="button">Limpar</button>
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
        t_reponsavel: '',
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
        .length(11 + 3)
    },
    'form.filiacao': function (value) {
      return Validator.value(value).required()
    },
    'form.responsavel': function (value) {
      if (this.form.adultoInapto === true) {
        return Validator.value(value).required()
      }
    },
    'form.t_responsavel': function (value) {
      if (this.form.adultoInapto === true) {
        return Validator.value(value).required()
      }
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
      this.form.adultoInapto = ''
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
