from flask_sqlalchemy import SQLAlchemy
from random import randint

db = SQLAlchemy()

class Family:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{
            "id": 1,
            "first_name": "John",
            "age": "25",
            "lucky_numbers": [1, 3],
            "last_name": self.last_name
        },

        {
            "id": 2,
            "first_name": "Alex",
            "age": "25",
            "lucky_numbers": [1, 7],
            "last_name": self.last_name
        },
          {
            "id": 3,
            "first_name": "Angel",
            "age": "25",
            "lucky_numbers": [1, 8, 0, 7],
            "last_name": self.last_name
        },
        
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)
        return self._members

    def delete_member(self, member_id):
        c = 0
        for i in self._members:
            if i['id'] == member_id:
                self._members.pop(c)
            c+=1    
        return self._members
        

    def update_member(self, member_id, body):
        for i in self._members:
            if i['id'] == member_id:
                self._members.append(body) 
        return self._members


        self._members = list(filter(lambda member: member['id']!=id, self._members))
        return None






    def get_member(self, id):
        member= next(filter(lambda member: member['id']==id,self._members),None)
        return member
    
    
    def get_all_members(self):
        names = []
        for i in self._members:
            names.append(i["first_name"])
        return names

    def sum(self):
        c = []
        for i in self._members:
            b = i["lucky_numbers"]
            c.append(sum(b))
        b = sum(c)   
        return b

    def concat(self):
        c = []
        for i in self._members:
            b = i["lucky_numbers"]
            c.append(b)
        return c