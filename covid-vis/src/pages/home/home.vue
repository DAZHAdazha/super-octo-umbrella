<template>
  <div>
    <h1>当日新增</h1>
    <div>{{times}}</div>
    <div class="main-container">
      <div id='main' style='width: 1000px;height:800px;'></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import echarts from 'echarts'
import china from 'echarts/map/json/china.json'

echarts.registerMap('china', china) // 注册对应的地图;

export default {
  name: 'name',
  data () {
    return {
      times: '',
      list: [],
      test: {},
      option: {
        tooltip: {
          triggerOn: 'click',
          formatter: function (e, t, n) {
            return e.value === 0.5
              ? e.name + '：有疑似病例'
              : e.seriesName + '<br />' + e.name + '：' + e.value
          }
        },
        visualMap: {
          min: 0,
          max: 1000,
          left: 26,
          bottom: 40,
          showLabel: !0,
          text: ['高', '低'],
          pieces: [
            {
              gt: 100,
              label: '> 100 人',
              color: '#7f1100'
            },
            {
              gte: 10,
              lte: 100,
              label: '10 - 100 人',
              color: '#ff5428'
            },
            {
              gte: 1,
              lt: 10,
              label: '1 - 9 人',
              color: '#ff8c71'
            },
            {
              gt: 0,
              lt: 1,
              label: '疑似',
              color: '#ffd768'
            },
            {
              value: 0,
              color: '#ffffff'
            }
          ],
          show: !0
        },
        geo: {
          map: 'china',
          roam: !1,
          scaleLimit: {
            min: 1,
            max: 2
          },
          zoom: 1.23,
          top: 120,
          label: {
            normal: {
              show: !0,
              fontSize: '14',
              color: 'rgba(0,0,0,0.7)'
            }
          },
          itemStyle: {
            normal: {
              // shadowBlur: 50,
              // shadowColor: 'rgba(0, 0, 0, 0.2)',
              borderColor: 'rgba(0, 0, 0, 0.2)'
            },
            emphasis: {
              areaColor: '#f2d5ad',
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              borderWidth: 0
            }
          }
        },
        series: [
          {
            name: '确诊病例',
            type: 'map',
            geoIndex: 0,
            data: []
          }
        ]
      }
    }
  },
  methods: {
    getData () {
      // 用于获取新浪API上的数据;
      axios.get('/api').then(response => {
        this.times = response.data.data.times

        response.data.data.list.forEach(element => {
          this.option.series[0].data.push({name: element.name, value: parseInt(element.econNum)})
        })

        var myChart = echarts.init(document.getElementById('main'))
        let tempOption = JSON.parse(JSON.stringify(this.option))
        myChart.setOption(tempOption)
      })
    }
  },
  mounted () {
    this.getData()
  }
}
</script>

<style scoped>
.main-container{
  display: flex;
  justify-content: center;
  width: 1200px;
  height: 1000px;
  background-color: rgba(3, 105, 142, 0.292);
  border-radius: 50px;
}

#main{
  position: relative;
  top: 70px;
}
</style>
