webpackJsonp([14],{"6CAH":function(e,s,a){"use strict";var t=function(){var e=this,s=e.$createElement,a=e._self._c||s;return a("div",[a("form",[a("div",{staticClass:"field is-horizontal"},[e._m(0),e._v(" "),a("div",{staticClass:"field-body"},[a("div",{staticClass:"field"},[a("p",{staticClass:"control is-expanded"},[a("input",{staticClass:"input",class:{"is-danger":!0},attrs:{type:"text"}})]),e._v(" "),a("p",{directives:[{name:"show",rawName:"v-show",value:!0,expression:"true"}],staticClass:"help is-danger"},[e._v("xxx")])]),e._v(" "),a("b-field",{staticClass:"file"},[a("b-upload",{model:{value:e.file,callback:function(s){e.file=s},expression:"file"}},[a("a",{staticClass:"button is-info"},[e._v("\n                    Arquivo\n                ")])]),e._v(" "),e.file?a("span",{staticClass:"file-name"},[e._v("\n                "+e._s(e.file.name)+"\n            ")]):e._e()],1)],1)]),e._v(" "),a("div",{staticClass:"field is-grouped is-grouped-right"},[a("p",{staticClass:"control"},[a("a",{staticClass:"button",on:{click:function(s){return s.preventDefault(),e.pesquisarPlano(s)}}},[e._v("Salvar")])])])]),e._v(" "),a("b-table",{attrs:{data:e.data,columns:e.columns,"checked-rows":e.checkedRows,checkable:""},on:{"update:checkedRows":function(s){e.checkedRows=s},"update:checked-rows":function(s){e.checkedRows=s}}}),e._v(" "),a("div",{staticClass:"field is-grouped is-grouped-right"},[a("button",{staticClass:"button field is-info",attrs:{disabled:!e.checkedRows.length},on:{click:function(s){e.checkedRows=[]}}},[e._v("\n      Visualizar\n    ")])])],1)},i=[function(){var e=this,s=e.$createElement,a=e._self._c||s;return a("div",{staticClass:"field-label is-normal"},[a("label",{staticClass:"label"},[e._v("Descrição")])])}],l={render:t,staticRenderFns:i};s.a=l},"H+jj":function(e,s,a){"use strict";s.a={name:"Documentos",beforeCreate:function(){console.log("Carregando infos...")},data:function(){return{form:{dt_validade:""},data:[{descricao:"Documento de teste",dt_recebimento:"12/12/2019",responsavel:"Fabiano Gomes"}],columns:[{field:"descricao",label:"Descrição"},{field:"dt_recebimento",label:"Data da Gravação"},{field:"responsavel",label:"Responsavel"}],checkedRows:[],file:null}},methods:{pesquisarPlano:function(){console.log("Consulta planos de saude")}}}},MzM6:function(e,s,a){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var t=a("H+jj"),i=a("6CAH"),l=a("VU/8"),n=l(t.a,i.a,!1,null,null,null);s.default=n.exports}});
//# sourceMappingURL=14.1e5b97c3322e95bd2030.js.map