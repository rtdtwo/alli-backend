from flask import Flask, request, jsonify
from flask_cors import CORS
import bl
import waitress

app = Flask(__name__)
CORS(app)


@app.route('/health_check')
def health_check():
    return jsonify({'code': 200, 'msg': 'The force is strong with this one!'}), 200


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


@app.route('/social/profile/<int:id>')
def get_social_profile(id):
    result = bl.get_social_profile(id)
    return jsonify(result), result['code']


@app.route('/social/profile', methods=['POST'])
def create_social_profile():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data Provided'}), 400
    result = bl.create_social_profile(request.json)
    return jsonify(result), result['code']


@app.route('/social/group', methods=['POST'])
def create_social_group():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data Provided'}), 400

    result = bl.create_social_group(request.json)
    return jsonify(result), result['code']


@app.route('/social/group/<int:id>/posts')
def get_posts_of_group(id):
    social_id = request.args.get('socialId', None)
    type = request.args.get('type', None)
    result = bl.get_posts_of_group(id, type, int(social_id))
    return jsonify(result), result['code']


@app.route('/social/post', methods=['POST'])
def create_social_post():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data Provided'}), 400
    result = bl.create_social_post(request.json)
    return jsonify(result), result['code']


@app.route('/social/post/<int:id>/likeUnlike', methods=['PUT'])
def like_unlike_social_post(id):
    social_id = request.args.get('socialId', None)
    result = bl.like_unlike_social_post(id, int(social_id))
    return jsonify(result), result['code']


@app.route('/social/group/<int:group_id>/joinOrLeave', methods=['PUT'])
def join_or_leave_group(group_id):
    social_id = request.args.get('socialId', None)
    result = bl.join_or_leave_group(group_id, int(social_id))
    return jsonify(result), result['code']


@app.route('/social/groups')
def get_social_groups():
    social_id = request.args.get('socialId', None)
    result = bl.get_social_groups(int(social_id), 'all')
    return jsonify(result), result['code']


@app.route('/social/profile/<int:id>/groups')
def get_social_groups_of_profile(id):
    result = bl.get_social_groups(id, 'profile')
    return jsonify(result), result['code']

@app.route('/mood', methods = ['POST'])
def create_mood():
    if not request.is_json:
        return jsonify({'code': 400, 'msg': 'No data Provided'}), 400
    result = bl.create_mood(request.json)
    return jsonify(result), result['code']
    
@app.route('/mood/<int:user_id>')
def get_mood(user_id):
    date = request.args.get('date', 'all')
    if date == 'all':
        result = bl.get_moods_of_user(user_id)
    else:
        result = bl.get_mood(user_id, date)

    return jsonify(result), result['code']


if __name__ == '__main__':
    waitress.serve(app, host='0.0.0.0', port='4000')
    # app.run(host='0.0.0.0', port='4000')
