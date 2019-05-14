<template>
  <section>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">Informações do paciente</p>
      </header>
      <br>
      <b-tabs position="is-centered"  type="is-toggle-rounded" v-model="activeTab">
        <b-tab-item label="Dados">
          <dados/>
        </b-tab-item>
        <b-tab-item label="Convênios" v-if="true">
          <convenios/>
        </b-tab-item>
        <b-tab-item label="Prontuário" v-if="isActive">
          <prontuarios/>
        </b-tab-item>
        <b-tab-item label="Documentos" v-if="false">
          <documentos/>
        </b-tab-item>
      </b-tabs>
    </div>
  </section>
</template>
<script>
import Dados from './Dados'
import Convenios from './Convenios'
import Prontuarios from './Prontuarios'
import Documentos from './Documentos'

export default {
  name: 'Tabs',
  components: {
    Dados,
    Convenios,
    Prontuarios,
    Documentos
  },
  data () {
    return {
      activeTab: 0,
      isActive: true
    }
  },
  methods: {
    initApp () {
      let perfil = this.$session.get('perfil')

      switch (perfil) {
        case 'Recepcao':
          this.isActive = false
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
        console.log('Carregando convênios...')
      }
    },
    isEnable () {
      // Para habilitar/desabilitar tabs Convênios e prontuários
    }
  }
}
</script>
<style>
.hero.is-link .tabs.is-toggle li.is-active a {
    background-color: #eaf0f4;
}
</style>
