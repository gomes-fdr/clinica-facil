<template>
<div class="modal-card" >
  <header class="modal-card-head">
      <p class="modal-card-title">Repetições deste horário</p>
  </header>
  <section class="modal-card-body">
      <div class="has-text-centered">
        <p>Periodicidade</p>
        <div class="block ">
            <b-radio v-model="formControl.radio"
                native-value="Repete">
                Repete
            </b-radio>
            <b-radio v-model="formControl.radio"
                native-value="DiasSemana">
                Dias da Semana
            </b-radio>
        </div>
        <div class="has-text-left">
          <b-field label="Cada um(a)" v-if="formControl.radio == 'Repete'">
            <b-select placeholder="Selecione uma opção" expanded="true">
                <option
                    v-for="opcao in formControl.opcoes"
                    :value="opcao"
                    :key="opcao">
                    {{ opcao }}
                </option>
            </b-select>
          </b-field>
        </div>
        <div v-if="formControl.radio == 'DiasSemana'">
          <label class="checkbox">
            <input type="checkbox"> Segunda
          </label>
          <label class="checkbox">
            <input type="checkbox"> Terça
          </label>
          <label class="checkbox">
            <input type="checkbox"> Quarta
          </label>
          <label class="checkbox">
            <input type="checkbox"> Quinta
          </label>
          <label class="checkbox">
            <input type="checkbox"> Sexta
          </label>
          <label class="checkbox">
            <input type="checkbox"> Sábado
          </label>
        </div>
      </div>
        <b-field label="Até o(a)">
          <b-select placeholder="Selecione uma opção" expanded="true">
              <option
                  v-for="opcao in formControl.opcoesTempo"
                  :value="opcao"
                  :key="opcao">
                  {{ opcao }}
              </option>
          </b-select>
        </b-field>
  </section>
  <footer class="modal-card-foot">
      <button class="button" type="button" @click="$parent.close()">Fechar</button>
      <button class="button is-primary">Salvar</button>
  </footer>
</div>
</template>
<script>
export default {
  name: 'RepeticaoHorarios',
  props: ['event', 'paciente', 'modo'],
  data () {
    return {
      formControl: {
        radio: 'Repete',
        opcoes: [
          'Dia',
          'Semana',
          'Quinzena',
          'Mês'
        ],
        opcoesTempo: [
          'próxima Semana',
          'próximo Mês',
          'próximo Semestre',
          'próximo Ano'
        ]
      }
    }
  }
}
</script>

<style>
.centrado {
  margin-left: auto;
  margin-right: auto;
  width: 8em
}
</style>
