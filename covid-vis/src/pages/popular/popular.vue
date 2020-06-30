<template>
  <div id='main'>
    <div class='popular-main'>
      <line-chart :history='history'></line-chart>
      <world-line :worldHistory='worldHistory'></world-line>
    </div>
    <div class='right'>
      <timeline></timeline>
    </div>
  </div>
</template>

<script>
import lineChart from '../main_page/datav/lineChart'
import worldLine from '../main_page/datav/worldLine'
import timeline from './components/timeline'
import axios from 'axios'
export default {
  name: 'popular',
  data () {
    return {
      history: [],
      worldHistory: []
    }
  },
  components: {
    lineChart,
    worldLine,
    timeline
  },
  methods: {
    getData () {
      axios.get('/api').then(response => {
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

<style scoped>
#main{
  display: flex;
  flex-direction: row;
  top: 100px;
}
.popular-main {
  width: 60%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
}
.right{
  margin-left: 3%;
}
</style>
