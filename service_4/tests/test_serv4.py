from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_serv4(self):
        objs=['Bastille', 'Stockade', 'Chain', 'Lock', 'Bars', 'Hook', 'Machine']
        sources=['Red', 'Burning', 'Scorched', 'Scalding']
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
