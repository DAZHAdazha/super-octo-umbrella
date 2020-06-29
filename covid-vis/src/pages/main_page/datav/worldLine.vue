<template>
  <div class='line-container'>
    <div id='worldLineChart'></div>
  </div>
</template>

<script>
import echarts from 'echarts'

export default {
  name: 'lineChart',
  props: {
    worldHistory: Array
  },
  data () {
    return {
      worldOption: {
        color: ['#DC143C', '#40E0D0', '#808080'],
        title: {
          text: '世界疫情历史折线图',
          textStyle: {
            color: 'white'
          }
        },
        tooltip: {
          trigger: 'axis'
        },
        dataZoom: [
          {
            startValue: '01.22'
          },
          {
            type: 'inside'
          }
        ],
        legend: {
          data: ['全球感染人数', '全球治愈人数', '全球死亡人数'],
          top: 30,
          textStyle: {
            color: 'white'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: [],
          axisLine: {
            lineStyle: {
              color: '#fff'
            }
          }
        },
        yAxis: {
          type: 'value',
          axisLine: {
            lineStyle: {
              color: '#fff'
            }
          }
        },
        series: [
          {
            name: '全球感染人数',
            type: 'line',
            data: [],
            areaStyle: {}
          },
          {
            name: '全球治愈人数',
            type: 'line',
            data: [],
            areaStyle: {}
          },
          {
            name: '全球死亡人数',
            type: 'line',
            data: [],
            areaStyle: {}
          }
        ]
      }
    }
  },
  watch: {
    worldHistory (newData, oldData) {
      console.log(newData)
      this.worldHistory = newData
      this.worldHistory.forEach(element => {
        this.worldOption.xAxis.data.unshift(element.date)
        this.worldOption.series[0].data.unshift(element.certain)
        this.worldOption.series[1].data.unshift(element.recure)
        this.worldOption.series[2].data.unshift(element.die)
        // console.log()
      })
      var myLineChart = echarts.init(document.getElementById('worldLineChart'))
      myLineChart.setOption(JSON.parse(JSON.stringify(this.worldOption)), true)
    }
  }
}
</script>

<style scoped>
#worldLineChart {
  width: 600px;
  height: 400px;
}
</style>
