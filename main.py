from crypt import methods
from unittest import result
from flask import Flask, request, jsonify
import bl

app = Flask(__name__)


@app.route('/user/<int:id>')
def get_user(id):
    result = bl.get_user(id)
    return jsonify(result), result['code']


@app.route('/user',methods=['POST'])
def create_user():
    if not request.is_json:
        return jsonify({'code': 400 ,'msg':'No data Provided'}), 400

    result=bl.create_user(request.json)
    return jsonify(result), result['code']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)