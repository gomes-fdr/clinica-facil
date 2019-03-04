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
            <b-autocomplete
              name="cep"
              id="cep"
              v-mask="'##.###-###'"
              placeholder="CEP"
              @blur="getCEP"
              :loading="isFetching"
              :data="data"
              v-model="form.cep">
            </b-autocomplete>
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
import {debounce} from 'lodash'

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
      },
      isFetching: false,
      data: []
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
          // console.log('Validação no endereço OK!');
          vm.$bus.$emit('submitEndereco', vm.form);
        }
      });
    },
    getCEP: debounce(function () {
        if (!this.form.cep.length) {
          this.data = []
            return
        }
        var cep = this.form.cep;
        cep = cep.replace('.', '');
        cep = cep.replace('-', '');

        this.isFetching = true;
        this.$http.get(`https://api.postmon.com.br/v1/cep/${cep}`)
            .then(function(response) {
                this.data = []
                if (response.body) {
                    // console.log(response.body);
                    this.form.rua = response.body.logradouro;
                    this.form.cidade = response.body.cidade;
                    this.form.estado = response.body.estado;
                }
                // debugger
            })
            .catch((error) => {
                this.data = [];
                this.erroCep();
                // throw error;
            })
            .finally(() => {
                this.isFetching = false
            })
    }, 500),
    erroCep() {
        this.$toast.open({
            duration: 5000,
            message: 'CEP não encontrado',
            type: 'is-warning',
            position: 'is-bottom'

        })
    }
  }
}
</script>

<style>
    #cep {
      background-color: #FFDB7E;
    }
</style>