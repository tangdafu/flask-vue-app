from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET','POST'])
def ping_pong():
    data = request.get_json(silent=True)
    #app.logger.info(data['text'])
    return jsonify(data)



@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/<path:fallback>')
def fallback(fallback):  # Vue Router 的 mode 为 'hash' 时可移除该方法
    if fallback.startswith('css/') or fallback.startswith('js/') \
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()