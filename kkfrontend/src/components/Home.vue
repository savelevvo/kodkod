<template>
  <div id="kodkod">
    <Header />

    <b-container class="bv-example-row">
      <h1 class="header-main">Recent</h1>
      <b-row>
        <b-col v-for="poll in recentPolls" :key="poll.id">
          <Poll :poll="poll" />
        </b-col>
      </b-row>

      <h1 class="header-main">Popular</h1>
      <b-row>
        <b-col v-for="poll in popularPolls" :key="poll.id">
          <Poll :poll="poll" />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Header from './Header.vue'
import Poll from './Poll.vue'

export default {
  name: 'kodkod',
  components: {
    Header,
    Poll
  },
  data() {
    return {
      recentPolls: [],
      popularPolls: []
    }
  },
  methods: {
    getPollsData(vm, endpoint) {
      const axios = require('axios').default
      axios
        .get('http://localhost:8000/polls/' + endpoint + '/?offset=0&limit=3')
        .then(function(response) {
          if (endpoint === 'recent') vm.recentPolls = response.data.results

          if (endpoint === 'popular') vm.popularPolls = response.data.results
        })
        .catch(function(error) {
          console.log(error)
        })
    }
  },
  mounted: function() {
    this.getPollsData(this, 'recent')
    this.getPollsData(this, 'popular')
  }
}
</script>

<style scoped>
.header-main {
  margin-top: 50px;
}
</style>
