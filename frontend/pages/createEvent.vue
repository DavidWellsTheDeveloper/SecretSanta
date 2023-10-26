<template>
  <v-container>
    <v-card class="justify-center" max-width="900">
      <v-form v-model="valid" @submit.prevent="onSubmit">
        <v-card-title>Create Event</v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="form.name"
                label="Event name"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="6">
              <v-date-picker
                v-model="form.eventDate"
                elevation="15"
                color="green lighten-1"
              ></v-date-picker>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
            <v-btn :color="valid? 'green': 'red'" text :disabled="!valid" type="submit">Submit</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import moment from "moment";
export default {
  data() {
    return {
      valid: false,
      form: {
        name: "",
        eventDate: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
          .toISOString()
          .substr(0, 10),
      },
    };
  },
  methods: {
    onSubmit() {

    }
  },
};
</script>

<style lang="scss" scoped>
</style>