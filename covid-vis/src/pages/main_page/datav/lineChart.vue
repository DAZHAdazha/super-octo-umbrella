<template>
  <div class='line-container'>
    <div id='lineChart'></div>
  </div>
</template>

<script>
import echarts from 'echarts'

export default {
  name: 'lineChart',
  props: {
    history: Array
  },
  data () {
    return {
      option: {
        color: ['#DC143C', '#40E0D0', '#808080'],
        title: {
          text: '全国疫情历史折线图',
          textStyle: {
            color: 'white'
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross'
          }
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
          data: ['全国感染人数', '全国治愈人数', '全国死亡人数'],
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
            name: '全国感染人数',
            type: 'line',
            data: [],
            areaStyle: {
            }
          },
          {
            name: '全国治愈人数',
            type: 'line',
            data: [],
            areaStyle: {}
          },
          {
            name: '全国死亡人数',
            type: 'line',
            data: [],
            areaStyle: {}
          }
        ]
      }
    }
  },
  mounted () {
    // var myLineChart = echarts.init(document.getElementById('lineChart'))
    // myLineChart.setOption(JSON.parse(JSON.stringify(this.option)), true)
  },
  watch: {
    history (newData, oldData) {
      this.history = newData
      this.history.forEach(element => {
        this.option.xAxis.data.unshift(element.date)
        this.option.series[0].data.unshift(element.cn_conNum)
        this.option.series[1].data.unshift(element.cn_cureNum)
        this.option.series[2].data.unshift(element.cn_deathNum)
        // console.log()
      })
      var myLineChart = echarts.init(document.getElementById('lineChart'))
      myLineChart.setOption(JSON.parse(JSON.stringify(this.option)), true)
    }
  }
}
</script>

<style scoped>
#lineChart {
  width: 600px;
  height: 400px;
}
</style>
