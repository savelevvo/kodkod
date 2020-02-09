<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand><router-link to="/">KodKod</router-link></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item
            ><router-link to="/categories">Categories</router-link></b-nav-item
          >
          <b-nav-item
            ><router-link to="/companies">Companies</router-link></b-nav-item
          >
          <b-nav-item disabled></b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-input-group size="sm" class="mr-sm-2">
              <b-input-group-prepend>
                <b-button variant="outline-secondary">Search</b-button>
              </b-input-group-prepend>
              <b-form-input id="type-search" type="search"></b-form-input>
            </b-input-group>
          </b-nav-form>

          <b-nav-form v-if="$store.state.isAuthenticated">
            <b-button variant="dark">
              Profile
            </b-button>
            <b-button variant="dark" @click.prevent="logout">
              Logout
            </b-button>
          </b-nav-form>
          <b-nav-form v-else>
            <b-button variant="dark" id="popover-login-form">
              Login
            </b-button>
            <b-popover
              target="popover-login-form"
              triggers="focus"
              placement="bottom"
            >
              <Login />
            </b-popover>

            <b-button variant="dark" id="popover-signup-form">
              Sign Up
            </b-button>
            <b-popover
              target="popover-signup-form"
              triggers="focus"
              placement="bottom"
            >
              <SignUp />
            </b-popover>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import Login from './Login.vue'
import SignUp from './SignUp.vue'

export default {
  components: {
    Login,
    SignUp
  },
  methods: {
    logout() {
      this.$store.commit('removeToken')
    }
  }
}
</script>
