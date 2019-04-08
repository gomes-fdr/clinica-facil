<template>
      <form>
    <div class="field is-horizontal">
      <div class="field-label is-normal">
        <label class="label">Senha</label>
      </div>
      <div class="field-body">
        <div class="field">
        <div class="field has-addons">
          <p class="control is-expanded">
            <input
             class="input"
             type="password"
             placeholder="Senha"
            >
          </p>
            
        </div>
        </div>
        <div class="field">
          <p class="control is-expanded">
            <input
             class="input"
             type="password"
             placeholder="Confirme a senha"
            >
          </p>
        </div>
      </div>
    </div>
    
    <hr>
    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <button type="reset" class="button" >Limpar</button>
      </p>
      <p class="control">
        <button class="button" disabled >Gravar</button>
      </p>
    </div>
  </form>
</template>

<script>
export default {
  name: 'Senha'}
</script>
