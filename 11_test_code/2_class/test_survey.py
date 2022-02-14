import unittest

from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Crea un questionario e imposta un set di risposte da usare con tutti i metodi"""
        question = "Quale linguaggio hai imparato per prima?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Italian', 'Mandarin']

    def test_store_single_response(self):
        """Test per una singola risposta."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
