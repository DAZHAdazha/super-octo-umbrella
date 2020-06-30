<template>
  <div id="data-view">
    <dv-full-screen-container>
      <top-header />
      <div class="main-content">
        <div class="leftContent">
            <scroll-board></scroll-board>
        </div>
        <div class="rightContent">
            <career-rank></career-rank>
        </div>
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>
import topHeader from "../components/topHeader";
import careerRank from "./components/careerRank";
import scrollBoard from "../components/scrollBoard";
export default {
  name: "defend",
  components: {
    topHeader,
    careerRank,
    scrollBoard
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

  .leftContent {
    margin-left: 2%;
    width: 70%;
  }

  .rightContent {
    width: 27%;
    margin-left: 2%;
  }
}
</style>