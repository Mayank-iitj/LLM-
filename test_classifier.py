
import unittest
from question_classifier import classify_question, get_response

class TestQuestionClassifier(unittest.TestCase):

    def test_classify_question(self):
        self.assertEqual(classify_question("What is the capital of France?"), "factual")
        self.assertEqual(classify_question("Who invented the light bulb?"), "factual")
        self.assertEqual(classify_question("When was the internet created?"), "factual")
        self.assertEqual(classify_question("Where is the Eiffel Tower located?"), "factual")
        self.assertEqual(classify_question("How many planets are in our solar system?"), "factual")
        self.assertEqual(classify_question("Define photosynthesis."), "factual")
        self.assertEqual(classify_question("Explain quantum physics."), "factual")

        self.assertEqual(classify_question("Do you think pineapple belongs on pizza?"), "opinion")
        self.assertEqual(classify_question("Should we invest in renewable energy?"), "opinion")
        self.assertEqual(classify_question("What's your opinion on modern art?"), "opinion")
        self.assertEqual(classify_question("How do you feel about remote work?"), "opinion")
        self.assertEqual(classify_question("What is the best programming language?"), "opinion")
        self.assertEqual(classify_question("What is the worst movie ever made?"), "opinion")

        self.assertEqual(classify_question("Calculate the square root of 16."), "math")
        self.assertEqual(classify_question("Solve for x in 2x + 5 = 15."), "math")
        self.assertEqual(classify_question("What is 10 plus 5?"), "math")
        self.assertEqual(classify_question("What is 20 minus 7?"), "math")
        self.assertEqual(classify_question("What is 3 times 9?"), "math")
        self.assertEqual(classify_question("What is 100 divided by 10?"), "math")

        self.assertEqual(classify_question("Tell me a joke."), "unknown")
        self.assertEqual(classify_question("Sing a song."), "unknown")

    def test_get_response_factual(self):
        response = get_response("factual", "What is the capital of France?")
        self.assertIsInstance(response, str)
        self.assertFalse("Error" in response)

    def test_get_response_opinion(self):
        response = get_response("opinion", "Do you think AI will take over the world?")
        self.assertIsInstance(response, str)
        self.assertFalse("Error" in response)

    def test_get_response_math(self):
        response = get_response("math", "Calculate 2 plus 2.")
        self.assertIsInstance(response, str)
        self.assertIn("math question", response)

    def test_get_response_unknown(self):
        response = get_response("unknown", "Tell me a story.")
        self.assertIsInstance(response, str)
        self.assertIn("not sure how to classify", response)

if __name__ == '__main__':
    unittest.main()


