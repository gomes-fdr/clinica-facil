<template>
<div>
  <form>
    <div class="section">

      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Horário</label>
        </div>
        <div class="field-body">
          <div class="field">
          <div class="field has-addons">
            <p class="control is-expanded">
              <input
              class="input"
              type="text"
              placeholder="Onde? (Sala)"
              >
            </p>
              <div class="control">
                <a class="button">
                  <i class="fas fa-plus"></i>
                </a>
              </div>
              <div class="control">
                <a class="button" >
                  <i class="fas fa-question"></i>
                </a>
              </div>
          </div>
          </div>
          <div class="field">
            <div class="field has-addons">
              <p class="control is-expanded">
                <input
                class="input"
                type="text"
                placeholder="Quem? (Profissional)"
                >
              </p>
              <div class="control">
                <a class="button">
                  <i class="fas fa-search"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
        <div class="field is-grouped is-grouped-right">
          <p class="control">
            <a class="button is-info" >Selecionar</a>
          </p>
        </div>
    </div>
  </form>
  <vue-scheduler
    :events="events"
    :event-dialog-config="dialogConfig"
    event-display="name"
    @event-clicked="eventClicked"
  >

  </vue-scheduler>
</div>
</template>
<script>
export default {
  name: 'Horarios',
  data () {
    return {
      dialogConfig: {
        title: 'Novo Horário',
        createButtonLabel: 'Adciona Horário',
        enableTimeInputs: false,
        fields: [
          {
            fields: [
              {
                name: 'hora',
                label: 'Hora',
                type: 'time',
                required: true
              },
              {
                name: 'duracao',
                label: 'Duração',
                required: true
              }
            ]
          },
          {
            name: 'repete',
            label: 'No. de vezes no dia',
            value: '1',
            required: true
          },
          {
            label: 'Consulta',
            fields: [
              {
                name: 'sala',
                label: 'Sala',
                required: true
              },
              {
                name: 'profissional',
                label: 'Profissional',
                required: true
              }
            ]
          }
        ]
      },
      events: []
    }
  },
  methods: {
    eventClicked (event) {
      console.log('Evento selecionado')
      console.log(event)
    }
  }
}
</script>

