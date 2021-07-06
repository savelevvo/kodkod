<template>
  <div>
    <b-card-group deck>
      <b-card :title="poll.subject">
        <template v-slot:header>
          <router-link
            :to="{ name: 'user-detail', params: { id: poll.user.id } }"
          >
            {{ poll.user.email }}</router-link
          >
        </template>

        <b-card-text>{{ poll.description }}</b-card-text>

        <b-form-group>
          <b-form-radio
            v-model="selected"
            name="some-radios"
            v-for="(vote, index) in poll.votes"
            :key="index"
            :value="vote.id"
          >
            {{ vote.text }} [{{ vote.votes_number }}]
          </b-form-radio>
        </b-form-group>

        <b-button variant="primary" size="sm">
          Submit
        </b-button>

        <template v-slot:footer>
          {{ 'Votes: ' + poll.votes_count.toString() }}
          <router-link :to="{ name: 'poll-detail', params: { id: poll.id } }">
            details
          </router-link>
        </template>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  props: { poll: Object },
  data() {
    return {
      selected: ''
    }
  }
}
</script>
