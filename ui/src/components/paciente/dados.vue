<template>
  <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Identificação</label>
      </div>
      <div class="field-body">
          <b-field 
          :type="{'is-danger': validation.hasError('form.nome') }"
          :message="[validation.firstError('form.nome')]">
            <b-input
             id="nome"
             name="nome"
             type="text"
             placeholder="Nome"
             v-model="form.nome">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.email') }"
          :message="[validation.firstError('form.email')]">
            <b-input
             name="email"
             type="email"
             placeholder="Email"
             v-model="form.email">
            </b-input>
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
          :message="[validation.firstError('form.dt_nascimento')]">
            <b-input
             name="dt_nascimento"
             v-mask="'##/##/####'"
             placeholder="Data Nascimento"
             v-model="form.dt_nascimento">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.rg') }"
          :message="[validation.firstError('form.rg')]">
            <the-mask
             name="rg"
             placeholder="Identidade"
             class="input"
            :class="{'input is-danger': validation.hasError('form.rg') }"
             mask="##########"
             v-model="form.rg">
            </the-mask>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.cpf') }"
          :message="[validation.firstError('form.cpf')]">
            <the-mask
             id="cpf"
             name="cpf"
             class="input"
            :class="{'input is-danger': validation.hasError('form.cpf') }"
             mask="###.###.###-##"
             placeholder="CPF"
             v-model="form.cpf">
            </the-mask>
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
        :message="[validation.firstError('form.filiacao')]">
          <b-input
            name="filiacao"
            type="text"
            placeholder="Filiação"
            v-model="form.filiacao">
            </b-input>
        </b-field>
        <b-field>
            <b-input
             name="profissao"
             type="text"
             placeholder="Profissão"
             v-model="form.profissao">
             </b-input>
        </b-field>
        <b-field
          :type="{'is-danger': validation.hasError('form.responsavel') }"
          :message="[validation.firstError('form.responsavel')]">
          <b-input
            name="responsavel"
            placeholder="Responsável"
            v-model="form.responsavel">
          </b-input>
        </b-field>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Telefones</label>
      </div>
      <div class="field-body">
        <b-field>
          <the-mask
            name="celular"
            type="text"
            class="input"
            :mask="['(##) ####-####', '(##) #####-####']" 
            placeholder="Celular"
            v-model="form.t_celular">
          </the-mask>
        </b-field>
        <b-field>
          <the-mask
          name="fixo"
          type="text"
          class="input"
          :mask="['(##) ####-####', '(##) #####-####']" 
          placeholder="Fixo"
          v-model="form.t_fixo">
          </the-mask>
        </b-field>
        <b-field>
          <the-mask 
            name="tel_resp"
            class="input"
            :mask="['(##) ####-####', '(##) #####-####']" 
            placeholder="Telefone Responsável"
            :disabled=isChild
            v-model="form.t_reponsavel">
          </the-mask>
        </b-field>
      </div>
    </div>

    <endereco/>
    <br>

    <div class="field is-grouped is-grouped-right">
      <div class="control is-grouped-right">
        <b-switch type="is-info" v-model="this.hasCelPhone">
          Envio de SMS?
        </b-switch>
        <b-switch type="is-info" v-model="form.adulto_inapto">
          Adulto com Responsável?
        </b-switch>
      </div>
    </div>
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button type="reset" class="button" >Limpar</button>
      </p>
      <p class="control">
        <a class="button" disabled>Novo</a>
      </p>
      <p class="control">
        <button class="button" @click.prevent="submit" disabled>Atualizar</button>
      </p>
    </div>
  </form>
</template>

<script>
import SimpleVueValidation from 'simple-vue-validator';
import Endereco from "../endereco";

var moment = require('moment');

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório',
    email: 'Formato de e-mail inválido',
    length: 'Tamanho do campo inválido'
  }
});

export default {
  created() {
    var vm = this;
    this.$bus.$on('submitEndereco', function(endereco) {
      vm.copyEndereco(endereco);
    });
  },
  components: {
    Endereco
  },
  data() {
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
          estado: '',
        },
        envio_sms: false,
        adulto_inapto: false,
      },
    };
  },
  validators: {
    'form.nome': function(value) {
      return Validator.value(value).required();
    },
    'form.email': function(value) {
      return Validator.value(value).email();
    },
    'form.dt_nascimento': function(value) {
      return Validator.value(value).required();
    },
    'form.rg': function(value) {
      return Validator.value(value).length(10);
    },
    'form.cpf': function(value) {
      return Validator.value(value).required().length(11);
    },
    'form.filiacao': function(value) {
      return Validator.value(value).required();
    },
    'form.responsavel': function(value) {
      return Validator.value(value).required();
    },    
  },
  methods: {
    submit() {
      var vm = this;
      this.$bus.$emit('submit');
      this.$validate()
      .then(function (success) {
        if (success) {
          // console.log('Validou, enviando...');
          // console.log(JSON.stringify(vm.form));
          vm.$toast.open({
              message: 'Formulário preenchido com sucesso!',
              type: 'is-success',
              position: 'is-bottom'
          })
          return;
        } else {
          vm.$toast.open({
              message: 'Formulário inválido! Verifique o preenchimento dos campos',
              type: 'is-danger',
              position: 'is-bottom'
          })
        }
      });
    },
    copyEndereco(endereco) {
      // console.log('Copiando endereco...');
      this.form.endereco = endereco;
      // console.log(JSON.stringify(this.form.endereco));
    }
  },
  computed: {
    isChild() {
      let birthday = moment(this.form.dt_nascimento, "DD/MM/YYYY");
      if (birthday.isValid()) {
          let age = Math.abs(birthday.diff(moment(), 'years'))
          if (age > 18) {
              return (false || !this.form.adulto_inapto);
          } else {
              return false;
          }
      }
    },
    hasCelPhone() {
      if (this.form.t_celular) {
        return true;
      }
    }
  },
};
</script>
<style>
    #cpf, #nome {
      background-color: #FFDB7E;
    }
</style>