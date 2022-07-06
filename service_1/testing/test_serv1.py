from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://service_2:5000/rand_1', text='gate')
            m.get('http://service_3:5000/rand_2', text='air')
            m.post('http://service_4:5000/final', text="The Big Doofus")

            response = self.client.get(url_for('home'))


        self.assert200(response)
        self.assertIn("The Big Doofus", response.data.decode())
        self.assertIn("gate", response.data.decode())
        self.assertIn("air", response.data.decode())
