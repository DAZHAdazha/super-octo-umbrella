<template>
  <div>
    <a-timeline id="timeLine">
      <a-timeline-item  v-for="item in items" :key="item.message" :style="{color:'white'}">{{item.message}}</a-timeline-item>
    </a-timeline>
  </div>
</template>

<script>
export default {
  name: 'timeline',
  data () {
    return {
      items: [
        { message: '武汉卫健委发布紧急通知 2019/12/30' },
        { message: '国家卫健委抵达武汉正式介入调查 2019/12/31' },
        { message: '华南海鲜市场关停 2020/1/1' },
        { message: '中科院武汉病毒所获得新冠病毒序列 2020/1/2' },
        { message: '武汉卫健委通报44例“不明肺炎”，未见明显人传人' },
        { message: '明确病原体为“冠状病毒” 2020/1/9' },
        {
          message:
            '前后武汉当地医院床位爆满，“疑似患者”激增，有医护被传染（三联报道）2020/1/10'
        },
        { message: '未发现新增病例；出现首个死亡案例；2020/1/11 ' },
        {
          message: '世界卫生组织正式将病毒命名为"2019新型冠状病毒" 2020/1/12'
        },
        {
          message:
            '世界卫生组织（WHO）以及武汉卫健委报告称“没有证据显示人传人“ 2020/1/14 '
        },
        {
          message:
            '武汉官方通报指出“有限度人传人”；武汉文旅局：春节文化惠民活动启动；2020/1/17'
        },
        {
          message:
            '武汉百步亭社区举办万家宴，数万人参与；钟南山专家组进驻武汉；2020/1/18'
        },
        { message: '武汉市疾病预防控制中心主任李刚：疫情可防可控；2020/1/19' },
        { message: '武汉卫健委通报18、19 新增136名患者；2020/1/20' },
        {
          message:
            '钟南山在接受央视新闻直播采访时表示新型冠状病毒肺炎是肯定的人传人；武汉实施进出管制；2020/1/21 '
        },
        {
          message:
            '中国国家卫健委承认已经出现人传人及医务人员感染，病毒存在变异可能；2020/1/22 '
        }
      ]
    }
  }
}
</script>

<style scoped>
#timeLine {
  margin-right: 40%;
  margin-top: 5%;
}
</style>
