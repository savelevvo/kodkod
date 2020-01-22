<template>
  <div id="kodkod">
    <Header :totalCount="pCount" />

    <b-container class="bv-example-row">
      <h1 class="header-main">Recent</h1>
      <b-row>
        <b-col v-for="poll in pPolls.slice(-3)" :key="poll.id">
          <Poll v-if="pCount" :poll="poll" />
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
      pCount: 0,
      pPolls: []
    }
  },
  methods: {
    async getData(vm) {
      const axios = require('axios').default
      await axios
        .get('http://localhost:8000/polls/')
        .then(function(response) {
          console.log(response)
          vm.pPolls = response.data.results
          vm.pCount = response.data.count
        })
        .catch(function(error) {
          console.log('ERROR!' + error)
        })
    }
  },
  mounted: function() {
    this.getData(this)
  }
}
</script>

<style scoped>
.header-main {
  margin-top: 50px;
}
</style>
