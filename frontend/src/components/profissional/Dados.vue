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
      <div class="field-label is-normal">
        <label class="label">Formação</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             type="text"
             placeholder="Faculdade"
             v-model="form.faculdade"
            >
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded has-icons-right">
            <input
             class="input"
             type="text"
             placeholder="Numero Conselho"
             v-model="form.no_conselho"
            >
          </p>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Perfil</label>
      </div>
      <div class="field-body">
        <div class="field">
          <b-select 
          placeholder="Perfil"
          expanded
          v-model="form.perfis"
          >
            <option
              v-for="p in perfilAPI"
              :value="p.id"
              :key="p.id"
            >
              {{ p.descricao }}
            </option>
          </b-select>
          <p v-show="validation.hasError('form.perfis')" class="help is-danger">{{ validation.firstError('form.perfis') }}</p>
        </div>
        <div class="field">
          <b-select 
          placeholder="Situação"
          expanded
          v-model="form.situacoes"
          >
            <option
              v-for="s in situacaoAPI"
              :value="s.id"
              :key="s.id">
              {{ s.descricao }}
            </option>
          </b-select>
          <p v-show="validation.hasError('form.situacoes')" class="help is-danger">{{ validation.firstError('form.situacoes') }}</p>
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

    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button type="reset" class="button" @click.prevent="reset">Limpar</button>
      </p>
      <p class="control">
        <button class="button" :disabled="bSenha" @click.prevent="inicializaSenha('1234')">Inicializa Senha</button>
      </p>
      <p class="control">
        <a class="button" :disabled="bNovo" @click.prevent="novoProfissional">Novo</a>
      </p>
      <p class="control">
        <button class="button" :disabled="bAtualizar" @click.prevent="atualizarProfissional">Atualizar</button>
      </p>
    </div>
  </form>
  <b-modal :active.sync="isImageModalActive">
    <b-table 
    :data="tabProfissional.data"
    :loading="tabProfissional.isLoading"
    :columns="tabProfissional.columns"
    :selected.sync="tabProfissional.selected"
    @dblclick="copiaProfissional"
    >
    
    </b-table>

  </b-modal>
</div>
</template>

