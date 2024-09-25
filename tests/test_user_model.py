import unittest
from app import create_app
from app.models import db, User, AnonymousUser, UserRole


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        # with self.app.app_context():
        #     db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_password_setter(self):
        u = User(username="john", email="john@example.com", password="cat")
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(username="john", email="john@example.com", password="cat")
        with self.assertRaises(AttributeError):
            u.password

    def test_password_salts_are_random(self):
        u = User(username="john", email="john@example.com", password="cat")
        u2 = User(username="anna", email="anna@example.com", password="cat")
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_user_role(self):
        u = User(
            username="john",
            email="john@example.com",
            password="cat",
            role=UserRole.USER,
        )
        self.assertTrue(u.can(UserRole.USER))
        self.assertFalse(u.can(UserRole.ADMIN))
        self.assertFalse(u.is_administrator())

    def test_administrator_role(self):
        u = User(
            username="john",
            email="john@example.com",
            password="cat",
            role=UserRole.ADMIN,
        )
        self.assertFalse(u.can(UserRole.USER))
        self.assertTrue(u.can(UserRole.ADMIN))
        self.assertTrue(u.is_administrator())

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(UserRole.USER))
        self.assertFalse(u.can(UserRole.ADMIN))
