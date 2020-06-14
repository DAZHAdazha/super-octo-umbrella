import Vue from 'vue'
import Router from 'vue-router'
<<<<<<< HEAD
import Home from '@/pages/home'
import main_page from '@/pages/main_page/main_page'
=======
import Home from '@/pages/home/home'

>>>>>>> 3ffca30bb27ffb963430db94bf09d11289548dc0
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
      component:main_page
    }
  ]
})
