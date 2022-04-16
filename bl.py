import json
import da


def get_user(id):
    user = da.get_user(id)
    if user is not None:
        return {
            'code': 200,
            'data': user.to_dict()
        }
    else:
        return {
            'code': 404,
            'msg': 'No User found with ID {}'.format(id)
        }


def signup(data):
    f_name = data['fName']
    l_name = data['lName']
    email = data['email']
    sex = data['sex']
    age = data['age']

    result = da.signup(f_name, l_name, email, sex, age)

    if result[0]:
        return {
            'code': 201,
            'msg': 'User Created',
            'data': result[1].to_dict()
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }


def goal(data):
    event_name = data['eventName']
    deadline = data['deadline']
    user_id = data['userId']

    result = da.goal(user_id, event_name, deadline)

    if result[0]:
        return {
            'code': 201,
            'msg': 'Goal Created',
            'data': {
                'user_id': user_id,
                'eventName': event_name,
                'deadline': deadline,
            }
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }


def get_goal(id):
    goal = da.get_goal(id)
    if goal is not None:
        return {
            'code': 200,
            'data': goal.to_dict()
        }
    else:
        return {
            'code': 404,
            'msg': 'No goal with ID {} exists'.format(id)
        }


def get_goals_of_user(user_id):
    goals = da.get_goals_of_user(user_id)

    return {
        'code': 200,
        'data': [goal.to_dict() for goal in goals]
    }


def create_social_group(data):
    name = data['name']
    description = data['description']
    created_by = data['createdBy']
    tags = data['tags']

    result = da.create_social_group(name, description, created_by, tags)

    if result[0]:
        return {
            'code': 201,
            'msg': 'Group Created'
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }


def get_social_profile(id):
    result = da.get_social_profile(id)
    if result is not None:
        return {'code': 200, 'data': result.to_dict()}
    else:
        return {'code': 404, 'msg': 'Profile not found'}


def create_social_profile(data):
    user_id = data['userId']
    nickname = data['nickname']
    bio = data['bio']

    result = da.create_social_profile(user_id, nickname, bio)

    if result[0]:
        return {
            'code': 201,
            'msg': 'Profile Created',
            'data': da.get_user(user_id).to_dict()
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }


def get_posts_of_group(group_id, type, social_id):
    if type == 'all':
        posts = da.get_all_posts_of_group(group_id)
    else:
        posts = da.get_posts_of_group_by_social_id(group_id, social_id)

    return {'code': 200, 'data': [post.to_dict(social_id) for post in posts]}


def create_social_post(data):
    created_by = data['userId']
    content = data['content']
    anonymous = data['anonymous']
    group_id = data['groupId']

    result = da.create_social_post(created_by, content, anonymous, group_id)

    if result[0]:
        return {
            'code': 201,
            'msg': 'Post Created'
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }


def like_unlike_social_post(post_id, social_id):
    if social_id is None:
        return {
            'code': 400,
            'msg': 'No social ID provided'
        }

    result = da.like_unlike_social_post(post_id, social_id)
    if result[0]:
        return {
            'code': 200,
            'msg': 'Post Liked or Unliked',
            'data': result[1].to_dict(social_id)
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }


def join_or_leave_group(group_id, social_id):
    if social_id is None:
        return {
            'code': 400,
            'msg': 'No social ID provided'
        }
        
    result = da.join_or_leave_group(group_id, social_id)
    if result[0]:
        return {
            'code': 200,
            'msg': 'Group Joined or Left',
            'data': result[1].to_dict(social_id)
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }


def get_social_groups(social_id, type):
    if social_id is None:
        return {'code': 400, 'msg': 'No social ID provided'}
    groups = da.get_all_social_groups()
    if type == 'all':
        result = [group.to_dict(social_id) for group in groups]
    else:
        user_groups = []
        for group in groups:
            if social_id in json.loads(group.members):
                user_groups.append(group)

        result = [group.to_dict(social_id) for group in user_groups]

    return {'code': 200, 'data': result}


def create_mood(data):
    user_id = data['userId'] 
    mood = data['mood']
    date = data['date']

    result = da.create_mood(user_id, mood, date)

    if result[0]:
        return {
            'code': 201,
            'msg': 'Mood created',
            'data': {
                'user_id': user_id,
                'mood': mood,
                'date': date,
            }
        }
    else:
        return {
            'code': 500,
            'msg': 'Error: {}'.format(result[1])
        }
    
def get_mood(user_id, date):
    mood = da.get_mood(user_id, date)
    if mood is not None:
        return {
            'code': 200,
            'data': mood.to_dict()
        }
    else:
        return {
            'code': 404,
            'msg': 'No mood with ID {} exists'.format(user_id, date)
        }


def get_moods_of_user(user_id):
    moods = da.get_moods_of_user(user_id)

    return {
        'code': 200,
        'data': [mood.to_dict() for mood in moods]
    }