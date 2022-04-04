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
            'f_name' : self.f_name,
            'l_name' : self.l_name,
            'email'  : self.email,
            'sex'    : self.sex,
            'age'    : self.age
        }


User.createTable(ifNotExists=True)
