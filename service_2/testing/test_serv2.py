from flask import url_for
from flask_testing import TestCase


from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    
    
    def test_objs(self):
        choices = ["prison", "gate", "weapon (bladed)", "weapon (blunt)", "dagger", "telescope", "armour", "crown", "scepter", "throne", "tower", "lake", "ocean", "mountain", "fortress"]
        response = self.client.get(url_for('rand_1'))

        self.assert200(response)
        self.assertIn(response.text, choices)