<template>
<div>
  <h4 class="title is-4 has-text-black has-text-centered">Sala: Profissional:</h4>
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
            <a class="button is-info" @click.prevent="eventCalendar">Montar Calendário</a>
          </p>
        </div>
    </div>
  </form>

<b-modal :width="1024" :active.sync="modal.isCalendarActive">
    <vue-scheduler
      :events="events"
      :event-dialog-config="dialogConfig"
      event-display="name"
      @event-clicked="eventClicked"
      :key="componentKey"
    >
    </vue-scheduler>
</b-modal>


</div>
</template>
<script>
import _ from 'lodash'

export default {
  name: 'Horarios',
  data () {
    return {
      componentKey: 0,
      modal: {
        isCalendarActive: false
      },
      dialogConfig: {
        title: 'Novo Horário',
        createButtonLabel: 'Adciona Horário',
        enableTimeInputs: true,
        fields: [
          {
            fields: [
              {
                name: 'hora',
                label: 'Hora',
                type: 'time'
              },
              {
                name: 'duracao',
                label: 'Duração'
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
                label: 'Sala'
              },
              {
                name: 'profissional',
                label: 'Profissional'
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
      _.remove(this.events, event)

      // Para forçar a renderização do calendário
      this.componentKey += 1
    },
    eventCalendar () {
      console.log('Calendario de eventos')
      this.modal.isCalendarActive = true
    },
    forceRerender () {
      this.componentKey += 1
    }
  },
  computed:{
    removeEvent (event) {
    }
  }
}
</script>

