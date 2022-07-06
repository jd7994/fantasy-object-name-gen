from flask import url_for
from flask_testing import TestCase


from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    
    
    def test_source(self):
        choices = ["flame", "earth", "water", "air", 'the celestial', "hellfire", "the occult", "the infernal", "the void", "fey", "shadow", "enchantment", "illusion", "abberation"]
        response = self.client.get(url_for('rand_2'))

        self.assert200(response)
        self.assertIn(response.text, choices)