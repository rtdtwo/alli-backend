from pickle import TRUE
from unittest import result
import da

def get_user(id):
    user=da.get_user(id)
    if user is not None:
        return {
            'code' : 200,
            'data' : user.to_dict()
        }
    else:
        return {
            'code' : 404,
            'msg' : 'No User found with ID {}'.format(id)
        }

def create_user(data):
    f_name = data['fName']
    l_name = data['lName']
    email = data['email']
    sex = data['sex']
    age = data['age']

    result = da.create_user(f_name,l_name,email,sex,age)

    if result[0]:
        return {
            'code' : 201,
            'msg' : 'User Created',
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
            'code' : 500,
            'msg'  :'Error: {}'.format(result[1])
        }

