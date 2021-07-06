import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      obtainJWT: 'http://127.0.0.1:8000/auth/token/',
      refreshJWT: 'http://127.0.0.1:8000/auth/token/refresh/',
      createAccount: 'http://127.0.0.1:8000/users/create-account/'
    }
  },

  mutations: {
    setAuthUser(state, { isAuthenticated }) {
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      localStorage.setItem('token', newToken)
      state.jwt = newToken
    },
    removeToken(state) {
      localStorage.removeItem('token')
      state.jwt = null
      Vue.set(state, 'isAuthenticated', false)
    }
  }
})
