<template>
  <div id="app">
    <router-link to="/register">注册</router-link>
    <router-link to="/login">登录</router-link>
    <router-link to="/lr">测试</router-link>
    <router-link to="/logout">注销</router-link>
    <router-view></router-view>
  </div>
  
</template>

<script>


export default {
  name: 'app',
  components: {
  }
}
</script>

<style>
</style>
