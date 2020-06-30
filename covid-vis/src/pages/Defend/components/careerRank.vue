<template>
  <div>
    <div class='header'>疫情工作危险指数 TOP6</div>
    <dv-active-ring-chart :config='config' style='width:700px;height:700px' />
  </div>
</template>

<script>
export default {
  name: 'careerRank',
  data () {
    return {
      config: {
        radius: '70%',
        activeRadius: '65%',
        data: [
          {
            name: '医护人员',
            value: 84
          },
          {
            name: '清洁工人',
            value: 57
          },
          {
            name: '公交司机',
            value: 54
          },
          {
            name: '惩教人员',
            value: 42
          },
          {
            name: '急救人员',
            value: 25
          },
          {
            name: '零售服务人员',
            value: 66
          }
        ],
        digitalFlopStyle: {
          fontSize: 20,
          fill: 'white'
        },
        showOriginValue: true
      }
    }
  }
}
</script>

<style lang='less'>
.header {
  font-size: 50px;
  font-weight: bold;
  height: 40px;
  line-height: 30px;
}
</style>
