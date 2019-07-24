content = '''
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="main" style="height:300px;"></div>
<script type="text/javascript">
var myChart = echarts.init(document.getElementById('main'));
var option = {
    backgroundColor: '#F5F5F5', //背景色
    title: {
        text: '测试统计数据',
        x: 'center'
    },
    legend: {
        orient: 'vertical',
        x: 'left',
        data: ['成功', '错误', '跳过']
    },
    color: ['#3c763d', '#FF4000', '#0099CC'],
    calculable: true,
    series: [{
        name: '测试结果',
        type: 'pie',
        radius: '55%',
        center: ['50%', '60%'],
        startAngle: 135,
        data: [{
            value: {{success_case_sum}},
            name: '成功',
            itemStyle: {
                normal: {
                    label: {
                        formatter: '{b} : {c} ({d}%)',
                        textStyle: {
                            align: 'left',
                            fontSize: 15,
                        }
                    },
                    labelLine: {
                        length: 40,
                    }
                }
            }
        }, {
            value: {{errors_case_sum}},
            name: '错误',
            itemStyle: {
                normal: {
                    label: {
                        formatter: '{b} : {c} ({d}%)',
                        textStyle: {
                            align: 'right',
                            fontSize: 15,
                        }
                    },
                    labelLine: {
                        length: 40,
                    }
                }
            }
        }, {
            value: {{skipped_case_sum}},
            name: '跳过',
            itemStyle: {
                normal: {
                    label: {
                        formatter: '{b} : {c} ({d}%)',
                        textStyle: {
                            align: 'right',
                            fontSize: 15,
                        }
                    },
                    labelLine: {
                        length: 40,
                    }
                }
            }
        }],
    }]
};
// 为echarts对象加载数据
myChart.setOption(option);
</script>
'''


def get_chart_tpl():
    return content


if __name__ == '__main__':
    print(get_chart_tpl())
