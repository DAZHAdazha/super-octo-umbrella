<template>
  <div class="echarts">
    <div :style="{height:'400px',width:'100%'}" ref="myEchart"></div>
  </div>
</template>

<script>
import echarts from "echarts";
import Axios from "axios";
export default {
  name: "main_page",
  data: function() {
    return {
      days: [],
      province: [],
      data: []
    };
  },
  mounted: function() {
    this.getData();
  },
  methods: {
    init() {
      this.mycharts = echarts.init(this.$refs.myEchart);
      const option = {
        baseOption: {
          timeline: {
            axisType: "category",
            // realtime: false,
            // loop: false,
            autoPlay: false, // 自动播放
            playInterval: 2000,
            symbolSize: 12,
            left: "5%",
            right: "5%",
            bottom: "0%",
            width: "90%",
            // controlStyle: {
            //     position: 'left'
            // },
            data: this.days.reverse(),
            tooltip: {
              formatter: this.days
            }
          },
          tooltip: {
            show: true,
            formatter: function(params) {
              return params.name + "：" + params.data["value"];
            }
          },
          visualMap: {
            type: "piecewise",
            pieces: [
              {
                min: 1002,
                color: "#73240D"
              },
              {
                min: 501,
                max: 1001,
                color: "#BB0000"
              },
              {
                min: 251,
                max: 500,
                color: "#BD430A"
              },
              {
                min: 101,
                max: 250,
                color: "#E08150"
              },
              {
                min: 11,
                max: 100,
                color: "#E9B090"
              },
              {
                min: 1,
                max: 10,
                color: "#F2DDD2"
              },
              {
                value: 0,
                color: "white"
              }
            ],
            orient: "vertical",
            itemWidth: 25,
            itemHeight: 15,
            showLabel: true,
            seriesIndex: [0],

            textStyle: {
              color: "#7B93A7"
            },
            bottom: "10%",
            left: "5%"
          },
          grid: {
            right: "5%",
            top: "20%",
            bottom: "10%",
            width: "20%"
          },
          xAxis: {
            min: 0,
            max: 4000,
            show: false
          },
          yAxis: [
            {
              inverse: true,
              offset: "2",
              type: "category",
              data: "",
              nameTextStyle: {
                color: "#fff"
              },
              axisTick: {
                show: false
              },
              axisLabel: {
                //rotate:45,
                textStyle: {
                  fontSize: 14,
                  color: "#000000"
                },
                interval: 0
              },
              axisLine: {
                show: false,
                lineStyle: {
                  color: "#333"
                }
              },
              splitLine: {
                show: false,
                lineStyle: {
                  color: "#333"
                }
              }
            }
          ],
          geo: {
            map: "china",
            right: "35%",
            left: "5%",
            label: {
              emphasis: {
                show: false
              }
            },
            itemStyle: {
              emphasis: {
                areaColor: "#2F95FA"
              }
            }
          },
          series: [
            {
              name: "mapSer",
              type: "map",
              map: "china",
              roam: false,
              geoIndex: 0,
              label: {
                show: false
              }
            },
            {
              name: "",
              type: "bar",
              zlevel: 2,
              barWidth: "40%",
              label: {
                normal: {
                  show: true,
                  fontSize: 14,
                  position: "right",
                  formatter: "{c}"
                }
              }
            }
          ]
        },
        animationDurationUpdate: 3000,
        animationEasingUpdate: "quinticInOut",
        options: []
      };
      for (var n = this.days.length - 1; n >= 0; n--) {
        var res = [];
        for (j = 0; j < data[n].length; j++) {
          res.push({
            name: province[j],
            value: data[n][j]
          });
        }
        res
          .sort(function(a, b) {
            return b.value - a.value;
          })
          .slice(0, 6);

        res.sort(function(a, b) {
          return a.value - b.value;
        });
        var res1 = [];
        var res2 = [];
        for (t = 0; t < 10; t++) {
          res1[t] = res[res.length - 1 - t].name;
          res2[t] = res[res.length - 1 - t].value;
        }
        option.options.push({
          title: [
            {
              text: this.days[n] + "日  " + news[n],
              textStyle: {
                color: "#2D3E53",
                fontSize: 28
              },
              left: 20,
              top: 20
            },
            {
              show: true,
              text: "感染人数前十的省份",
              textStyle: {
                color: "#2D3E53",
                fontSize: 18
              },
              right: "10%",
              top: "15%"
            }
          ],
          yAxis: {
            data: res1
          },
          series: [
            {
              type: "map",
              data: res
            },
            {
              type: "bar",
              data: res2,
              itemStyle: {
                normal: {
                  color: function(params) {
                    // build a color map as your need.
                    var colorList = [
                      {
                        colorStops: [
                          {
                            offset: 0,
                            color: "#FF0000" // 0% 处的颜色
                          },
                          {
                            offset: 1,
                            color: "#990000" // 100% 处的颜色
                          }
                        ]
                      },
                      {
                        colorStops: [
                          {
                            offset: 0,
                            color: "#00C0FA" // 0% 处的颜色
                          },
                          {
                            offset: 1,
                            color: "#2F95FA" // 100% 处的颜色
                          }
                        ]
                      }
                    ];
                    if (params.dataIndex < 3) {
                      return colorList[0];
                    } else {
                      return colorList[1];
                    }
                  }
                }
              }
            }
          ]
        });
      }
      this.mycharts.setOption(option);
    },
    getData() {
      this.$http.get("static/mock/main_page.json").then(
        Response => {
          console.log(Response);
          var resdata = Response.body;
          this.days = resdata.days;
          this.province = resdata.province;
          this.data = resdata.data;
          console.log(this.province);
        },
        error => {
          console.log("Wrong");
        }
      );
      // 使用刚指定的配置项和数据显示图表。
      this.init();
    }
  }
};
</script>

<style>
</style>
