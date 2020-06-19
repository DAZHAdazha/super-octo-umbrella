<template>
  <div id="ranking-board">
    <div class="ranking-board-title">感染人数排名</div>
    <dv-scroll-ranking-board :config="config" />
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "RankingBoard",
  data() {
    return {
      config: {
        data: [],
        rowNum: 9
      }
    };
  },
  mounted() {
    this.getNews();
  },
  methods: {
    getNews() {
      axios
        .get("/globalrank")
        .then(res => {
          // console.log(res);
          var response = res.data;
          // console.log(response);
          for(var i=0;i<response.length;i++){
            this.config.data.push({name:response[i].country,value:response[i].cases})
          }
          console.log(this.config.data);
          this.config = { ...this.config };
        })
        .catch(err => {
          console.log("fail");
        });
    }
  }
};
</script>

<style lang="less">
#ranking-board {
  width: 20%;
  box-shadow: 0 0 3px blue;
  display: flex;
  flex-direction: column;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, 0.5);
  box-sizing: border-box;
  padding: 0px 20px;

  .ranking-board-title {
    // font-weight: bold;
    padding-top: 10px;
    padding-left: 50px;
    height: 50px;
    width: 100px;
    // display: flex;
    align-items: center;
    font-size: 15px;
  }

  .dv-scroll-ranking-board {
    flex: 1;
  }
}
</style>
