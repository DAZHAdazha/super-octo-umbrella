// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import echarts from 'echarts'
import vueResource from 'vue-resource'
import ant from 'ant-design-vue'
import 'ant-design-vue/dist/antd.less'
import 'jquery'

Vue.use(ant)
Vue.use(vueResource)
Vue.prototype.$echarts = echarts
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
