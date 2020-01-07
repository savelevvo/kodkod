<template>
    <div>
      <b-jumbotron header="BootstrapVue" lead="Bootstrap v4 Components for Vue.js 2">
        <p>
            {{ currentQuestion.question }}
        </p>
        <b-button @click="next" variant="success" href="#">Next</b-button>
      </b-jumbotron>
    </div>
</template>

<script>
    export default {
        props: {
            currentQuestion: Object,
            next: Function
        }
    }
</script>
