<template>
  <section>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">Informações do paciente</p>
      </header>
      <b-tabs position="is-centered" class="block" v-model="activeTab">
        <b-tab-item label="Dados">
          <dados/>
        </b-tab-item>
        <b-tab-item label="Convênios" >
          <convenio/>
        </b-tab-item>
        <b-tab-item label="Prontuário" >
          <prontuario/>
        </b-tab-item>
        <b-tab-item label="Documentos" disabled></b-tab-item>
      </b-tabs>
    </div>
  </section>
</template>
<script>
import Dados from './Dados'
import Convenio from './Convenio'
import Prontuario from './Prontuario'

export default {
  name: 'Tabs',
  components: {
    Dados,
    Convenio,
    Prontuario
  },
  data () {
    return {
      activeTab: 0
    }
  },
  computed: {
    loadConvenios () {
      if (this.activeTab === 1) {
        console.log('Carregando convênios...')
      }
    }
  }
}
</script>