<template>
  <div id="logout">
    <h1>Logout page.</h1>
    <a href="javascript:" @click="logout">Logout</a>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      // alert(this.$store.state.isLogin)
      this.$store.commit('logout')
      // alert(this.$store.state.isLogin)
      // localStorage.removeItem('Flag')
    }
  }
}
</script>