from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
#this is a rrrrrrreal head scratcher
#there's a problem with your mocker, bad request
    def test_serv4(self):

        objs=['Bastille', 'Stockade', 'Chain', 'Lock', 'Bars', 'Hook', 'Machine']
        sources=['Red', 'Burning', 'Scorched', 'Scalding']
        #with requests_mock.Mocker() as m:
            #m.get('http://service_4:5000/final', json={"obj":"prison", "source":"flame"})
        obj = []
        source = []
        response = self.client.post(url_for('final'), json={"obj": "prison", "source": "flame"})
        words = response.text.split(' ')
        print(words)
        
        for word in words:
            if word in objs:
                obj.append(word)
            elif word in sources:
                source.append(word)
        self.assertIn(obj[0], objs)
        self.assertIn(source[0], sources)


        # self.assert200(response)
        # self.assertIn("The Big Doofus", response.data.decode())
        # self.assertIn("gate", response.data.decode())
        # self.assertIn("air", response.data.decode())
