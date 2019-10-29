<template>
  <div id="login">
    <h1>Login page.</h1>
    <a href="javascript:" @click="sendRequest">Login</a>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    data() {
      return {
        isAuthed: null
      }
    },
    methods: {
      sendRequest() {
        axios.get('http://127.0.0.1:8000/login', { params: { username: 'hgj', password: '123456'}})
        .then(res => {
          if (res.data.code === 0) {
            this.isAuthed = true
            localStorage.setItem('Flag', 'isLogin')
          } else {
            this.isAuthed = false
          }
        })
      }
    }
}
</script>

<style lang="">

</style>