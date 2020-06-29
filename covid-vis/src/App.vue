<template>
  <div id="app">
    <dv-full-screen-container>
      <top-header></top-header>
      <router-view/>
    </dv-full-screen-container>
  </div>
</template>

<script>

import topHeader from './pages/components/topHeader'
export default {
  name: 'App',
  components: {
    topHeader
  }
}
</script>

<style>

#dv-full-screen-container {
  width: 100%;
  height: 100%;
  background-color: #030409;
  color: #fff;
  background-image: url("./pages/components/img/bg.png");
  background-size: 100% 100%;
  box-shadow: 0 0 3px blue;
  display: flex;
  flex-direction: column;
}

#app{
  width: 100%;
  display: flex;
  flex-direction:row;
  justify-content: center
}
</style>
