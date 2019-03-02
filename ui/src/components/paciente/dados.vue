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
             placeholder="Data Nascimento"
             v-model="form.dt_nascimento">
             </b-input>
          </b-field>
          <b-field>
            <b-input
             name="rg"
             placeholder="Identidade"
             v-model="form.rg">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.cpf') }"
          :message="[validation.firstError('form.cpf')]">
            <b-input
             name="cpf"
             placeholder="CPF"
             v-model="form.cpf">
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
          <b-input
            name="celular"
            type="text"
            placeholder="Celular"
            v-model="form.t_celular">
          </b-input>
        </b-field>
        <b-field>
          <b-input
          name="fixo"
          type="text"
          placeholder="Fixo"
          v-model="form.t_fixo">
          </b-input>
        </b-field>
        <b-field>
          <b-input 
            name="tel_resp"
            placeholder="Telefone Responsável"
            v-model="form.t_reponsavel">
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
        envio_sms: true,
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
    'form.cpf': function(value) {
      return Validator.value(value).required();
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
      this.$bus.$emit('submit');
      this.$validate()
      .then(function (success) {
        if (success) {
          console.log('Validou, enviando...');
        }
      });
    },
    copyEndereco(endereco) {
      console.log('Copiando endereco...');
      this.form.endereco = endereco;
      console.log(JSON.stringify(this.form.endereco));
    }
  }
};
</script>
