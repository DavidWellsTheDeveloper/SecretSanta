<template>
    <div>
        <v-container>
            <v-card width="400" class="mx-auto mt-5">
                <v-card-title>
                    <h1 class="display-1 mx-auto">Login</h1>
                </v-card-title>
                <v-card-text>
                    <v-form id="login-form" v-model="valid" @submit.prevent="loginUser">
                        <v-text-field
                        id="username-field"
                        v-model="login.username"
                        label="username"
                        :rules="rules_username"
                        prepend-icon="mdi-account-circle"
                        ></v-text-field>
                        <v-text-field
                        id="password-field"
                        v-model="login.password"
                        label="password"
                        :rules="rules_password"
                        prepend-icon="mdi-lock"
                        :type="showPassword ? 'text' : 'password'"
                        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="showPassword = !showPassword"
                        ></v-text-field>
                        <v-row>
                            <v-col>
                                <v-btn color="info" :disabled="!valid" type="submit">
                                    Login
                                </v-btn>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-btn type="link" small text to="/Register" color="error">
                                    Need an account? Register.
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-form>
                </v-card-text>
                <v-alert v-if="loginError" dense text type="error">
                    {{ loginErrorMessage }}
                </v-alert>
            </v-card>
            <v-card>
                <v-card-title class="headline text-center">
                    Welcome {{ $auth.loggedIn }}
                </v-card-title>
            </v-card>
        </v-container>

    </div>
</template>

<script>
    export default {
        auth: false,
        name: "Login",
        data() {
            return {
                valid: false,
                rules_username: [(value) => !!value || "Required"],
                rules_password: [(value) => !!value || "Required"],
                showPassword: false,
                login: {
                    username: "",
                    password: "",
                },
                loginError: false,
                loginErrorMessage:
                "Something went wrong when logging in. Check your Username & Password, and try again.",
            };
        },
        computed: {
            auth() {
                return this.$auth
            }
        },
        methods: {
            loginUser() {
                this.performLogin()
                this.redirectAfterLogin()
            },

            async performLogin() {
                this.loginError = false
                try {
                    let response = await this.$auth.loginWith('local', { data: this.login })
                } catch (error) {
                    this.loginError = true
                    console.log(error)
                }
            },

            redirectAfterLogin() {
                this.$router.push({ name: 'index' })
            }
        },
        head() {
            return {
                title: 'Login',
                meta: [
                    {
                        hid: 'description',
                        name: 'description',
                        content: 'Login to manage your own recipes, food, and ingredients',
                    },
                ],
            }
        },
    }
</script>

<style lang="scss" scoped>

</style>