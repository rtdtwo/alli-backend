from calendar import c
from datetime import date
import json
import model
import time


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


def signup(f_name, l_name, email, sex, age):
    existing_user = get_user_by_email(email)
    if existing_user is not None:
        print('User already exists, skipping create')
        return (True, existing_user)
    else:
        try:
            new_user = model.User(
                f_name=f_name,
                l_name=l_name,
                email=email,
                sex=sex,
                age=age,
                social_id=0,
            )

            new_user.set()

            existing_user = get_user_by_email(email)
            if existing_user is not None:
                return (True, existing_user)
            else:
                return (False, 'An Error Occurred')
        except Exception as e:
            return (False, e)


def goal(user_id, event_name, deadline):
    try:
        new_goal = model.Goal(
            event_name=event_name,
            deadline=deadline,
            user_id=user_id
        )
        new_goal.set()
        return (True, None)
    except Exception as e:
        return (False, e)


def get_goal(id):
    goal = list(model.Goal.selectBy(id=id))
    if len(goal) > 0:
        return goal[0]
    else:
        return None


def get_goals_of_user(user_id):
    return list(model.Goal.selectBy(user_id=user_id))


def create_social_group(name, description, user, tags):
    try:
        new_group = model.SocialGroup(
            name=name,
            description=description,
            created_by=user,
            created_at=time.time(),
            tags=json.dumps(tags),
            members=json.dumps([user])
        )
        new_group.set()
        return (True, None)
    except Exception as e:
        return (False, e)


def get_social_profile_by_user_id(user_id):
    profiles = list(model.SocialProfile.selectBy(user_id=user_id))
    if len(profiles) > 0:
        return profiles[0]
    else:
        return None


def get_social_profile(id):
    profiles = list(model.SocialProfile.selectBy(id=id))
    if len(profiles) > 0:
        return profiles[0]
    else:
        return None


def get_social_profile_by_user_id(user_id):
    profiles = list(model.SocialProfile.selectBy(user_id=user_id))
    if len(profiles) > 0:
        return profiles[0]
    else:
        return None


def create_social_profile(user_id, nickname, bio):
    try:
        new_profile = model.SocialProfile(
            user_id=user_id,
            bio=bio,
            nickname=nickname
        )
        new_profile.set()

        new_profile = get_social_profile_by_user_id(user_id)
        if new_profile is not None:
            user = get_user(user_id)
            if user is not None:
                user.social_id = new_profile.id
                user.syncUpdate()
            else:
                return (False, 'Could not update user: No such user')
        else:
            return (False, 'Profile not created for unknown reasons')

        return (True, new_profile.id)
    except Exception as e:
        return (False, e)


def get_all_posts_of_group(group_id):
    return list(model.SocialPost.selectBy(group_id=group_id))


def get_posts_of_group_by_social_id(group_id, social_id):
    return list(model.SocialPost.selectBy(group_id=group_id, created_by=social_id))


def get_post_by_id(id):
    posts = list(model.SocialPost.selectBy(id=id))
    if len(posts) > 0:
        return posts[0]
    else:
        return None


def create_social_post(created_by, content, anonymous, group_id):
    try:
        new_post = model.SocialPost(
            created_by=created_by,
            created_at=time.time(),
            content=content,
            anonymous=anonymous,
            likes=json.dumps([created_by]),
            group_id=group_id
        )

        new_post.set()

        return (True, None)
    except Exception as e:
        return (False, e)


def like_unlike_social_post(post_id, social_id):
    try:
        post = get_post_by_id(post_id)
        if post is None:
            return (False, 'No such post')

        likes = json.loads(post.likes)

        if social_id in likes:
            likes.remove(social_id)
        else:
            likes.append(social_id)

        post.likes = json.dumps(likes)

        post.syncUpdate()

        return (True, post)
    except Exception as e:
        return (False, e)


def get_group_by_id(id):
    groups = list(model.SocialGroup.selectBy(id=id))
    if len(groups) > 0:
        return groups[0]
    else:
        return None


def join_or_leave_group(group_id, social_id):
    try:
        group = get_group_by_id(group_id)
        if group is None:
            return (False, 'No such group exists')
        members = json.loads(group.members)
        if social_id in members:
            members.remove(social_id)
        else:
            members.append(social_id)
        group.members = json.dumps(members)
        group.syncUpdate()
        return (True, group)
    except Exception as e:
        return (False, e)


def create_mood(user_id, mood, date):
    try:
        moods = list(model.Mood.selectBy(user_id=user_id, date=date))
        if len(moods) > 0:
            existing_mood = moods[0]
            existing_mood.mood = mood
            existing_mood.syncUpdate()
            return (True, None)
        else:
            new_mood = model.Mood(
                user_id=user_id,
                mood=mood,
                date=date
            )
            new_mood.set()
            return True, None
    except Exception as e:
        return (False, e)


def get_all_social_groups():
    return list(model.SocialGroup.select())


def get_mood(user_id, date):
    mood = list(model.Mood.selectBy(user_id=user_id, date=date))
    if len(mood) > 0:
        return mood[0]
    else:
        return None


def get_moods_of_user(user_id):
    return list(model.Mood.selectBy(user_id=user_id))


def create_abstinence(user_id, addiction):
    try:
        new_abstinenece = model.Abstinence(
            user_id=user_id,
            addiction=addiction,
            start_time=time.time()
        )
        new_abstinenece.set()
        return (True, None)
    except Exception as e:
        return (False, e)


def get_abstinence_of_user(user_id):
    return list(model.Abstinence.selectBy(user_id=user_id))


def reset_abstinence(id):
    abstinence = list(model.Abstinence.selectBy(id=id))
    try:
        if len(abstinence) > 0:
            abstinence_to_reset = abstinence[0]
            abstinence_to_reset.start_time = time.time()
            abstinence_to_reset.syncUpdate()
            return (True, None)
        else:
            return (False, 'No abstinence with this ID')
    except Exception as e:
        return (False, e)
