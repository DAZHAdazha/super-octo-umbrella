<template>
  <div id="sideBar">
    <div class="header">新闻实时搜索关键词热度</div>
    <dv-capsule-chart :config="config" style="width:350px;height:400px" />
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "sideBar",
  data() {
    return {
      config: {
        data: [],
        colors: ["#e062ae", "#fb7293", "#e690d1", "#32c5e9", "#96bfff"],
        unit: "热度",
        showValue: true
      }
    };
  },
  mounted() {
    this.getBaiudu();
  },
  methods: {
    up(x,y){
      return -x.ratio+y.ratio;
    },
    getBaiudu() {
      axios
        .get("/baidu", {
          headers: {
            Host: "index.baidu.com",
            Connection: "keep-alive",
            Pragma: "no-cache",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
            Accept:
              "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            Referer: "http://index.baidu.com/v2/main/index.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            Cookie:
              'BAIDUID=18D82A8B17EDAA6DD0D6EA47ED2FE0A1:FG=1; BIDUPSID=5223638718BFADAFB98437BF597D1963; PSTM=1590899692; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1455_32124_21115_32139_31660_32046_32107_26350; indexpro=4v28geg6mepffpvm6liilvqs83; CHKFORREG=bdaa8ae70de9be4bd1d9e2352e772a1b; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1592879962,1592920401,1592920508; BDUSS=WQ2S3ozWEJGSXhhVW5PM1JCRFI0OGh4RmFVRXl5bTgxY3NnRUVBLUFITERyeGxmSVFBQUFBJCQAAAAAAAAAAAEAAADbUCmlYmluZ25vaQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMMi8l7DIvJeT; bdindexid=puu5q12qtq5vipmeqng42u0671; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1592973717; delPer=0; PSINO=3; ZD_ENTRY=baidu; BCLID=9492458164013148787; BDSFRCVID=upIOJeC62ZouP0buPTrSjIDXfmOfq8jTH6aoF0963UOyS6N2fev9EG0PeM8g0KubqVK_ogKKLmOTHp0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJ4q_IPMJK_3qR5gMJ5q-n3HKUrL5t_XbI6y3JjOHJOoDDvgMURcy4LdjG5C0nFDXbvt-PJX3JczOMnGD6jBht-X3-Aq54RaXaQeKlKKKKJ6ElcL-ltBQfbQ0M6uqP-jW5TaaJ6D-n7JOpvshfnxybOQQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6IHtbuO_DLbJIvDqTrP-trf5DCShUFsKDrrB2Q-XPoO3KO8OM7h5tt20Jkqyt7v-RcPW6Lf2MbgylRp8P3y0bb2DUA1y4vpWJT0W2TxoUJ2fnRJEUcG-4QWXUIebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hCP6DTKBD6OM5pJfeJcXfRFOVTrJabC3JxKzXU6qLT5XKxJgXP5abCvIXIT_WlnifJj5W-RJhp0njxQyKbJU5I-f-fjaLqQU8nb6BUonDh8ebG7MJUntKHTXKbnO5hvv8b6O3M72DMKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJj8qJn-j_K_Q-J5fjtoN-n8_KPFD-xLX-PoyKD6ysJOOaCviSlvOy4oTj6DFMGb-t-jtBjrbLbcYWUnhh4cqMboK3MvB-fPebJoa5HALXnQ1MqcAhtbDQft20-IIeMtjBbQaWDjhQn7jWhvdDq72yb02QlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDq6FftbPDoCv5b-0_JtjmDTDhq4tehHRtbUc9WDTm_Doua-5mhboG0hOK0PIPQb7h2xRh-RbB-pPKKR7PhKICDpoc2qJBXG5hKRK83mkjbn5zfn02OP5PKqjvBP4syPRr2xRnWT4jKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8ZD6Dajj5P; RT="sl=0&ss=kbsvf5dn&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=eqfo0u01ygk&ul=9ar5k"'
          }
        })
        .then(res => {
          console.log(res);
          var list = res.data.data.wordlist[0].wordGraph;
          list.sort(this.up);
          console.log(list);
          for (var i = 1; i < 10; i++) {
            this.config.data.push({name:list[i].word,value:list[i].ratio});
          }
          this.config = { ...this.config };
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style>
#sideBar {
  box-sizing: border-box;
  box-shadow: 0 0 3px blue;
}
.header {
  font-size: 25px;
  font-weight: bold;
  height: 30px;
  line-height: 30px;
}
</style>