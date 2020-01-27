<template>
  <div>
    <b-card-group deck>
      <b-card
        :header="poll.user.toString()"
        header-tag="header"
        footer="4 Comments 21 votes 9 watchers"
        footer-tag="footer"
        :title="poll.subject"
      >
        <b-card-text>Description text</b-card-text>
        <b-list-group>
          <b-list-group-item v-for="(vote, index) in poll.votes" :key="index">
            {{ vote.text }} [{{ vote.votes_number }}]
          </b-list-group-item>
        </b-list-group>

        <b-button variant="primary">
          Submit
        </b-button>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  props: { poll: Object },
  data() {
    return {}
  },
  computed: {},
  watch: {},
  methods: {}
}
</script>
