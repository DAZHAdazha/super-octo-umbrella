import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/home/home'
import main_page from '@/pages/main_page/main_page'
import dataV from '@jiaminghi/data-view'

Vue.use(dataV)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/main',
      name: 'main_page',
      component: main_page
    }
  ]
})
