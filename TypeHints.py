from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None
    friends: List[int] = []


external_data = {'id': '123', 'signup_ts': '2020-02-20 10:00', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.dict())