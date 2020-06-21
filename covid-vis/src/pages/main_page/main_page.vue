<template>
  <div id="data-view">
    <dv-full-screen-container>

      <top-header />

      <div class="main-content">
        <!-- <digital-flop /> -->

        <div class="block-left-right-content">
          <ranking-board />
          <!-- 疫情排名 -->

          <div class="block-top-bottom-content">
            <div class="block-top-content">
              <rose-chart />
              <!-- 地图模块 -->

              <!-- <water-level-chart /> -->

              <scroll-board />
              <!-- 新闻模块 -->
            </div>

            <!-- <cards /> -->
          </div>
        </div>
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>
import topHeader from '../components/topHeader'
import digitalFlop from './datav/digitalFlop'
import rankingBoard from './datav/rankingBoard'
import roseChart from './datav/roseChart'
import waterLevelChart from './datav/waterLevelChart'
import scrollBoard from './datav/scrollBoard'
import cards from './datav/cards'

export default {
  name: 'main_page',
  components: {
    topHeader,
    // digitalFlop,
    rankingBoard,
    roseChart,
    // waterLevelChart,
    scrollBoard,
    // cards
  },
  data () {
    return {
    }
  },
  methods: {
  },
  mounted () {
    this.getData()
  }
}
</script>

<style lang="less">
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
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  .block-left-right-content {
    flex: 1;
    display: flex;
    margin-top: 20px;
  }

  .block-top-bottom-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    padding-left: 20px;
  }

  .block-top-content {
    height: 55%;
    display: flex;
    flex-grow: 0;
    box-sizing: border-box;
    padding-bottom: 20px;
  }
}
</style>
