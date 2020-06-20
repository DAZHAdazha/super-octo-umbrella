<template>
  <div id="top-header">
    <dv-border-box-4 style="width:300px;height:100px;">
      <div class="infected" v-if="comming">全球感染人数:{{globalnumber}}</div>
      <div class="add" v-if="comming">昨日新增感染人数:{{globaladdnumber}}</div>
    </dv-border-box-4>
    <!-- <dv-decoration-8 style="width:300px;height:50px;" /> -->
    <dv-decoration-5 class="header-center-decoration" />
    <div class="center-title">实时疫情数据</div>
    <dv-border-box-4 style="width:300px;height:100px;" :reverse="true">
      <div class="infected" v-if="comming">国内感染人数:{{domesticnumber}}</div>
      <div class="add" v-if="comming">昨日新增感染人数:{{domesticaddnumber}}</div>
    </dv-border-box-4>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "TopHeader",
  data(){
    return{
      comming:false
    }
  },
  mounted() {
    this.getNews();
  },
  methods:{
    getNews(){
      axios
        .get("/api")
        .then(res => {
          // console.log(res);
          var response = res.data.data;
          this.comming=true;
          this.domesticnumber=response.gntotal;
          this.domesticaddnumber=response.add_daily.addcon_new;
          this.globalnumber=response.othertotal.certain;
          this.globaladdnumber=response.othertotal.certain_inc;
        })
        .catch(err => {
          console.log("fail");
        });
    }
  }
};
</script>

<style lang="less">
#top-header {
  position: relative;
  width: 100%;
  height: 100px;
  display: flex;
  justify-content: space-between;
  flex-shrink: 0;

  .header-center-decoration {
    width: 40%;
    height: 60px;
    margin-top: 30px;
  }

  .header-left-decoration,
  .header-right-decoration {
    width: 25%;
    height: 60px;
  }

  .center-title {
    position: absolute;
    font-size: 30px;
    font-weight: bold;
    left: 50%;
    top: 15px;
    transform: translateX(-50%);
  }

  .infected {
    position: absolute;
    width: 300px;
    font-size: 20px;
    font-weight: bold;
    left: 150px;
    top: 50px;
    transform: translateX(-50%);
  }

  .add{
    position: absolute;
    font-size: 20px;
    width: 300px;
    font-weight: bold;
    left: 150px;
    right: 100px;
    top: 20px;
    transform: translateX(-50%);
  }
}
</style>
