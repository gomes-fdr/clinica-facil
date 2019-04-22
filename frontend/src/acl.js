import Vue from 'vue'
import router from './router'
import { AclInstaller, AclCreate, AclRule } from 'vue-acl'

Vue.use(AclInstaller)

export default new AclCreate({
  initial: 'Publico',
  notfound: '/login',
  router,
  acceptLocalRules: true,
  globalRules: {
    isPsicologo: new AclRule('Psicologo'),
    isRecepcao: new AclRule('Recepcao'),
    isPsiquiatra: new AclRule('Psiquiatra'),
    isNutricionista: new AclRule('Nutricionista'),
    isFonoaudiologo: new AclRule('Fonoaudiologo'),
    isNeurologista: new AclRule('Neurologista'),
    isCoordenador_Agendas: new AclRule('Coordenador_Agendas'),
    isAdministracao: new AclRule('Administracao').or('Psicologo').or('Recepcao'),
    isPublico: new AclRule('Publico')
  }
})
