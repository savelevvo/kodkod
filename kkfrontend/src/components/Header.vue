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

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
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
