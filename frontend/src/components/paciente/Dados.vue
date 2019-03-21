<template>
  <form id="dados">
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Identificação</label>
      </div>
      <div class="field-body">
        <b-field
          :type="{'is-danger': validation.hasError('form.nome') }"
          :message="[validation.firstError('form.nome')]"
        >
          <div class="control is-expanded">
            <input
              class="input"
              id="nome"
              name="nome"
              type="text"
              placeholder="Nome"
              v-model="form.nome"
            >
          </div>
          <div class="control">
            <a class="button is-warning" @click.prevent="pesquisarNome">
              <i class="fas fa-search"></i>
            </a>
          </div>
        </b-field>

        <b-field
          :type="{'is-danger': validation.hasError('form.email') }"
          :message="[validation.firstError('form.email')]"
        >
          <b-input name="email" type="email" placeholder="Email" v-model="form.email"></b-input>
        </b-field>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Documentos</label>
      </div>
      <div class="field-body">
        <b-field
          :type="{'is-danger': validation.hasError('form.dt_nascimento') }"
          :message="[validation.firstError('form.dt_nascimento')]"
        >
          <b-input name="dt_nascimento" placeholder="Data Nascimento" v-model="form.dt_nascimento"></b-input>
        </b-field>
        <b-field
          :type="{'is-danger': validation.hasError('form.rg') }"
          :message="[validation.firstError('form.rg')]"
        >
          <b-input name="rg" placeholder="Identidade" v-model="form.rg"></b-input>
        </b-field>
        <b-field
          :type="{'is-danger': validation.hasError('form.cpf') }"
          :message="[validation.firstError('form.cpf')]"
        >
          <div class="control is-expanded">
            <input
              class="input"
              id="cpf"
              name="cpf"
              type="text"
              placeholder="CPF"
              v-model="form.cpf"
            >
          </div>
          <div class="control">
            <a class="button is-warning" @click.prevent="pesquisarCPF">
              <i class="fas fa-search"></i>
            </a>
          </div>
        </b-field>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Contatos</label>
      </div>
      <div class="field-body">
        <b-field
          :type="{'is-danger': validation.hasError('form.filiacao') }"
          :message="[validation.firstError('form.filiacao')]"
        >
          <b-input name="filiacao" type="text" placeholder="Filiação" v-model="form.filiacao"></b-input>
        </b-field>
        <b-field>
          <b-input name="profissao" type="text" placeholder="Profissão" v-model="form.profissao"></b-input>
        </b-field>
        <b-field
          :type="{'is-danger': validation.hasError('form.responsavel') }"
          :message="[validation.firstError('form.responsavel')]"
        >
          <b-input
            name="responsavel"
            placeholder="Responsável"
            :disabled="isChild"
            v-model="form.responsavel"
          ></b-input>
        </b-field>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Telefones</label>
      </div>
      <div class="field-body">
        <b-field>
          <b-input name="celular" type="text" placeholder="Celular" v-model="form.t_celular"></b-input>
        </b-field>
        <b-field>
          <b-input name="fixo" type="text" placeholder="Fixo" v-model="form.t_fixo"></b-input>
        </b-field>
        <b-field>
          <b-input
            name="tel_resp"
            placeholder="Telefone Responsável"
            :disabled="isChild"
            v-model="form.t_reponsavel"
          ></b-input>
        </b-field>
      </div>
    </div>

    <section id="endereco">
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Endereço</label>
        </div>
        <div class="field-body">
          <b-field
            :type="{'is-danger': validation.hasError('form.endereco.cep') }"
            :message="[validation.firstError('form.endereco.cep')]"
          >
            <div class="control is-expanded">
              <input
                class="input"
                id="cep"
                name="cep"
                type="text"
                placeholder="CEP"
                v-model="form.endereco.cep"
              >
            </div>
            <div class="control">
              <a class="button is-warning" @click.prevent="pesquisarCEP">
                <i class="fas fa-search"></i>
              </a>
            </div>
          </b-field>
          <b-field
            :type="{'is-danger': validation.hasError('form.endereco.rua') }"
            :message="[validation.firstError('form.endereco.rua')]"
          >
            <b-input name="rua" placeholder="Rua" v-model="form.endereco.rua"></b-input>
          </b-field>
          <b-field
            :type="{'is-danger': validation.hasError('form.endereco.numero') }"
            :message="[validation.firstError('form.endereco.numero')]"
          >
            <b-input name="numero" placeholder="Número" v-model="form.endereco.numero"></b-input>
          </b-field>
        </div>
      </div>

      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Endereço</label>
        </div>
        <div class="field-body">
          <b-field>
            <b-input
              name="complemento"
              placeholder="Complemento"
              v-model="form.endereco.complemento"
            ></b-input>
          </b-field>
          <b-field
            :type="{'is-danger': validation.hasError('form.endereco.cidade') }"
            :message="[validation.firstError('form.endereco.cidade')]"
          >
            <b-input name="cidade" placeholder="Cidade" v-model="form.endereco.cidade"></b-input>
          </b-field>
          <b-field
            :type="{'is-danger': validation.hasError('form.endereco.estado') }"
            :message="[validation.firstError('form.endereco.estado')]"
          >
            <b-input name="estado" placeholder="Estado" v-model="form.endereco.estado"></b-input>
          </b-field>
        </div>
      </div>
    </section>
    <br>

    <div class="field is-grouped is-grouped-right">
      <div class="control is-grouped-right">
        <b-switch type="is-info" v-model="this.hasCelPhone">Envio de SMS?</b-switch>
        <b-switch type="is-info" v-model="form.adultoInapto">Adulto com Responsável?</b-switch>
      </div>
    </div>
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button type="reset" @click.prevent="reset" class="button">Limpar</button>
      </p>
      <p class="control">
        <a class="button" :disabled="bNovo">Novo</a>
      </p>
      <p class="control">
        <button class="button" @click.prevent="submit" :disabled="bAtualizar">Atualizar</button>
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
        .length(11)
    },
    'form.filiacao': function (value) {
      return Validator.value(value).required()
    },
    'form.responsavel': function (value) {
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
      // this.$bus.$emit("submit");
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
        .get(`http://localhost:5000/api/v1/paciente/cpf/${cpf}`, {'headers': {'Authorization': `b: ${auth.getToken()}`}})
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
            setTimeout(function () { auth.logout() }, 5000)
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
