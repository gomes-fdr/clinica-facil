<template>
  <div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Endereço</label>
      </div>
      <div class="field-body">
        <div class="field" >
          <b-field :type="{'is-danger': v.$error }">
            <b-autocomplete
              id="cep"
              name="cep"
              placeholder="CEP"
              v-model="cep">
            </b-autocomplete>
          </b-field>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Rua" name="rua">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Número">
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
            <input class="input" type="text" placeholder="Complemento" :class="{ hasError: v.$error }">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Cidade" name="cidade">
          </p>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input class="input" type="text" placeholder="Estado" name="estado">
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: ""
    },
    v: {
      type: Object,
      required: true
    }
  },
  computed: {
    cep: {
      get() {
        return this.value;
      },
      set(value) {
        this.v.$touch();
        this.$emit("input", value);
      }
    }
  }
};
</script>

<style>
    .hasError  {
    color: red;
    }
</style>
