<template>
  <v-container>
    <h1>Home Page</h1>
  </v-container>
</template>

<script>

export default {
  // User does not need to be authenticated for this page
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
