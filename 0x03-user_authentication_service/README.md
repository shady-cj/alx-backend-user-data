# 0x03-user_authentication_service


## TASKS


### 0. User model
mandatory
Score: 0.0% (Checks completed: 0.0%)
In this task you will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).

The model will have the following attributes:

* `id`, the integer primary key
* `email`, a non-nullable string
* `hashed_password`, a non-nullable string
* `session_id`, a nullable string
* `reset_token`, a nullable string

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$ 
```


**File**: `user.py`