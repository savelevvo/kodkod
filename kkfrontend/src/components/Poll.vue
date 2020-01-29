<template>
  <div>
    <b-card-group deck>
      <b-card
        :header="poll.user.email"
        header-tag="header"
        :footer="footerText"
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
    return {
      footerText: ''
    }
  },
  mounted: function() {
    this.footerText = 'Votes: ' + this.poll.votes_count.toString()
  }
}
</script>
