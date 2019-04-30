<template>
  <section>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">Agenda de atendimento</p>
      </header>
      <br>
      <b-tabs position="is-centered"  type="is-toggle-rounded" v-model="activeTab">
        <b-tab-item label="Consulta">
          <consulta/>
        </b-tab-item>
        <b-tab-item label="Horários" v-if="!formControl.isHorarioDisabled">
          <horarios/>
        </b-tab-item>
      </b-tabs>
    </div>
  </section>
</template>
<script>
import Horarios from './Horarios'
import Consulta from './Consulta'

export default {
  name: 'Tabs',
  components: {
    Horarios,
    Consulta
  },
  data () {
    return {
      activeTab: 0,
      formControl: {
        isHorarioDisabled: false
      }
    }
  },
  methods: {
    initApp () {
      let perfil = localStorage.getItem('perfil')

      switch (perfil) {
        case 'Psicologo':
        case 'Psiquiatra':
        case 'Nutricionista':
        case 'Fonoaudiologo':
        case 'Neurologista':
        case 'Recepcao':
          this.formControl.isHorarioDisabled = true
          break
        default:
          break
      }
    }
  },
  mounted () {
    this.initApp()
  },
  computed: {
    loadConvenios () {
      if (this.activeTab === 1) {
        console.log('Carregando agenda...')
      }
    }
  }
}
</script>
<style>
.hero.is-link .tabs.is-toggle li.is-active a {
    background-color: #eaf0f4;
}
</style>
