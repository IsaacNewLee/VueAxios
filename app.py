import json
from flask import Flask, request, redirect, Response

# app = Flask(__name__,template_folder="templates",static_folder="staticccc",static_url_path='/vvvvv')
app = Flask(__name__, )


@app.route('/')
def login():
    if request.method == 'GET':
        resp = Response("<h2>首页<h2>")
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp


# 默认get请求
@app.route('/course')
def index():
    resp = Response(json.dumps({
        "name": "alex"
    }))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return redirect('/login')


@app.route("/create", methods=["post", ])
def create():
    print(request.form.get("name"))

    with open("user.json", "r") as f:
        # 反序列化
        data = json.loads(f.read())

    data.append({"name": request.form.get("name")})

    with open("user.json", "w") as f:
        f.write(json.dumps(data))

    resp = Response(json.dumps(data))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == '__main__':
    app.run()
