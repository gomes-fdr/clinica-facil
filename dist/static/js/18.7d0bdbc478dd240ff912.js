webpackJsonp([18],{"H+bC":function(a,t,e){"use strict";var o=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("div",[e("form",[e("div",{staticClass:"modal-card",staticStyle:{width:"auto"}},[a._m(0),a._v(" "),e("section",{staticClass:"modal-card-body"},[e("p",{staticClass:" has-text-black has-text-centered"},[a._v("Profissional: "+a._s(a.event.name))]),a._v(" "),e("p",{staticClass:" has-text-black has-text-centered"},[a._v(a._s(a.date))]),a._v(" "),e("br"),a._v(" "),e("form",[e("div",{staticClass:"field is-horizontal"},[a._m(1),a._v(" "),e("div",{staticClass:"field-body"},[e("div",{staticClass:"field"},[e("div",{staticClass:"field has-addons"},[e("p",{staticClass:"control is-expanded"},[e("input",{directives:[{name:"model",rawName:"v-model",value:a.form.paciente.nome,expression:"form.paciente.nome"}],staticClass:"input",class:{"is-danger":a.validation.hasError("form.paciente.nome")},attrs:{type:"text",placeholder:"Nome"},domProps:{value:a.form.paciente.nome},on:{input:function(t){t.target.composing||a.$set(a.form.paciente,"nome",t.target.value)}}})]),a._v(" "),e("div",{staticClass:"control"},[e("a",{staticClass:"button is-right",on:{click:function(t){return t.preventDefault(),a.pesquisaPaciente(t)}}},[e("i",{staticClass:"fas fa-search"})])])]),a._v(" "),e("p",{directives:[{name:"show",rawName:"v-show",value:a.validation.hasError("form.paciente.nome"),expression:"validation.hasError('form.paciente.nome')"}],staticClass:"help is-danger"},[a._v(a._s(a.validation.firstError("form.paciente.nome")))])]),a._v(" "),e("div",{staticClass:"field"},[e("b-select",{attrs:{placeholder:"Convênio",expanded:""},model:{value:a.form.convenio,callback:function(t){a.$set(a.form,"convenio",t)},expression:"form.convenio"}},a._l(a.apiConvenios,function(t){return e("option",{key:t.id,domProps:{value:t}},[a._v("\n                "+a._s(t.descricao)+"\n                ")])}),0),a._v(" "),e("p",{directives:[{name:"show",rawName:"v-show",value:a.validation.hasError("form.convenio"),expression:"validation.hasError('form.convenio')"}],staticClass:"help is-danger"},[a._v(a._s(a.validation.firstError("form.convenio")))])],1)])])])]),a._v(" "),e("footer",{staticClass:"modal-card-foot"},[e("div",{staticClass:"field is-grouped is-grouped-right"},[e("button",{staticClass:"button is-danger",attrs:{disabled:!0}},[a._v("Confirmar Ausência")]),a._v(" "),e("button",{staticClass:"button is-danger",attrs:{disabled:!0}},[a._v("Apagar Consulta")]),a._v(" "),e("button",{staticClass:"button is-info",attrs:{disabled:!0}},[a._v("Confirmar Presença")]),a._v(" "),e("button",{staticClass:"button is-info",on:{click:function(t){return t.preventDefault(),a.salvarConsulta(t)}}},[a._v("Salvar Consulta")])])])])]),a._v(" "),e("b-modal",{attrs:{active:a.modal.isActive},on:{"update:active":function(t){return a.$set(a.modal,"isActive",t)}}},[e("b-table",{attrs:{data:a.modal.data,loading:a.modal.isLoading,columns:a.modal.columns,selected:a.modal.selected},on:{"update:selected":function(t){return a.$set(a.modal,"selected",t)},dblclick:a.copiaPaciente}})],1)],1)},i=[function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("header",{staticClass:"modal-card-head"},[e("p",{staticClass:"modal-card-title"},[a._v("Controle de Consulta")])])},function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("div",{staticClass:"field-label is-normal"},[e("label",{staticClass:"label"},[a._v("Paciente")])])}],s={render:o,staticRenderFns:i};t.a=s},U91L:function(a,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=e("X6Eo"),i=e("H+bC"),s=e("VU/8"),n=s(o.a,i.a,!1,null,null,null);t.default=n.exports},X6Eo:function(a,t,e){"use strict";var o=e("mtWM"),i=e.n(o),s=e("IXCS"),n=e.n(s),c=e("PJh5"),r=i.a.create({baseURL:"https://sistema-darmas.com.br/api/v1/",headers:{Authorization:"Bearer: "+localStorage.getItem("token")}}),l=n.a.Validator.create({templates:{required:"Campo obrigatório"}});t.a={name:"ControleConsulta",props:["event"],data:function(){return{date:"",apiConvenios:[],form:{dataMarcacao:null,confirmacao_consulta_sms:!1,compareceu:!1,paciente:{id:"",nome:""},quem_marcou_id:"",horario_id:"",convenio:[]},modal:{isLoading:!1,isActive:!1,data:[],columns:[{field:"nome",label:"Nome"},{field:"cpf",label:"CPF"}],selected:null}}},validators:{"form.paciente.nome":function(a){return l.value(a).required()},"form.convenio":function(a){return l.value(a).required()}},mounted:function(){this.initApp()},methods:{initApp:function(){this.date=c.utc(this.event.date).format("dddd, DD MMMM YYYY")+" das "+this.event.startTime+" as "+this.event.endTime,this.form.horario_id=this.event.horario_id,this.form.quem_marcou_id=localStorage.getItem("profissional_id")},salvarConsulta:function(){var a=this;console.log("Salvar NOVA consulta");var t=this;this.$validate().then(function(e){if(e){var o=a.form;o.dataMarcacao=new Date,r.post("https://sistema-darmas.com.br/api/v1/agenda/consulta",o).then(function(a){a&&(t.$toast.open({message:"CONSULTA salav com sucesso",type:"is-success",position:"is-bottom"}),t.$parent.close())}).catch(function(a){t.$toast.open({message:"FALHA ao gravar uma CONSULTA",type:"is-danger",position:"is-bottom"})}).finally(function(){})}}).catch(function(a){})},pesquisaPaciente:function(){if(console.log("Pesquisa paciente"),this.form.paciente.nome.length){var a=this;r.get("https://sistema-darmas.com.br/api/v1/paciente/nome/"+a.form.paciente.nome,{}).then(function(t){t&&(a.modal.data=t.data,a.modal.isActive=!0)}).catch(function(t){a.$toast.open({message:"NENHUM PACIENTE encontrado.",type:"is-danger",position:"is-bottom"})}).finally(function(){a.modal.isLoading=!1})}},copiaPaciente:function(){console.log("Copia paciente");var a=this;r.get("https://sistema-darmas.com.br/api/v1/paciente/nome-completo/"+a.modal.selected.nome).then(function(t){var e=t.data;a.form.paciente.id=e.id,a.form.paciente.nome=e.nome,a.getPSPaciente(a.form.paciente.id)}).catch(function(a){console.log(a)}).finally(function(){a.modal.isLoading=!1}),this.modal.isActive=!1},getPSPaciente:function(a){console.log("Busca planos de saude de um paciente");var t=this;r.get("https://sistema-darmas.com.br/api/v1/ps-paciente/"+a,{}).then(function(a){console.log(a.data),a.data.forEach(function(a){var e={id:"",descricao:""};e.id=a.id,e.descricao=a.ps.descricao,t.apiConvenios.push(e)})}).catch(function(a){console.log(a)})}}}}});
//# sourceMappingURL=18.7d0bdbc478dd240ff912.js.map