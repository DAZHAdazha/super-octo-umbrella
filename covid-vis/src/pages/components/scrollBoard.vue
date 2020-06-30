<template>
  <div id='scroll-board'>
    <dv-scroll-board :config='config' v-if='completed' />
    <dv-loading v-if='loading'>Loading...</dv-loading>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ScrollBoard',
  data() {
    return {
      config: {
        header: ['内容', '来源'],
        data: [
          ['避免接触野生动物，不要捕食、贩卖、购买野味', '搜狐网'],
          ['打喷嚏或咳嗽时，不要直接用手捂住口鼻', '搜狐网'],
          ['人与人之间接触时，要保持1米以上的距离，尤其是面对面谈话时', '搜狐网'],
          ['不要随地吐痰', '搜狐网'],
          ['出行箱可随身携带含有酒精的消毒产品，酒精含量最好可以达到70%~80%', '搜狐网'],
          ['不去人群密集的地方', '搜狐网'],
          ['保持室内空气流通，避免到封闭、空气不流通的公众场合', '搜狐网'],
          ['乘坐电梯避免人员拥挤，人多时可等一等', '百度网']
        ],
        index: true,
        columnWidth: [100, 500, 150],
        align: ['center'],
        rowNum: 6,
        headerBGC: '#1981f6',
        headerHeight: 45,
        oddRowBGC: 'rgba(0, 44, 81, 0.8)',
        evenRowBGC: 'rgba(10, 29, 50, 0.8)',
        waitTime:1000
      },
      loading: false,
      completed: true
    };
  },
  mounted() {
    // this.getNews();
  },
  methods: {
    getNews() {
      axios
        .get('/news', {
          headers: {
            authoration: 'apicode',
            apicode: '2e5cda5ad3e14374bf59db91c877c3d3'
          }
        })
        .then(res => {
          // console.log(res);
          var news = res.data.newslist[0].news;
          console.log(news);
          for (var i = 0; i < news.length; i++) {
            var arr = new Array();
            arr[0] = news[i].pubDateStr;
            arr[1] =
              '<a href=' + news[i].sourceUrl + '>' + news[i].title + '</a>';
            arr[2] = news[i].infoSource;
            this.config.data.push(arr);
          }
          this.loading = false;
          this.completed = true;
          this.config = { ...this.config };
        })
        .catch(err => {
          console.log('Newsfail');
        });
    }
  }
};
</script>

<style lang='less'>
#scroll-board {
  width: 100%;
  box-sizing: border-box;
  margin-right: 10px;
  height: 100%;
  overflow: hidden;
}
</style>
