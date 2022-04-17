import json
import da

from sqlobject import *

from sqlobject.sqlite import builder
conn = builder()('database.db')


class User(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = conn

    f_name = StringCol()
    l_name = StringCol()
    email = StringCol()
    social_id = BigIntCol()
    sex = IntCol()
    age = IntCol()

    def to_dict(self):
        social_profile = da.get_social_profile(self.id)
        d = {
            'id': self.id,
            'fName': self.f_name,
            'lName': self.l_name,
            'email': self.email,
            'sex': self.sex,
            'age': self.age,
            'socialProfile': None
        }

        if social_profile is not None:
            d['socialProfile'] = social_profile.to_dict()

        return d

class Goal(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = conn

    event_name = StringCol()
    deadline = BigIntCol()
    user_id = BigIntCol()

    def to_dict(self):
        return {
            'userId': self.user_id,
            'eventName': self.event_name,
            'deadline': self.deadline,
            'id': self.id
        }

# SOCIAL MEDIA

class SocialProfile(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = conn

    user_id = BigIntCol()
    bio = StringCol()
    nickname = StringCol()

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'bio': self.bio
        }


class SocialPost(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = conn

    created_by = BigIntCol()
    created_at = BigIntCol()
    content = StringCol()
    anonymous = BoolCol()
    likes = StringCol()
    group_id = BigIntCol()

    def to_dict(self, asker_id):
        likes = json.loads(self.likes)
        return {
            'id': self.id,
            'content': self.content,
            'createdAt': self.created_at,
            'anonymous': self.anonymous,
            'createdBy': da.get_social_profile(self.created_by).to_dict(),
            'likes': len(likes),
            'likedByAsker': asker_id in likes
        }

class SocialGroup(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = conn

    name = StringCol()
    description = StringCol()
    created_by = BigIntCol()
    created_at = BigIntCol()
    tags = StringCol()
    members = StringCol()

    def to_dict(self, asker_id):
        members = json.loads(self.members)
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'createdAt': self.created_at,
            'tags': json.loads(self.tags),
            'members': len(members),
            'askerAMember': asker_id in members
        }

#MOOD

class Mood(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = conn

    user_id = BigIntCol()
    mood = StringCol()
    date = StringCol()

    def to_dict(self):
        return{
            'id' : self.id,
            'userId': self.user_id,
            'mood' : self.mood,
            'date' : self.date
        }


#Abstinenece


class Abstinence(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    _connection = conn

    user_id = BigIntCol()
    addiction = StringCol()
    start_time = BigIntCol()

    def to_dict(self):
        return{
            'id' : self.id,
            'userId': self.user_id,
            'addiction' : self.addiction,
            'startTime' : self.start_time
        }

User.createTable(ifNotExists=True)
Goal.createTable(ifNotExists=True)
SocialProfile.createTable(ifNotExists=True)
SocialGroup.createTable(ifNotExists=True)
SocialPost.createTable(ifNotExists=True)
Mood.createTable(ifNotExists=True)
Abstinence.createTable(ifNotExists=True)

    

