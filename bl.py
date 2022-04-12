from pickle import TRUE
from unittest import result
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
            'data': {
                'id': result[1],
                'fName': f_name,
                'lName': l_name,
                'email': email,
                'sex': sex,
                'age': age,
            }
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
