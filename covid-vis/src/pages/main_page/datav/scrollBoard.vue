<template>
  <div id='scroll-board'>
    <dv-scroll-board :config='config' v-if='completed' style="width:1000px;height:1200px"/>
    <dv-loading v-if='loading'>Loading...</dv-loading>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ScrollBoard',
  data () {
    return {
      config: {
        header: ['标题', '内容', '来源'],
        data: [],
        index: true,
        columnWidth: [50, 300, 500, 150],
        align: ['center'],
        rowNum: 7,
        headerBGC: '#1981f6',
        headerHeight: 45,
        oddRowBGC: 'rgba(0, 44, 81, 0.8)',
        evenRowBGC: 'rgba(10, 29, 50, 0.8)'
      },
      loading: true,
      completed: false
    }
  },
  mounted () {
    this.getNews()
  },
  methods: {
    getNews () {
      axios
        .get('/news', {
          headers: {
            authoration: 'apicode',
            apicode: '2e5cda5ad3e14374bf59db91c877c3d3'
          }
        })
        .then(res => {
          // console.log(res);
          var news = res.data.newslist[0].news
          // console.log(news)
          for (var i = 0; i < news.length; i++) {
            // eslint-disable-next-line no-array-constructor
            var arr = new Array()
            // arr[0] = news[i].pubDateStr
            arr[0] =
              '<a href=' + news[i].sourceUrl + '>' + news[i].title + '</a>'
            arr[1] = news[i].summary
            arr[2] = news[i].infoSource
            this.config.data.push(arr)
          }
          this.loading = false
          this.completed = true
          this.config = { ...this.config }
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang='less'>
#scroll-board {
  width: 50%;
  box-sizing: border-box;
  height: 100%;
  overflow: hidden;
}
</style>