<script>
import SimpleVueValidation from 'simple-vue-validator'
import { eBus } from '../../main'

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
      isImageModalActive: false,
      perfilAPI: '',
      situacaoAPI: '',
      tabProfissional: {
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
        id: '',
        nome: '',
        email: '',
        dt_nascimento: '',
        cpf: '',
        rg: '',
        faculdade: '',
        no_conselho: '',
        perfis: '',
        situacoes: '',
        t_celular: '',
        t_fixo: '',
        cep: '',
        rua: '',
        numero: '',
        complemento: '',
        cidade: '',
        estado: ''
      },
      bNovo: true,
      bAtualizar: true,
      bSenha: true
    }
  },
  validators: {
    'form.nome': function (value) {
      return Validator.value(value).required()
    },
    'form.email': function (value) {
      return Validator.value(value).email().required()
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
    'form.perfis': function (value) {
      return Validator.value(value).required()
    },
    'form.situacoes': function (value) {
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
  created () {
    this.perfilProfissional()
    this.situacaoProfissional()
  },
  methods: {
    copiaProfissional () {
      console.log('Copia Profissional')
      if (!this.tabProfissional.selected.nome) {
        return
      }
      this.$http
      .get(`${process.env.API_URL}profissional/nome-completo/${this.tabProfissional.selected.nome}`)
      .then(response => {
        // console.log(response)
        let tmp = response.data
        let t = moment.utc(tmp.dt_nascimento).format('DD/MM/YYYY')
        tmp.dt_nascimento = t
        // console.log(tmp)
        this.form = tmp
        this.bNovo = true
        this.bSenha = false
        this.bAtualizar = false
        eBus.$emit('PROFISSIONAL_ID', this.form.id)
      })
      .catch(error => {
        // console.log(error)
        this.$toast.open({
          message:
            'NENHUM PROFISSIONAL encontrado.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
      .finally(() => {
        this.tabProfissional.isLoading = false
      })
      this.isImageModalActive = false
    },
    perfilProfissional () {
      this.$http
      .get(`${process.env.API_URL}profissional/perfil`)
      .then(response => {
        this.perfilAPI = response.data
      })
    },
    situacaoProfissional () {
      this.$http
      .get(`${process.env.API_URL}profissional/situacao`)
      .then(response => {
        // console.log(response.data)
        this.situacaoAPI = response.data
      })
    },
    pesquisarNome () {
      console.log('Pesquisar profissional')
      if (!this.form.nome.length) {
        return
      }
      this.tabProfissional.isLoading = true
      this.$http
      .get(`${process.env.API_URL}profissional/nome/${this.form.nome}`)
      .then(response => {
        this.tabProfissional.data = response.data
        this.isImageModalActive = true
      })
      .catch(error => {
        this.$toast.open({
          message:
            'NENHUM PROFISSIONAL encontrado com esse nome.',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
      .finally(() => {
        this.tabProfissional.isLoading = false
      })
    },
    pesquisarCPF () {
      console.log('Pesquisar CPF')
      if (!this.form.cpf.length) {
        return
      }
      this.$http
      .get(`${process.env.API_URL}profissional/cpf/${this.form.cpf}`)
      .then(response => {
        let tmp = response.data
        let t = moment.utc(tmp.dt_nascimento).format('DD/MM/YYYY')
        tmp.dt_nascimento = t
        // console.log(tmp)
        this.form = tmp
        this.bAtualizar = false
        this.bSenha = false
        this.bNovo = true
      })
      .catch(error => {
        // console.log(error)
        this.$toast.open({
          duration: 5000,
          message: 'PACIENTE não encontrado',
          type: 'is-warning',
          position: 'is-bottom'
        })
        this.bNovo = false
        this.bSenha = false
        this.bAtualizar = true
      })
    },
    novoProfissional () {
      console.log('Novo Profissional')
      let data = {}

      this.$validate()
      .then(response => {
        // console.log(response)
        if (response) {
          data = {...this.form}
          delete data.id
          let dtTmp = moment.utc(this.form.dt_nascimento, 'DD/MM/YYYY')
          data.dt_nascimento = dtTmp
          // console.log(JSON.stringify(data))
          this.$http
          .post(`${process.env.API_URL}profissional`, data)
          .then(response => {
            this.$toast.open({
              message: 'SUCESSO! PACIENTE gravado.',
              type: 'is-success',
              position: 'is-bottom'
            })
          })
          .catch(error => {
            // console.log(error)
            this.$toast.open({
              message:
                'FALHA ao inserir novo PACIENTE!',
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
        } else {
          this.$toast.open({
            message:
              'FORMULÁRIO INCOMPLETO',
            type: 'is-danger',
            position: 'is-bottom'
          })
        }
      })
    },
    reset () {
      this.form.nome = ''
      this.form.email = ''
      this.form.dt_nascimento = ''
      this.form.cpf = ''
      this.form.rg = ''
      this.form.faculdade = ''
      this.form.no_conselho = ''
      this.form.perfis = ''
      this.form.situacoes = ''
      this.form.t_celular = ''
      this.form.t_fixo = ''
      this.form.cep = ''
      this.form.rua = ''
      this.form.numero = ''
      this.form.complemento = ''
      this.form.cidade = ''
      this.form.estado = ''
      this.data = []
      this.bNovo = true
      this.bSenha = true
      this.bAtualizar = true
      this.validation.reset()
    },
    pesquisarCEP () {
      if (!this.form.cep.length) {
        this.data = []
        console.log('Nada enviado...')
        return
      }
      var cep = this.form.cep
      cep = cep.replace('.', '')
      cep = cep.replace('-', '')

      // Remove o cabeçalho de autorização, feio mas funciona
      this.$http.defaults.headers.common = {}

      this.$http
        .get(`https://viacep.com.br/ws/${cep}/json`)
        .then(response => {
          if (response.data) {
            // console.log(response.body);
            this.form.rua = response.data.logradouro
            this.form.cidade = response.data.localidade
            this.form.estado = response.data.uf
          }
        })
        .catch(error => {
          this.erroCep()
        })
        .finally(() => {
          // Adiciona o cabeçãlho de autorização, feio ma funciona
          this.$http.defaults.headers.common['Authorization'] = 'Bearer ' + this.$session.get('jwt')
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
    atualizarProfissional () {
      console.log('Atualizar profissional')
      let data = {...this.form}

      this.$validate()
      .then(response => {
        if (response) {
          delete data.id
          let dtTmp = moment.utc(this.form.dt_nascimento, 'DD/MM/YYYY')
          data.dt_nascimento = dtTmp
          if (!data.faculdade) {
            data.faculdade = null
          }
          if (!data.no_conselho) {
            data.no_conselho = null
          }
          console.log(JSON.stringify(data))
          this.$http
          .post(`${process.env.API_URL}profissional/${this.form.nome}`, data)
          .then(response => {
            // console.log(response)
            this.$toast.open({
              message: 'SUCESSO! PROFISSIONAL gravado.',
              type: 'is-success',
              position: 'is-bottom'
            })
          })
          .catch(error => {
            // console.log(error)
            this.$toast.open({
              message:
                'FALHA ao inserir novo PROFISSIONAL!',
              type: 'is-danger',
              position: 'is-bottom'
            })
          })
        } else {
          this.$toast.open({
            message:
              'FORMULÁRIO INCOMPLETO',
            type: 'is-danger',
            position: 'is-bottom'
          })
        }
      })
    },
    inicializaSenha (p) {
      console.log('Inicializa Senha de Profissional')
      let data = {
        id_profissional: this.form.id,
        password: p
      }

      this.$http
      .post(`${process.env.API_URL}profissional/reset-senha`, data)
      .then(response => {
        this.$toast.open({
          message: 'SUCESSO! SENHA INICIALIZADA.',
          type: 'is-success',
          position: 'is-bottom'
        })
      })
      .catch(error => {
        // console.log(error)
        this.$toast.open({
          message:
            'FALHA ao INICIALIZAR senha!',
          type: 'is-danger',
          position: 'is-bottom'
        })
      })
    }
  }
}
</script>
