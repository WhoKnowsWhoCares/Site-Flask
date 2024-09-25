import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        # with self.app.app_context():
        #     db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_app_exists(self):
        self.assertFalse(current_app is None)
