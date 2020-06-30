<template>
<div id='data-view'>
    <dv-full-screen-container>
    <topHeader></topHeader>
    <div class="left">
          <simulation></simulation>
    </div>
        <div class="right">
          <searchArea></searchArea>
        </div>
    </dv-full-screen-container>
  </div>
</template>
<script>

import simulation from './components/simulation'
import topHeader from '../components/topHeader'
import searchArea from './components/searchArea'

export default {
  name: 'transmit',
  components: {
    topHeader,
    simulation,
    searchArea
  }
}
</script>

<style scoped lang="less">
#data-view {
  width: 100%;
  height: 100%;
  background-color: #030409;
  color: #fff;

  #dv-full-screen-container {
    background-image: url("../components/img/bg.png");
    background-size: 100% 100%;
    box-shadow: 0 0 3px blue;
    display: flex;
    flex-direction: column;
  }

  .main-content {
    margin-top: 30px;
    flex: 1;
    display: block;
    flex-direction: row;
  }

  .left{
    position: absolute;
    width: 55%;
    left:5%;
    top: 10%;
  }

  .right{
    position: absolute;
    top: 8%;
    width: 35%;
    right: 5%;

  }
}
</style>
