<template>
  <form action="#" @submit.prevent="submit">
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Identificação</label>
      </div>
      <div class="field-body">
        <div class="field">
          <b-field>
            <b-input type="text" name="nome" placeholder="Nome"></b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field>
            <b-input type="email" name="email" placeholder="Email"></b-input>
          </b-field>
        </div>
      </div>
    </div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Documentos</label>
      </div>
      <div class="field-body">
        <div class="field">
          <b-field>
            <b-input placeholder="Data Nascimento" name="dt_nascimento"></b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field>
            <b-input placeholder="Identidade" name="rg"></b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field>
            <b-input placeholder="CPF" name="cpf"></b-input>
          </b-field>
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Contatos</label>
      </div>
      <div class="field-body">
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Filiação">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Profissão">
          </p>
        </div>
        <div class="field">
          <b-field>
            <b-input placeholder="Responsável" name="responsavel"></b-input>
          </b-field>
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
            <input class="input" type="text" placeholder="Celular">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Fixo">
          </p>
        </div>
        <div class="field">
          <b-field>
            <b-input placeholder="Telefone Responsável" name="tel_resp"></b-input>
          </b-field>
        </div>
      </div>
    </div>

    <endereco v-model="form.cep" :v="$v.form.cep" />
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
        <button class="button">Atualizar</button>
      </p>
    </div>
  </form>
</template>

<script>
import Endereco from "../endereco";
import { required } from "vuelidate/lib/validators";
export default {
  components: {
    Endereco
  },
  data() {
    return {
        form: {
            cep:""
        }
    };
  },
  validations: {
    form: {
      cep: { required },
    }
  },
  methods: {
    submit() {
        this.$v.form.$touch();
        if (this.$v.form.$pending || this.$v.form.$error){
            console.log('ERROS');
            return;
        } 
        alert("Form submitted");
    }
  }
};
</script>
