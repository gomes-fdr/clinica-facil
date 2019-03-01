<template>
  <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Identificação</label>
      </div>
      <div class="field-body">
          <b-field 
          :type="{'is-danger': validation.hasError('nome') }"
          :message="[validation.firstError('nome')]">
            <b-input
             name="nome"
             type="text"
             placeholder="Nome"
             v-model="nome">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('email') }"
          :message="[validation.firstError('email')]">
            <b-input
             name="email"
             type="email"
             placeholder="Email"
             v-model="email">
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
          :type="{'is-danger': validation.hasError('dt_nascimento') }"
          :message="[validation.firstError('dt_nascimento')]">
            <b-input
             name="dt_nascimento"
             placeholder="Data Nascimento"
             v-model="dt_nascimento">
             </b-input>
          </b-field>
          <b-field>
            <b-input
             name="rg"
             placeholder="Identidade"
             v-model="rg">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('cpf') }"
          :message="[validation.firstError('cpf')]">
            <b-input
             name="cpf"
             placeholder="CPF"
             v-model="cpf">
            </b-input>
          </b-field>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Contatos</label>
      </div>
      <div class="field-body">
        <b-field
        :type="{'is-danger': validation.hasError('filiacao') }"
        :message="[validation.firstError('filiacao')]">
          <b-input
            name="filiacao"
            type="text"
            placeholder="Filiação"
            v-model="filiacao">
            </b-input>
        </b-field>
        <b-field>
            <b-input
             name="profissao"
             type="text"
             placeholder="Profissão"
             v-model="profissao">
             </b-input>
        </b-field>
        <b-field
          :type="{'is-danger': validation.hasError('responsavel') }"
          :message="[validation.firstError('responsavel')]">
          <b-input
            name="responsavel"
            placeholder="Responsável"
            v-model="responsavel">
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
          <b-input
            name="celular"
            type="text"
            placeholder="Celular"
            v-model="t_celular">
          </b-input>
        </b-field>
        <b-field>
          <b-input
          name="fixo"
          type="text"
          placeholder="Fixo"
          v-model="t_fixo">
          </b-input>
        </b-field>
        <b-field>
          <b-input 
            name="tel_resp"
            placeholder="Telefone Responsável"
            v-model="t_reponsavel">
          </b-input>
        </b-field>
      </div>
    </div>

    <endereco/>
    <br>

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
import SimpleVueValidation from 'simple-vue-validator';
import Endereco from "../endereco";

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório',
    email: 'Formato de e-mail inválido'
  }
});

export default {
  components: {
    Endereco
  },
  data() {
    return {
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
      cep: '',
      rua: '',
      numero: '',
      complemento: '',
      cidade: '',
      estado: '',
      envio_sms: true,
      adulto_inapto: false
    };
  },
  validators: {
    nome: function(value) {
      return Validator.value(value).required();
    },
    email: function(value) {
      return Validator.value(value).email();
    },
    dt_nascimento: function(value) {
      return Validator.value(value).required();
    },
    cpf: function(value) {
      return Validator.value(value).required();
    },
    filiacao: function(value) {
      return Validator.value(value).required();
    },
    responsavel: function(value) {
      return Validator.value(value).required();
    },
    cep: function(value) {
      return Validator.value(value).required();
    },
    rua: function(value) {
      return Validator.value(value).required();
    },
    numero: function(value) {
      return Validator.value(value).required();
    },
    cidade: function(value) {
      return Validator.value(value).required();
    },
    estado: function(value) {
      return Validator.value(value).required();
    },
  },
  methods: {
    submit() {
         this.$validate()
          .then(function (success) {
            if (success) {
              alert('Validation succeeded!');
            }
          });
    }
  }
};
</script>
