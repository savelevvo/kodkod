<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand>KodKod</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <b-navbar-nav>
          <b-nav-item href="#">Categories</b-nav-item>
          <b-nav-item href="#">Companies</b-nav-item>
          <b-nav-item disabled>Counter: {{ numCorrect }}/{{ numTotal }}</b-nav-item>
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

          <b-nav-item href="#">Login</b-nav-item>
          <b-nav-item href="#">Sign Up</b-nav-item>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>



</template>

<script>
  export default {
      props: [
          'numCorrect',
          'numTotal'
      ]
  }
</script>
