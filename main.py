from tinydb import TinyDB
from api import response


db = TinyDB('db.json' , indent=4)


users = db.table('users')


if response.status_code == 200:
    users_data = response.json()['results']
    for user in users_data:
        users.insert({
            'first_name':user['name']['first'],
            'last_name':user['name']['last'],
            'age':user['dob']['age'],
            'email':user['email'],
            'country':user['location']['country'],
            'phone':user['phone'],
            
        })


