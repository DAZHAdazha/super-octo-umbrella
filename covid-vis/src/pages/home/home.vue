<template>
  <div>
    <h1>home testing</h1>

    <div>{{data}}</div>
  </div>

</template>

<script>
import axios from 'axios'
import echarts from 'echarts'

export default {
  name: 'name',
  data () {
    return {
      data: {}
    }
  },
  methods: {

    getData () { // 用于获取新浪API上的数据;
      axios.get('/api')
        .then(response => {
          this.data = response.data
        })
    }
  },
  mounted () {
    this.getData()
  }
}
</script>

<style scoped>

</style>
