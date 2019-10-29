import Vue from 'vue'
import App from './App.vue'
       // canvas模块

// 不再需要在G.ready回调中操作



Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
