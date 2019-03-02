<template>
  <div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Endereço</label>
      </div>
      <div class="field-body">
          <b-field
          :type="{'is-danger': validation.hasError('form.cep') }"
          :message="[validation.firstError('form.cep')]">
            <the-mask
              name="cep"
              class="input"
              :class="{'input is-danger': validation.hasError('form.cep') }"
              mask="##.###-###"
              placeholder="CEP"
              v-model="form.cep">
            </the-mask>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.rua') }"
          :message="[validation.firstError('form.rua')]">
            <b-input
             name="rua"
             placeholder="Rua"
             v-model="form.rua">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.numero') }"
          :message="[validation.firstError('form.numero')]">
            <the-mask
            name="numero"
            class="input"
            :class="{'input is-danger': validation.hasError('form.numero') }"
            mask="#####"
            placeholder="Número"
            v-model="form.numero">
            </the-mask>
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
             v-model="form.complemento">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.cidade') }"
          :message="[validation.firstError('form.cidade')]">
            <b-input
             name="cidade"
             placeholder="Cidade"
             v-model="form.cidade">
            </b-input>
          </b-field>
          <b-field
          :type="{'is-danger': validation.hasError('form.estado') }"
          :message="[validation.firstError('form.estado')]">
            <b-input
             name="estado"
             placeholder="Estado"
             v-model="form.estado">
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
      vm.submitEndereco();
    });
  },
  data() {
    return {
      form: {
        cep: '',
        rua: '',
        numero: '',
        complemento: '',
        cidade: '',
        estado: '',
      }
    }
  },
  validators: {
    'form.cep': function(value) {
      return Validator.value(value).required();
    },
    'form.rua': function(value) {
      return Validator.value(value).required();
    },
    'form.numero': function(value) {
      return Validator.value(value).required();
    },
    'form.cidade': function(value) {
      return Validator.value(value).required();
    },
    'form.estado': function(value) {
      return Validator.value(value).required();
    },
  },
  methods: {
    submitEndereco() {
      var vm = this;
      this.$validate()
      .then(function (success) {
        if (success) {
          console.log('Validação no endereço OK!');
          vm.$bus.$emit('submitEndereco', vm.form);
        }
      });
    }
  }
}
</script>

