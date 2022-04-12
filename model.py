import email
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
    sex = IntCol()
    age = IntCol()
    def to_dict(self):
        return {
            'id' : self.id,
            'f_name' : self.f_name,
            'l_name' : self.l_name,
            'email'  : self.email,
            'sex'    : self.sex,
            'age'    : self.age
        }


User.createTable(ifNotExists=True)

class Goal(SQLObject):
    class sqlmeta:
        lazyUpdate = True
        
    _connection = conn

    event_name = StringCol()
    deadline = BigIntCol()
    user_id = BigIntCol()
    
    def to_dict(self):
        return {
            'userId' : self.user_id, 
            'eventName' : self.event_name,
            'deadline' : self.deadline,
            'id' : self.id
        }
   
Goal.createTable(ifNotExists=True)
 




#  {
#     "fName": "Srikanth Rao",
#     "lName": "Parcha",
#     "age": 21,
#     "sex": 0,
#     "email": "parcha.srikanthr@ufl.edu"
# }


# {
#     "userId" : 1,
#     "eventName" : "marriage",
#     "deadline" : 1651107708
# }