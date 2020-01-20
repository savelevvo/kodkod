<template>
  <div id="kodkod">
    <Header :totalCount="pCount" />

    <b-container class="bv-example-row">
      <h1 class="header-main">Popular</h1>
      <b-row>
        <b-col v-for="poll in pPolls" :key="poll.id">
          <Polls v-if="pCount" :subject="poll.subject" :author="poll.user" />
        </b-col>
      </b-row>

      <!--      <h1 class="header-main">Recent</h1>-->
      <!--      <b-row>-->
      <!--        <b-col v-for="i in [1, 2, 3]" :key="i">-->
      <!--          <Polls-->
      <!--            v-if="questions.length"-->
      <!--            :currentQuestion="questions[index]"-->
      <!--            :next="next"-->
      <!--            :increment="increment"-->
      <!--          />-->
      <!--        </b-col>-->
      <!--      </b-row>-->
    </b-container>
  </div>
</template>

<script>
import Header from './Header.vue'
import Polls from './Poll.vue'

export default {
  name: 'kodkod',
  components: {
    Header,
    Polls
  },
  data() {
    return {
      questions: [],
      index: 0,
      numCorrect: 0,
      numTotal: 0,
      pCount: 0,
      pPolls: []
    }
  },
  methods: {
    next() {
      this.index++
    },
    increment(isCorrect) {
      if (isCorrect) {
        this.numCorrect++
      }
      this.numTotal++
    },
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
