<template>
  <section>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">Informações do paciente</p>
      </header>
      <b-tabs position="is-centered" class="block">
        <b-tab-item label="Dados">
          <dados/>
        </b-tab-item>
        <b-tab-item label="Convênios" disabled></b-tab-item>
        <b-tab-item label="Prontuário" disabled></b-tab-item>
        <b-tab-item label="Documentos" disabled></b-tab-item>
      </b-tabs>
    </div>
  </section>
</template>
<script>
import Dados from './Dados'

export default {
  name: 'Tabs',
  components: {
    Dados
  }
}
</script>