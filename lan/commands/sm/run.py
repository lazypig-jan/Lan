import json
from flask import Flask, render_template
from lan import Config, Monitor

app = Flask(__name__)
# 初始化config
cf = Config()


@app.route("/")
def index():
    return render_template("index.html", port=cf.get('port'))


@app.route("/get_data")
def get_data():
    m = Monitor()
    return json.dumps(m.get_info(), ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=cf.get('port'))
