import Vuex from 'vuex'
import vue from 'vue'
vue.use(Vuex)


export default new Vuex.Store({
  state: {
    isLogin: false
  },

  getters: {
    isLogin: state => state.isLogin
  },

  mutations: {
    userStatus(state, flag) {
      state.isLogin = flag
    },
    logout (state) {
      localStorage.removeItem('username')
      state.username = null
      localStorage.removeItem('Flag')
      state.token = null
      state.isLogin = false
    }
  },

  actions: {
    userLogin({ commit }, flag) {
      commit('userStatus', flag)
    }
  }

})