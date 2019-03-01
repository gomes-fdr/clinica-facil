<template>
  <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Identificação</label>
      </div>
      <div class="field-body">
        <div class="field">
          <b-field>
            <b-input
             name="nome"
             type="text"
             placeholder="Nome">
            </b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field>
            <b-input
             name="email"
             type="email"
             placeholder="Email">
            </b-input>
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
            <b-input
             name="dt_nascimento"
             placeholder="Data Nascimento">
             </b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field>
            <b-input
             name="rg"
             placeholder="Identidade">
            </b-input>
          </b-field>
        </div>
        <div class="field">
          <b-field>
            <b-input
             name="cpf"
             placeholder="CPF">
            </b-input>
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
            <input
             name="filiacao"
             class="input"
             type="text"
             placeholder="Filiação">
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             name="profissao"
             class="input"
             type="text"
             placeholder="Profissão">
          </p>
        </div>
        <div class="field">
          <b-field>
            <b-input
             name="responsavel"
             placeholder="Responsável">
             </b-input>
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
            <input
             name="celular"
             class="input"
             type="text"
             placeholder="Celular">
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
            name="fixo"
            class="input"
            type="text"
            placeholder="Fixo">
          </p>
        </div>
        <div class="field">
          <b-field>
            <b-input 
             name="tel_resp"
             placeholder="Telefone Responsável">
            </b-input>
          </b-field>
        </div>
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
import Endereco from "../endereco";


export default {
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
            cep: '',
            rua: '',
            numero: '',
            complemento: '',
            cidade: '',
            estado: ''
        }
    };
  },
  
  methods: {
    submit() {
        console.log('oi');
    }
  }
};
</script>
