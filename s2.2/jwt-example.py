import hashlib

import jwt

# token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQWNhZGVteSBCYWNrZW5kIiwicm9sZXMiOlsiQURNSU4iXX0.qf96rc2HVxLh4jMxpfUScnaT5xc0-i7o9nAvowMCRhU'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQWNhZGVteSBCYWNrZW5kIiwicm9sZXMiOlsiQURNSU4iLCJVU0VSIl19.BgNFm6IBc16dyqQMtcel7kdJCXSV5LDuFCU0dZJCAt8'
key = hashlib.sha256('my-secret')

try:
    jwt_data = jwt.decode(jwt=token, key=key, algorithms=["HS256"])
    print(jwt_data)
except jwt.exceptions.InvalidSignatureError:
    print("Signature verification failed")
