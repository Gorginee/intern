import Register from './components/Register.vue'
import Login from './components/Login.vue'
import Logout from './components/Logout.vue'
import LoginRequired from './components/LoginRequired.vue'
import Router from 'vue-router'
import store from '../store'

const router = new Router({
  mode: 'history',
  routes: [
    {
      name: 'register',
      path: '/register',
      component: Register,
      meta: {
        loginRequired: false
      }
    },
    {
      name: 'login',
      path: '/login',
      component: Login,
      meta: {
        loginRequired: false
      }
    },
    {
      name: 'logout',
      path: '/logout',
      component: Logout,
      meta: {
        loginRequired: false
      }
    },
    {
      name: 'lr',
      path: '/lr',
      component: LoginRequired,
      meta: {
        loginRequired: true
      }
    }
  ]
})


router.beforeEach((to, from, next) => {
  let getFlag = localStorage.getItem('Flag')

  if (getFlag === 'isLogin') {
    store.state.isLogin = true
    // store.dispatch('userLogin', true)
    next()

    if (to.path === '/login' || to.path === '/register') {
      next({
        path: '/'
      })
    }

  } else {
    if (to.meta.loginRequired) {
      next({
        path: '/login'
      })
      alert('Please log in first !')
    } else {
      next()
    }
  }
})




export default router


