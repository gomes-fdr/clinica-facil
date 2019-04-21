<template>
      <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Senha</label>
      </div>
      <div class="field-body">
        <div class="field">
        <div class="field has-addons">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('password') }"
             type="password"
             placeholder="Senha"
             v-model="password"
            >
          </p>
          <p v-show="validation.hasError('password')" class="help is-danger">{{ validation.firstError('password') }}</p>
            
        </div>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             :class="{'is-danger': validation.hasError('repeat') }"
             type="password"
             placeholder="Confirme a senha"
             v-model="repeat"
            >
          </p>
          <p v-show="validation.hasError('repeat')" class="help is-danger">{{ validation.firstError('repeat') }}</p>
        </div>
      </div>
    </div>
    
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button class="button" @click.prevent="reset">Limpar</button>
      </p>
      <p class="control">
        <button class="button" :disabled="submitted" @click.prevent="submit">Gravar</button>
      </p>
    </div>
  </form>
</template>

<script>
import SimpleVueValidation from 'simple-vue-validator'
import { API_URL, eBus } from '../../main'

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório',
    match: 'Senhas diferentes'
  }
})

export default {
  name: 'Senha',
  data () {
    return {
      id: '',
      password: '',
      repeat: '',
      submitted: true
    }
  },
  validators: {
    'repeat, password': function (repeat, password) {
      if (this.validation.isTouched('repeat')) {
        this.submitted = false
        return Validator.value(repeat).required().match(password)
      }
    }
  },
  mounted () {
    let vm = this
    eBus.$on('PROFISSIONAL_ID', function (id) {
      vm.id = id
    })
  },
  methods: {
    submit: function () {
      let vm = this
      let data = {
        id_profissional: this.id,
        password: this.password
      }
      this.$validate()
        .then(function (success) {
          if (success) {
            console.log(data)
            vm.$http
            .post(`${API_URL}profissional/reset-senha`, data)
            .then(function (response) {
              console.log(response)
              vm.$toast.open({
                message: 'SUCESSO! SENHA INICIALIZADA.',
                type: 'is-success',
                position: 'is-bottom'
              })
            })
            .catch(function (error) {
              // console.log(error)
              vm.$toast.open({
                message:
                  'FALHA ao INICIALIZAR senha!',
                type: 'is-danger',
                position: 'is-bottom'
              })
            })
          }
        })
    },
    reset: function () {
      this.password = ''
      this.repeat = ''
      this.validation.reset()
    }
  }
}
</script>
