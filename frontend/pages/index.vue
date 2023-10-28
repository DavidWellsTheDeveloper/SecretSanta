<template>
  <v-container>
    <h1>Home Page</h1>
  </v-container>
</template>

<script>
import Login from "~/components/Login.vue"

export default {
  auth: false,
  name: "index",
  data() {
    return {
      
    }
  },
  methods: {
    
  },
  head() {
    return {
      title: "Home",
      meta: [
        {
          hid: "description",
          name: "description",
          content: "Home Page",
        },
      ],
    };
  },
};
</script>
