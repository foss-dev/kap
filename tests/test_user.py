import os
import unittest
from werkzeug import generate_password_hash

from tracer import app
from tracer.data.models import db, User, Role

USER_TEST_DB = 'user_test.db'

def create_roles(ctx):
    role = Role('admin')

    ctx.session.add(role)
    ctx.session.commit()


def create_user(ctx):
    email = 'admin@admin'
    name = 'John Doe'
    password = generate_password_hash('admin')
    is_active = True
    roles = 1
    user = User(
        email=email, name=name, password=password, active=is_active, roles=roles)
    
    ctx.session.add(user)

    ctx.session.commit()

class TestUserApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(USER_TEST_DB)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.app_context().push()
        

    def setUp(self):
        with app.app_context():
            db.init_app(app)
            db.drop_all()
            db.create_all()
            create_roles(db)
            create_user(db)

    def tearDown(self):
        pass
    
    def test_users(self):

        user_count = User.query.count()
        minimum_count = 1

        self.assertGreaterEqual(user_count, minimum_count, msg="Users should have 1 user or more than")
    
    def test_get_user(self):

        user_id = 1
        count_have_to_be_one = 1

        user_count = User.query \
            .with_entities(User.id, User.active, User.email, User.name, Role.id.label('roleid'), Role.name.label('rolename')) \
            .join(Role, Role.id == User.roles) \
            .filter(User.id == user_id).count()

        self.assertEqual(user_count, count_have_to_be_one, msg="User have to return 1 user")

if __name__ == "__main__":
    unittest.main()