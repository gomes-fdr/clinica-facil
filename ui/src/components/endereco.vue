<template>
  <div>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Endereço</label>
      </div>
      <div class="field-body">
        <div class="field" >
          <b-field>
            <b-autocomplete
              id="cep"
              name="cep"
              placeholder="CEP">
            </b-autocomplete>
          </b-field>
        </div>
        <div class="field">
            <input
             name="rua"
             class="input"
             type="text"
             placeholder="Rua">
        </div>
        <div class="field">
            <input
            name="numero"
             class="input"
             type="text"
             placeholder="Número">
        </div>
      </div>
    </div>

    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Endereço</label>
      </div>
      <div class="field-body">
        <div class="field">
            <input
             name="complemento"
             class="input"
             type="text"
             placeholder="Complemento">
        </div>
        <div class="field">
            <input
             name="cidade"
             class="input"
             type="text"
             placeholder="Cidade">
        </div>
        <div class="field">
            <input
             name="estado"
             class="input"
             type="text"
             placeholder="Estado">
        </div>
      </div>
    </div>
  </div>
</template>
