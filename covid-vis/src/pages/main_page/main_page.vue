<template>
  <div id='data-view'>
    <dv-full-screen-container>
      <top-header />

      <div class='main-content'>
        <!-- <digital-flop /> -->

        <div class='block-left-right-content'>
          <ranking-board/>
          <!-- 疫情排名 -->
          <div class="chart-container">
            <rose-chart :china="china" :world="world" :jwsr="jwsr"></rose-chart>
            <!-- <rose-circle :jwsr="jwsr"></rose-circle> -->

            <!-- <button
              @click="switchChart"
              style="width: 200px;
                     color: black"
            >
              {{butText}}
            </button>
            <line-chart :history="history" v-show="chartShow"></line-chart>
            <world-line :worldHistory="worldHistory" v-show="!chartShow"></world-line> -->

          </div>
          <!-- 地图模块 -->
          <!-- <water-level-chart /> -->
          <scroll-board />
        </div>
      </div>
    </dv-full-screen-container>
  </div>
</template>

<script>
import axios from 'axios'
import topHeader from '../components/topHeader'
// import digitalFlop from './datav/digitalFlop'
import rankingBoard from './datav/rankingBoard'
import roseChart from './datav/roseChart'
// import waterLevelChart from './datav/waterLevelChart'
import scrollBoard from './datav/scrollBoard'
// import cards from './datav/cards'
import roseCircle from './datav/roseCircle'
import lineChart from './datav/lineChart'
import worldLine from './datav/worldLine'

export default {
  name: 'main_page',
  components: {
    topHeader,
    // digitalFlop,
    rankingBoard,
    roseChart,
    // waterLevelChart,
    scrollBoard,
    roseCircle,
    lineChart,
    worldLine
    // cards
  },
  data () {
    return {
      china: [], // 中国地图数据
      world: [], // 世界地图数据
      jwsr: [], // 中国境外新增数据
      history: [], // 中国历史数据
      worldHistory: [], // 世界历史数据
      chartShow: true,
      butText: '切换为世界疫情历史'
    }
  },
  methods: {
    switchChart () {
      this.chartShow = !this.chartShow
      this.butText = this.chartShow ? '切换为世界疫情历史' : '切换为中国疫情历史'
    },
    getData () {
      axios.get('/api').then(response => {
        this.china = response.data.data.list
        this.world = response.data.data.worldlist
        this.jwsr = response.data.data.jwsrTop
        this.history = response.data.data.historylist
        this.worldHistory = response.data.data.otherhistorylist
      })
    }
  },
  mounted () {
    this.getData()
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
    display: flex;
    flex-direction: row;
    height: 100%;
  }

  .block-left-right-content {
    flex: 1;
    display: flex;
    margin-top: 20px;
    height: 100%;
  }

  .chart-container {
    width: 600px;
    display: flex;
    flex-direction: column;
    background-color: rgba(6, 30, 93, 0.5);
    border-top: 2px solid rgba(1, 153, 209, .5);
    box-sizing: border-box;
  }

}
</style>
