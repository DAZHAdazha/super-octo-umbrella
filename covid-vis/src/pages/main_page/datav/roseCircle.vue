<template>
  <div class="container">
    <div id='roseCircle' style='width: 100px;height:100px;'></div>
    <div class="item-container">
      <!-- <div class="item" v-for="(item,index) in jwsr" :key="index">{{item.name}} : {{item.jwsrNum}}</div> -->
    </div>
  </div>
</template>

<script>
import echarts from 'echarts'

export default {
  name: 'roseCircle',
  props: {
    jwsr: Array
  },
  watch: {
    jwsr (newData, oldData) {
      this.jwsr = newData
      // console.log(JSON.parse(JSON.stringify(this.jwsr)))
      this.jwsr.forEach(element => {
        this.option.series[0].data.push({value: parseInt(element.jwsrNum), name: element.name})
      })
      var myRose = echarts.init(document.getElementById('roseCircle'))
      myRose.setOption(JSON.parse(JSON.stringify(this.option)))
      // }}
    }
  },
  data () {
    return {
      option: {
        // backgroundColor: '#2c343c',
        title: {
          text: '国内境外输入病例排名',
          left: 'center',
          top: 20,
          textStyle: {
            color: '#ccc'
          }
        },

        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },

        visualMap: {
          show: false,
          min: 30,
          max: 500,
          inRange: {
            colorLightness: [0.8, 0.2]
          }
        },
        series: [
          {
            name: '访问来源',
            type: 'pie',
            radius: '55%',
            center: ['50%', '50%'],
            data: [
            ].sort(function (a, b) {
              return a.value - b.value
            }),
            roseType: 'angle',
            label: {
              normal: {
                textStyle: {
                  color: 'black'
                }
              }
            },
            labelLine: {
              normal: {
                lineStyle: {
                  color: 'black'
                },
                smooth: 0.2,
                length: 10,
                length2: 20
              }
            },
            itemStyle: {
              normal: {
                color: '#DC143C',
                shadowBlur: 200,
                shadowColor: 'rgba(0, 0, 0, 0.05)'
              }
            }
          }
        ]
      }
    }
  }
}
</script>

<style scoped>
.container{
  width: 100px;
  height: 100px;
  display: flex;
  flex-direction: row;
  justify-content: space-around
}

.item-container{
  position: relative;
  top: 100px;
}

.item{
  margin: 20px;
  font-size: 20px;
}
</style>
