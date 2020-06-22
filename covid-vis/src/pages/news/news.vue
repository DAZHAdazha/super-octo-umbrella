<template>
  <div id="data-view">
    <dv-full-screen-container>
      <top-header />
      <div class="main-content">
        <!-- <digital-flop /> -->
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>
import axios from "axios";
import topHeader from "../components/topHeader";
export default {
  name: "news",
  components: {
    topHeader
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
    flex: 1;
    display: flex;
    flex-direction: column;
  }


}
</style>