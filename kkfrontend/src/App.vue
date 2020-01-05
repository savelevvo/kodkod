<template>
  <div id="app">
    <Header />

    <b-container class="bv-example-row">
      <b-row>
        <b-col sm="6" offset="3">
          <Poll />
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
  mounted: function() {
    fetch('http://localhost:8000/auth/token/',
            {
              method: 'post',
              mode: 'no-cors',
              cache: 'no-cache',
              accept: '*/*',
              referrer: 'no-referrer',
              headers: {
                  'Access-Control-Allow-Origin': '*',
              },
              body: JSON.stringify({'username': 'admin', 'password': 'admin'})
            }
    )
    .then((response) => {console.log(response.json())})
}



}
</script>
