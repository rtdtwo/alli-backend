from flask import Flask, request, jsonify
import bl
import waitress

app = Flask(__name__)


@app.route('/user/<int:id>')
def get_user(id):
    result = bl.get_user(id)
    return jsonify(result), result['code']


@app.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data Provided'}), 400
    result = bl.signup(request.json)
    return jsonify(result), result['code']


@app.route('/goal', methods=['POST'])
def goal():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data Provided'}), 400

    result = bl.goal(request.json)
    return jsonify(result), result['code']


@app.route('/goal/<string:id>')
def get_goal(id):
    if id == 'all':
        user_id = request.args.get('userId')
        result = bl.get_goals_of_user(int(user_id))
    else:
        result = bl.get_goal(int(id))

    return jsonify(result), result['code']


if __name__ == '__main__':
    waitress.serve(app, host='0.0.0.0', port='4000')
