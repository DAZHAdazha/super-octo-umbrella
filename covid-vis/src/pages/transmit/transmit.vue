<template>

<div id='data-view'>
    <dv-full-screen-container>

    <div class="leftContent">

          <simulation></simulation>

    </div>
        <div class="rightContent">

        </div>

    </dv-full-screen-container>
    
  </div>
</template>

<script>

import simulation from "./components/simulation";

export default {
  name: "transmit",
  components: {

    simulation
  }
};
</script>

<style lang="less">
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
    display: flex;
    flex-direction: row;
  }

  .leftContent{
    width: 60%;
  }

  .rightContent{
    width: 35%;
    margin-left: 1%;
  }
}
</style>
