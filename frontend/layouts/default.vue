<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :expand-on-hover="$vuetify.breakpoint.mdAndUp"
      :permanent="$vuetify.breakpoint.mdAndUp"
      app
      dark
      color="primary"
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in itemsCommon"
          :key="i"
          :to="item.to"
          :color="activeLinkColor"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click="toggleDarkTheme()">
          <v-list-item-action>
            <v-icon>
              {{
                $vuetify.theme.dark ? 'mdi-brightness-5' : 'mdi-weather-night'
              }}
            </v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Change Theme</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
      </v-list>

      <v-list v-show="$auth.loggedIn">
        <v-list-item
          v-for="(item, i) in itemsLoggedIn"
          :key="i"
          :to="item.to"
          :color="activeLinkColor"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click="logout()">
          <v-list-item-action>
            <v-icon>mdi-account-circle</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list v-show="!$auth.loggedIn">
        <v-list-item
          v-for="(item, i) in itemsNotLoggedIn"
          :key="i"
          :to="item.to"
          :color="activeLinkColor"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar v-if="$vuetify.breakpoint.smAndDown" clipped-left app>
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title>{{ title }}</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <nuxt />
    </v-main>
    <v-footer app>
      <span>&copy; Secret Santa {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      title: 'Secret Santa',
      drawer: false,
      fixed: false,
      itemsCommon: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/',
        },
      ],
      itemsLoggedIn: [
        {
          icon: 'mdi-cart-variant',
          title: 'Create Event',
          to: '/CreateEvent',
        },
        {
          icon: 'mdi-text-box-multiple',
          title: 'My Events',
          to: '/MyEvents',
        },
      ],
      itemsNotLoggedIn: [
        {
          icon: 'mdi-account-circle',
          title: 'Login',
          to: '/login',
        },
        {
          icon: 'mdi-account-check-outline',
          title: 'Register',
          to: '/register',
        },
      ],
      activeLinkColor: 'secondary',
    }
  },
  methods: {
    logout() {
      this.$auth.logout()
      this.$router.push({ name: 'login' })
    },
    toggleDarkTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark
    },
  },
  head() {
    return {
      title: 'Secret Santa',
      titleTemplate: 'Secret Santa | %s',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'Secret Santa is the last Secret Santa app you\'ll ever need.',
        },
      ],
    }
  },
}
</script>