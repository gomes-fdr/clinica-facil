<template>
  <section class="hero is-success is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="column is-4 is-offset-4">
          <h3 class="title has-text-grey">Clinica Darmas</h3>
          <p class="subtitle has-text-grey">Por favor, identifique-se para entrar.</p>
          <div class="box">
            <figure class="avatar">
              <img src="../assets/logo-darmas.png">
            </figure>
            <form>
              <b-field
                :type="{'is-danger': validation.hasError('form.email') }"
                :message="[validation.firstError('form.email')]"
              >
                <div class="control">
                  <input
                    name="email"
                    class="input is-large"
                    type="email"
                    v-model="form.email"
                    placeholder="Seu Email"
                    autofocus
                  >
                </div>
              </b-field>

              <b-field
                :type="{'is-danger': validation.hasError('form.password') }"
                :message="[validation.firstError('form.password')]"
              >
                <div class="control">
                  <input
                    name="password"
                    class="input is-large"
                    type="password"
                    v-model="form.password"
                    placeholder="Sua Senha"
                  >
                </div>
              </b-field>
              <button
                class="button is-block is-info is-large is-fullwidth"
                @click.prevent="login"
              >Login</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import SimpleVueValidation from 'simple-vue-validator'
import axios from 'axios'
// import auth from '../auth'

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório',
    email: 'Formato de e-mail inválido',
    length: 'Tamanho do campo inválido'
  }
})

export default {
  name: 'Login',
  data () {
    return {
      form: {
        email: '',
        password: ''
      }
    }
  },
  validators: {
    'form.email': function (value) {
      return Validator.value(value)
        .required()
        .email()
    },
    'form.password': function (value) {
      return Validator.value(value).required()
    }
  },
  methods: {
    login () {
      console.log(process.env.API_URL)
      this.$validate()
      .then(success => {
        if (success) {
          axios({
            method: 'post',
            url: process.env.API_URL + 'token',
            data: {
              email: this.form.email,
              password: this.form.password
            }
          })
          .then(response => {
            if (response.status === 200 && 'token' in response.data) {
              this.$session.start()
              this.$session.set('jwt', response.data.token)
              const data = JSON.parse(atob(response.data.token.split('.')[1]))
              this.$session.set('perfil', data.identity.profile)
              this.$session.set('nome', data.identity.nome)
              this.$session.set('situacao', data.identity.situacao)
              this.$session.set('profissional_id', data.identity.profissional_id)

              this.$http.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.token
              this.$acl.change(this.$session.get('perfil'))
              this.$router.replace(this.$route.query.redirect || '/')
            }
          })
          .catch(error => {
            this.$toast.open({
              message: 'Usuário ou senha INVÁLIDOS',
              type: 'is-danger',
              position: 'is-bottom'
            })
          })

        } else {
          this.$toast.open({
            message:
              'Formulário inválido! Verifique o preenchimento dos campos',
            type: 'is-danger',
            position: 'is-bottom'
          })
        }
      })
    }
  }
}
</script>


<style scoped>
html,
body {
  /* font-family: "Open Sans", serif; */
  font-size: 14px;
  font-weight: 300;
}
.hero.is-success {
  background: #f2f6fa;
}
.hero .nav,
.hero.is-success .nav {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.box {
  margin-top: 5rem;
}
.avatar {
  margin-top: -70px;
  padding-bottom: 20px;
}
.avatar img {
  padding: 5px;
  background: #fff;
  border-radius: 50%;
  -webkit-box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1),
    0 0 0 1px rgba(10, 10, 10, 0.1);
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
}
input {
  font-weight: 300;
}
p {
  font-weight: 700;
}
p.subtitle {
  padding-top: 1rem;
}
</style>