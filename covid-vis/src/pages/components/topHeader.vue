<template>
  <div id='top-header'>
    <dv-border-box-4 style='width:300px;height:90px;'>
      <div class='infected' v-if='comming'>全球感染人数:{{globalnumber}}</div>
      <div class='add' v-if='comming'>昨日新增感染人数:{{globaladdnumber}}</div>
    </dv-border-box-4>
    <!-- <dv-decoration-8 style='width:300px;height:50px;' /> -->
    <dv-decoration-5 class='header-center-decoration' />
    <div class='center-title'>疫情大数据平台</div>
    <dv-border-box-4 style='width:300px;height:90px;' :reverse='true'>
      <div class='infected' v-if='comming'>国内感染人数:{{domesticnumber}}</div>
      <div class='add' v-if='comming'>昨日新增感染人数:{{domesticaddnumber}}</div>
      <div class='menu'>
        <a-dropdown :overlayStyle="{color: '#08c'}">
          <a class='ant-dropdown-link' @click='e => e.preventDefault()'>
            <a-icon type='menu' :style="{ fontSize: '30px', color: '#08c' }" />
          </a>
          <a-menu slot='overlay'>
            <a-menu-item>
              <router-link to='/main'>实时数据</router-link>
            </a-menu-item>
            <a-menu-item>
              <router-link to='/news'>舆情分析</router-link>
            </a-menu-item>
            <a-menu-item>
              <router-link to='/popular'>疫情回顾</router-link>
            </a-menu-item>
            <a-menu-item>
              <router-link to='/transmit'>疫情警惕</router-link>
            </a-menu-item>
            <a-menu-item>
              <router-link to='/defend'>新冠防范</router-link>
            </a-menu-item>
          </a-menu>
        </a-dropdown>
      </div>
    </dv-border-box-4>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TopHeader',
  data () {
    return {
      comming: false
    }
  },
  mounted () {
    this.getNews()
  },
  methods: {
    getNews () {
      axios
        .get('/api')
        .then(res => {
          // console.log(res);
          var response = res.data.data
          // console.log(response)
          this.comming = true
          this.domesticnumber = response.gntotal
          this.domesticaddnumber = response.add_daily.addcon_new
          this.globalnumber = response.othertotal.certain
          this.globaladdnumber = response.othertotal.certain_inc
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang='less'>
#top-header {
  position: relative;
  width: 100%;
  height: 70px;
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
    font-size: 16px;
    font-weight: bold;
    left: 200px;
    top: 45px;
    transform: translateX(-50%);
  }

  .add {
    position: absolute;
    font-size: 16px;
    width: 300px;
    font-weight: bold;
    left: 200px;
    right: 200px;
    top: 20px;
    transform: translateX(-50%);
  }

  .menu {
    position: absolute;
    right: 20px;
    top: 30px;
    width: 20px;
  }
}
</style>
