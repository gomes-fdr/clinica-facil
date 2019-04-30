<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://sistema-darmas.com.br">
        <img src="../assets/logo-darmas.png">
      </a>

      <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
         <router-link class="navbar-item" to="/">Inicio</router-link>
         <router-link class="navbar-item" to="/agenda">Agenda</router-link>
         <router-link class="navbar-item" to="/paciente">Paciente</router-link>
         <router-link class="navbar-item" to="/profissional">Profissional</router-link>
        <a class="navbar-item" v-show="false">
          Ajuda
        </a>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <p>{{nome}} [{{perfil}}]</p>
        </div>
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-light" @click.prevent="logout">
              Sair
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import auth from '../auth'

export default {
  data () {
    return {
      nome: localStorage.getItem('nome'),
      perfil: localStorage.getItem('perfil')
    }
  },
  methods: {
    logout () {
      auth.logout()
    }
  }
}
</script>

