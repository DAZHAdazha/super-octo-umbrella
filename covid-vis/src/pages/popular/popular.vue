<template>
  <div class="popular-main">
    <line-chart :history="history"></line-chart>
    <world-line :worldHistory="worldHistory"></world-line>
  </div>
</template>

<script>
import lineChart from '../main_page/datav/lineChart'
import worldLine from '../main_page/datav/worldLine'
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
    worldLine
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
.popular-main{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  position: relative;
  top: 100px
}
</style>
