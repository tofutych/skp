<template>
  <div class="home">
    <div class="columns is-mobile is-multiline is-centered">

      <GroupBox v-for="group in groups" v-bind:key="group.id" v-bind:group="group"></GroupBox>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
import GroupBox from "@/components/GroupBox.vue";

export default {
  name: 'HomeView',

  data() {
    return {
      groups: []
    }
  },

  components: {
    GroupBox
  },

  mounted() {
    this.getGroups()
  },

  methods: {
    getGroups() {
      axios
        .get('/api/groups/')
        .then(response => {
          this.groups = response.data
          console.log(this.groups)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
