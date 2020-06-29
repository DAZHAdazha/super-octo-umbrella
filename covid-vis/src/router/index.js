import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/home/home'
import main_page from '@/pages/main_page/main_page'
import news from '@/pages/news/news'
import popular from '@/pages/popular/popular'
import dataV from '@jiaminghi/data-view'
// import transmit from '@/pages/transmit/transmit.vue'

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
    },
    {
      path: '/news',
      name: 'news',
      component: news
    },
    {
      path: '/popular',
      name: 'popular',
      component: popular
    }
    // {
    //   path: '/transmit',
    //   name: 'transmit',
    //   component: transmit
    // }
  ]
})
