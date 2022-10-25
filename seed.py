from app import app
from models import db, User

db.drop_all()
db.create_all()

user1 = User.register(
                username = 'mtbocim',
                password = 'password',
                email = 'email@email.com',
                first_name = 'Michael',
                last_name = 'Bocim',
            )
user2 = User.register(
                username = 'gball',
                password = 'password1',
                email = 'email2@email.com',
                first_name = 'Gordon',
                last_name = 'Ball',
            )

db.session.add(user1)

db.session.add(user2)
db.session.commit()