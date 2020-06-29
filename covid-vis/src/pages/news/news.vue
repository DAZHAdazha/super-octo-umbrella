<template>
  <div id='data-view'>
    <dv-full-screen-container>
      <top-header />
      <div class='main-content'>
        <!-- <digital-flop /> -->
        <div class='leftContent'>
          <searchArea></searchArea>
        </div>
        <div class='rightContent'>
          <sideBar></sideBar>
        </div>
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>
import topHeader from '../components/topHeader'
import searchArea from './components/searchArea'
import sideBar from './components/sideBar'
export default {
  name: 'news',
  components: {
    topHeader,
    searchArea,
    sideBar
  }
}
</script>

<style lang='less'>
#data-view {
  width: 100%;
  height: 100%;
  background-color: #030409;
  color: #fff;

  #dv-full-screen-container {
    background-image: url('../components/img/bg.png');
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
