from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        """Executed before each test"""
        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_homepage(self):
        """Make sure HTML is showed, and the highscore, nplays info is in the session
        along with the game board"""

        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)


    def test_valid_word(self):
        """Test if word is a valid word by modifying the board in the session"""

        with client.session_transaction() as sess:
            sess['board'] = [["B", "L", "U", "E", "E"],
                             ["B", "L", "U", "E", "E"],
                             ["B", "L", "U", "E", "E"],
                             ["B", "L", "U", "E", "E"],
                             ["B", "L", "U", "E", "E"]]
                           
            response = self.client.get("/check-word?word=blue")
            self.assertEqual(response.json["result"], "ok")


    def test_invalid_word(self):
        """Test if word is valid and exists on the board"""

        with self.client:
        response = self.client.get("/check-word?word=pink")
        self.assertEqual(response.json["result"], "not-on-board")


    def test_non_english_word(self):
        """Test if word is a valid English word in the dictionary""" 

        with self.client:
            response = self.client.get("/check-word?word=asjfajsnj")
            self.assertEqual(response.json["result"], "not-word")