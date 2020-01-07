<template>
  <div id="app">
    <Header />

    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="6" offset="3">
          <Poll v-if="questions.length"
            :currentQuestion="questions[index]"
            :next="next"
          />
        </b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import Header from './components/Header.vue'
import Poll from './components/Poll.vue'

export default {
  name: 'app',
  components: {
    Header,
    Poll
  },
  data() {
    return {
      questions: [],
      index: 0
    }
  },
  methods: {
    next() {
      this.index++
    }
  },
  mounted: function() {
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
