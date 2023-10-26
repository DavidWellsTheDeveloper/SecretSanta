<template>
  <v-container>
    <h1>My Events</h1>
    <v-row v-if="myEvents">
      <v-col cols="12" md="6" v-for="user in myEvents" :key="user.id">
        <v-card>
          <v-card-title>{{ user.eventId.eventName }}</v-card-title>
          <v-card-subtitle>{{ user.userId.username }}</v-card-subtitle>
          <v-card-text>
            {{ user.userId.first_name }} {{ user.userId.last_name }}: {{ user.userId.email }}
        </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
//   name: "MyEvents",
  data() {
    return {
      ownedEventsUsers: null,
      myEvents: null,
    }
  },
  computed: {
    events() {
        this.eventUsers.map(item => item.eventId)
    }
  },
  async asyncData({ $axios }) {
    let ownedData = await $axios.$get("/myOwnedEventUser/")
    let participantData = await $axios.$get("/myEventUser/")
    return {
        myEvents: participantData,
        ownedEventsUsers: ownedData
    }
  }
}
</script>

<style lang="scss" scoped>
</style>