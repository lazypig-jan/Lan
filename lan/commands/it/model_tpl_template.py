content = '''
<!doctype html>
<html>
<head>
    <title>{{title}}</title>
    <meta charset="UTF-8">
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>

    <!-- 引入 echarts.js -->
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts-all-3.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>

    <style type="text/css" media="screen">
        body {
            margin: 0;
            font-family: "Arial", "Microsoft YaHei", "黑体", "宋体", sans-serif;
            font-size: 18px;
            line-height: 1.5;
            line-height: 1.5;
            color: #333333;
        }

        .table {
            margin-bottom: 1px;
            width: 100%;
        }

        .hiddenRow {
            display: none;
        }

        .container-fluid {
            padding-right: 120px;
            padding-left: 120px;
        }

        .nav-tabs li {
            width: 186px;
            text-align: center;
        }
    </style>
    <script type="text/javascript">
      function showClassDetail(detail_id, hiddenRow_id, class_type) {
          console.log(document.getElementById(hiddenRow_id).className)

          if ('详细' ==  document.getElementById(detail_id).innerText) {
              if ('all' == class_type) {
                  document.getElementById(hiddenRow_id).className = 'all';
              }
              else if ('success' == class_type) {
                  document.getElementById(hiddenRow_id).className = 'success';
              }
              else if ('error' == class_type) {
                  document.getElementById(hiddenRow_id).className = 'error';
              }
              else if ('fail' == class_type) {
                  document.getElementById(hiddenRow_id).className = 'fail';
              }
              else{
                  document.getElementById(hiddenRow_id).className = 'untreaded';
              }
              document.getElementById(detail_id).innerText = "收起"
          }
          else {
              document.getElementById(detail_id).innerText = "详细"
              document.getElementById(hiddenRow_id).className = 'hiddenRow';
          }
      }
    </script>
</head>

<body>
    <div class="container-fluid">
        <div class="page-header">
            <h1 class="text-primary" style="font-size:45px;line-height:75px">{{title}}</h1>
        </div>

        <div class="col-md-12">
            <div class="col-md-4" style="Background-Color:#F5F5F5;">
                <h3 style="line-height:25px">测试基本信息</h3>
                <table class="table table-hover table-bordered" style="width:100% height:11px">
                    <tbody>
                        <tr class="info">
                            <td class="text-center">开始时间</td>
                            <td class="text-center">{{start_time}}</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">结束时间</td>
                            <td class="text-center">{{end_time}}</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">测试用时</td>
                            <td class="text-center">11 分 4 秒</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">总用例数</td>
                            <td class="text-center">{{all_case_sum}}</td>
                        </tr>
                        <tr class="info">
                            <td class="text-center">跳过用例数</td>
                            <td class="text-center">{{skipped_case_sum}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="col-md-8">
                {{chart_html}}
            </div>
        </div>

        <div class="col-md-12"><span style="display: block;height: 40px;"></span></div>

        <div class="col-md-12">
            <div class="tabbable">
                {{nav_html}}
            </div>
            <div class="tab-content">
                {{content_html}}
            </div>
        </div>

    </div>
</body>
</html>

'''


def get_template_tpl():
    return content


if __name__ == '__main__':
    print(get_template_tpl())
