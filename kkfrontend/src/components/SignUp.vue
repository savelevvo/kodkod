<template>
  <b-form>
    <b-form-group id="input-group-1">
      <b-form-input
        id="input-1"
        v-model="email"
        placeholder="Email"
        type="email"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2">
      <b-form-input
        id="input-2"
        v-model="username"
        placeholder="Username"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-3" label-for="input-2">
      <b-form-input
        id="input-3"
        v-model="password"
        type="password"
        placeholder="Password"
        required
      ></b-form-input>
    </b-form-group>
    <b-button
      size="sm"
      type="submit"
      variant="primary"
      @click.prevent="createAccount"
      >Submit</b-button
    >
  </b-form>
</template>

<script>
export default {
  name: 'kodkod',

  data() {
    return {
      username: '',
      password: '',
      email: ''
    }
  },
  methods: {
    createAccount() {
      const payload = {
        username: this.username,
        password: this.password,
        email: this.email
      }
      const axios = require('axios').default
      axios
        .post(this.$store.state.endpoints.createAccount, payload)
        .then(response => {
          console.log(response)
          this.authenticate()
          this.$store.commit('updateToken', response.data.access)

          this.$store.commit('setAuthUser', {
            isAuthenticated: true
          })
        })
    },
    authenticate() {
      const payload = {
        username: this.username,
        password: this.password,
        email: this.email
      }
      const axios = require('axios').default
      axios
        .post(this.$store.state.endpoints.obtainJWT, payload)
        .then(response => {
          console.log(response)
          this.$store.commit('updateToken', response.data.access)

          this.$store.commit('setAuthUser', {
            isAuthenticated: true
          })
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
