<template>
  <section>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">Informações do profissional</p>
      </header>
      <br>
      <b-tabs position="is-centered"  type="is-toggle-rounded" v-model="activeTab">
        <b-tab-item label="Dados">
          <dados/>
        </b-tab-item>
        <b-tab-item label="Documentos" >
          <documentos/>
        </b-tab-item>
        <b-tab-item label="Senha do Sistema" >
          <senha/>
        </b-tab-item>
      </b-tabs>
    </div>
  </section>
</template>
<script>
import Dados from './Dados'
import Documentos from './Documentos'
import Senha from './Senha'

export default {
  name: 'Tabs',
  components: {
    Dados,
    Documentos,
    Senha
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
<style>
.hero.is-link .tabs.is-toggle li.is-active a {
    background-color: #eaf0f4;
}
</style>


