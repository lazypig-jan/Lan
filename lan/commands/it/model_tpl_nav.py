content = '''
<ul class="nav nav-tabs">
    {% for item in datas %}
    <li {% if loop.index == 1 %} class="active" {% endif %}>
        <a href="#panel-{{loop.index}}" data-toggle="tab" style="Background-Color: {{item.bg}}; color: #fff;">{{item.text}} ( {{item.num}} )</a>
    </li>
    {% endfor %}
</ul>
'''


def get_nav_tpl():
    return content


if __name__ == '__main__':
    print(get_nav_tpl())
