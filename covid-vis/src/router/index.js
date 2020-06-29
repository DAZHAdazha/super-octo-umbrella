import Vue from 'vue'
import Router from 'vue-router'

import mainPage from '@/pages/main_page/main_page'
import news from '@/pages/news/news'
import popular from '@/pages/popular/popular'
import defend from '@/pages/Defend/defend'
import dataV from '@jiaminghi/data-view'
import transmit from '@/pages/transmit/transmit.vue'

Vue.use(dataV)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      redirect: '/main',
      component: mainPage
    },
    {
      path: '/main',
      name: 'main_page',
      component: mainPage
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
    },
    {
      path: '/defend',
      name: 'defend',
      component: defend
    },
    {
      path: '/transmit',
      name: 'transmit',
      component: transmit
    }
  ]
})
