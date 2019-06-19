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
          <b-field
            label="A cada"
            v-if="formControl.radio == 'Repete'"
            :type="{'is-danger': validation.hasError('formData.unidade') }"
            :message= "validation.firstError('formData.unidade')"
          >
            <b-select
              placeholder="Selecione uma opção"
              v-model="formData.unidade"
              expanded
            >
                <option
                    v-for="opcao in formControl.opcoesUnidade"
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
        <b-field label="Repete até o(a)"
          :type="{'is-danger': validation.hasError('formData.ate') }"
          :message= "validation.firstError('formData.ate')"
        >
          <b-select 
            placeholder="Selecione uma opção"
            v-model="formData.ate"
            expanded
          >
              <option
                  v-for="opcao in formControl.opcoesRepeticao"
                  :value="opcao.ate"
                  :key="opcao.id">
                  {{ opcao.descricao }}
              </option>
          </b-select>
        </b-field>
  </section>
  <footer class="modal-card-foot">
      <button class="button" type="button" @click="$parent.close()">Fechar</button>
      <button class="button is-primary" @click.prevent="createHorario">Salvar</button>
  </footer>
</div>
</template>
<script>
import SimpleVueValidation from 'simple-vue-validator'

const Validator = SimpleVueValidation.Validator.create({
  templates: {
    required: 'Campo obrigatório'
  }
})

// let weekday = new Array(7)
// weekday[0] = 'Domingo'
// weekday[1] = 'Segunda-feira'
// weekday[2] = 'Terça-feira'
// weekday[3] = 'Quarta-feira'
// weekday[4] = 'Quinta-feira'
// weekday[5] = 'Sexta-feira'
// weekday[6] = 'Sábado'
// let day = new Date()
// let today = weekday[day.getDay()]

let moment = require('moment')
let now = moment()
console.log(now.format())

export default {
  name: 'RepeticaoHorarios',
  props: ['event', 'paciente', 'modo'],
  data () {
    return {
      formControl: {
        radio: 'Repete',
        opcoesUnidade: [
          'Dia',
          'Semana',
          'Quinzena',
          'Mês'
        ],
        opcoesRepeticao: [
          {
            id: 0,
            descricao: 'Próxima Semana',
            ate: moment().add(7, 'd')
          },
          {
            id: 1,
            descricao: 'Próximo Mês',
            ate: moment().add(1, 'M')
          },
          {
            id: 2,
            descricao: 'Próximo Semestre',
            ate: moment().add(6, 'M')
          },
          {
            id: 3,
            descricao: 'Próximo Ano',
            ate: moment().add(1, 'y')
          }
        ]
      },
      formData: {
        unidade: null,
        ate: null
      }
    }
  },
  validators: {
    'formData.unidade': function (value) {
      return Validator.value(value).required()
    },
    'formData.ate': function (value) {
      return Validator.value(value).required()
    }
  },
  methods: {
    createHorario () {
      console.log('Criação de horario(s)')
      this.$validate()
      .then(response => {
        console.log(response)
        if (response) {
          switch (this.formData.unidade) {
            case 'Dia':
              console.log('Dia até...')
              let d = moment(this.event.date)
              console.log(d.format())
              // console.log(this.formData.ate.format())

              break
            default:
              break
          }
        }
      })
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
