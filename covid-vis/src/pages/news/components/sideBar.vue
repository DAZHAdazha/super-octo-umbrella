<template>
  <div id="sideBar">
    <div class="header">新闻实时搜索关键词热度</div>
    <dv-capsule-chart :config="config" style="width:350px;height:400px" />
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'sideBar',
  data () {
    return {
      config: {
        data: [],
        colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
        unit: '热度',
        showValue: true
      }
    }
  },
  mounted () {
    this.getBaiudu()
  },
  methods: {
    up (x, y) {
      return -x.ratio + y.ratio
    },
    getBaiudu () {
      axios
        .get('/baidu', {
          headers: {
            Pragma: 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            Accept:
              'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
          }
        })
        .then(res => {
          // console.log(res);
          var list = res.data.data.wordlist[0].wordGraph
          list.sort(this.up)
          // console.log(list);
          for (var i = 1; i < 10; i++) {
            this.config.data.push({ name: list[i].word, value: list[i].ratio })
          }
          this.config = { ...this.config }
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
#sideBar {
  box-sizing: border-box;
  box-shadow: 0 0 3px blue;
}
.header {
  margin-top: 20px;
  font-size: 25px;
  font-weight: bold;
  height: 30px;
  line-height: 30px;
}
</style>
