<template>
  <div id="kodkod">
    <Header
      :numCorrect="numCorrect"
      :numTotal="numTotal"
    />

    <b-container class="bv-example-row">
      <h1 class="header-main">Popular</h1>
      <b-row>
        <b-col v-for="i in [1,2,3]" :key="i">
          <Polls v-if="questions.length"
            :currentQuestion="questions[index]"
            :next="next"
            :increment="increment"
          />
        </b-col>
      </b-row>

      <h1 class="header-main">Recent</h1>
      <b-row>
        <b-col v-for="i in [1,2,3]" :key="i">
          <Polls v-if="questions.length"
            :currentQuestion="questions[index]"
            :next="next"
            :increment="increment"
          />
        </b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import Header from './components/Header.vue'
import Polls from './components/Polls.vue'

export default {
  name: 'kodkod',
  components: {
    Header,
    Polls
  },
  data () {
    return {
      questions: [],
      index: 0,
      numCorrect: 0,
      numTotal: 0
    }
  },
  methods: {
    next () {
      this.index++
    },
    increment (isCorrect) {
      if (isCorrect) {
        this.numCorrect++
      }
      this.numTotal++
    }
  },
  mounted: function () {
    fetch('https://opentdb.com/api.php?amount=10&type=multiple',
      {
        method: 'get'
      }
    )
      .then((response) => { return response.json() })
      .then((jsonData) => { this.questions = jsonData.results })
  }
}
</script>

<style scoped>
  .header-main {
    margin-top: 50px;
  }
</style>
