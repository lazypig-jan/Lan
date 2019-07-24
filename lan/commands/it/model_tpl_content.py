content = '''
{% for item in datas %}
{% set lp1 = loop %}
<div class="tab-pane {% if loop.index == 1 %} active {% endif %}" id="panel-{{lp1.index}}">
    <table class="table table-hover table-bordered">
       <tr class="all">
         {% for v in titles %}
         <td class="text-center" style="Background-Color:#dff0d8">{{v.text}}</td>
         {% endfor %}
       </tr>

       {% for v in item.list %}
        {% set lp2 = loop %}
       <tr class="all">
         {% for vv in titles %}
           {% if vv.name == 'case_id' %}
            <td class="text-center">{{loop.index}}</td>
           {% endif %}
           {% if vv.name == 'case_name' %}
            <td class="text-center">{{v.name}}</td>
           {% endif %}
           {% if vv.name == 'api_url' %}
            <td class="text-center">{{v.url}}</td>
           {% endif %}
            {% if vv.name == 'method' %}
            <td class="text-center">{{v.mode}}</td>
           {% endif %}
           {% if vv.name == 'time' %}
            <td class="text-center">{{v.time}}</td>
           {% endif %}
           {% if vv.name == 'result' %}
            <td class="text-center">{{v.status}}</td>
           {% endif %}
           {% if vv.name == 'detailed' %}
            <td class="text-center">
                <a href="javascript:showClassDetail('panel-{{lp1.index}}-detail-{{lp2.index}}','panel-{{lp1.index}}-hidden-{{lp2.index}}', '{{v.status_type}}')" class="detail" id = "panel-{{lp1.index}}-detail-{{lp2.index}}">详细</a>
            </td>
           {% endif %}
         {% endfor %}
       </tr>
        {% for vv in titles %}
            {% if vv.name == 'detailed' %}
                <tr class='hiddenRow' id="panel-{{lp1.index}}-hidden-{{lp2.index}}" >
                   <td colspan='7'><div><pre class="text-left">{{v.msg}}</pre></div></td>
                </tr>
            {% endif %}
        {% endfor %}

       {% endfor %}
    </table>
</div>
{% endfor %}
'''


def get_content_tpl():
    return content


if __name__ == '__main__':
    print(get_content_tpl())
