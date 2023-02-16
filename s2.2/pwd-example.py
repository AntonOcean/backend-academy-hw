import base64
import hashlib
import bcrypt

# register https POST
# login - anton99
# password - password1

# --> hash(password) -> db_password = hash

# login https POST
# login - anton99
# password - password1
# compare hash(password1) == db_password

# hash + salt

# user_password = "password"
#
# # env/vault
# secret = "my secret key"
# salt = bcrypt.gensalt(rounds=5)
#
# print(len(salt))
#
# user_password = user_password + secret
#
# db_password = bcrypt.hashpw(user_password.encode(), salt)
#
# print(db_password)
#
# print()
# print(db_password[:29])
#
#
# new_password = 'password'
#
# db_password = b'$2b$12$RZfOcLSYfgpW5eqmqg.xN.qyJHoOsTif58KsBhQrrbuxckVa0cpVq'
# print(bcrypt.checkpw((new_password + secret).encode(), db_password))


# POST /login  form(username, password) -> ok session_key/jwt_key
# a) session: db users: session_key, user_id, date, is_active
# b) jwt: secret_key -> token(user_id, roles: [USER, ADMIN])

# GET /secret_data -> 403 status  (?)


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQWNhZGVteSBCYWNrZW5kIiwicm9sZXMiOlsiQURNSU4iXX0.qf96rc2HVxLh4jMxpfUScnaT5xc0-i7o9nAvowMCRhU
# my-secret
