<template>
  <section>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">Informações do paciente</p>
      </header>
      <br>
      <b-tabs position="is-centered"  type="is-toggle-rounded" v-model="activeTab">
        <b-tab-item label="Consulta">
        </b-tab-item>
        <b-tab-item label="Horários" v-if="true">
          <horarios/>
        </b-tab-item>
      </b-tabs>
    </div>
  </section>
</template>
<script>
import Horarios from './Horarios'

export default {
  name: 'Tabs',
  components: {
    Horarios
  },
  data () {
    return {
      activeTab: 0
    }
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
