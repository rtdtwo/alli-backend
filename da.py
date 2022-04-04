import model


def get_user(id):
    users = list(model.User.selectBy(id=id))
    if len(users) > 0:
        return users[0]
    else:
      return None

def get_user_by_email(email):
    users = list(model.User.selectBy(email=email))
    if len(users) > 0:
        return users[0]
    else:
      return None


def create_user(f_name, l_name, email, sex, age):
    existing_user = get_user_by_email(email)
    if existing_user is not None:
        print('User already exists, skipping create')
        return (True, existing_user.id)
    else:
        try:
            new_user = model.User(
                f_name=f_name,
                l_name=l_name,
                email=email,
                sex=sex,
                age=age
            )

            new_user.set()

            existing_user = get_user_by_email(email)
            if existing_user is not None:
                return (True, existing_user.id)
            else:
                return (False, 'An Error Occurred')
        except Exception as e:
            return (False, e)