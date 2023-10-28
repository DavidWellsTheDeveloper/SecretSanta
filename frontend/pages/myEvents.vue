<template>
    <v-container>
        <h1 class="page-title" style="margin-bottom: 20px;">Events for {{ $auth.user.first_name }} {{ $auth.user.last_name }}</h1>
            <!-- <NuxtLink to="/"> -->
            <v-card
                class="card-list"
                elevation="10"
                v-for="event in events"
                :key="event.eventId.id"
                width="50%"
            >
                <v-card-title
                    class="card-title"
                >
                    {{ event.eventId.eventName }}
                </v-card-title>
                <v-card-text
                    class="card-text"
                >

                    <b>Pairing Date:</b> {{ event.eventId.pairingDate }}
                </v-card-text>
            </v-card>
            <!-- </NuxtLink> -->
    </v-container>
</template>

<script>
    export default {
        data() {
            return {
                events: null
            }
        },
        mounted () {
            this.getMyEvents()
        },
        methods: {
            async getMyEvents() {
                try {
                    let response = await this.$axios.get('myEventUser')
                    this.events = response.data
                } catch (error) {
                    this.loginError = true
                    console.log(error)
                }
            },
        },
    }
</script>

<style lang="scss" scoped>
.card-text {
    margin-left: 25px;
}

.card-title {
    padding-bottom: 0px;
}

.card-list {
    margin-bottom: 15px;
    margin-left: 25px;
}
</style>