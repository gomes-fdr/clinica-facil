<template>
  <div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Endereço</label>
      </div>
      <div class="field-body">
          <b-field
          :type="{'is-danger': validation.hasError('cep') }"
          :message="[validation.firstError('cep')]">
            <b-autocomplete
              name="cep"
              placeholder="CEP"
              v-model="cep">
            </b-autocomplete>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('rua') }"
          :message="[validation.firstError('rua')]">
            <b-input
             name="rua"
             placeholder="Rua"
             v-model="rua">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('numero') }"
          :message="[validation.firstError('numero')]">
            <b-input
            name="numero"
            placeholder="Número"
            v-model="numero">
            </b-input>
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
             v-model="complemento">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('cidade') }"
          :message="[validation.firstError('cidade')]">
            <b-input
             name="cidade"
             placeholder="Cidade"
             v-model="cidade">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('estado') }"
          :message="[validation.firstError('estado')]">
            <b-input
             name="estado"
             placeholder="Estado"
             v-model="estado">
            </b-input>
          </b-field>
      </div>
    </div>
  </div>
</template>

<script>
import SimpleVueValidation from 'simple-vue-validator';

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório'
  }
});
export default {
  created() {
    var vm = this;
    this.$bus.$on('submit', function() {
      vm.submit();
    });
  },
  data() {
    return {
      cep: '',
      rua: '',
      numero: '',
      complemento: '',
      cidade: '',
      estado: '',
    }
  },
  validators: {
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
}
</script>

