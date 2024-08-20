import unittest
from io import StringIO
import sys

class TestGreetings(unittest.TestCase):

    def test_hello(self):
        user_input = "Hello"
        expected_output = "$0\n"
        self.assertEqual(self.run_test(user_input), expected_output)

    def test_how_you_doing(self):
        user_input = "How you doing?"
        expected_output = "$20\n"
        self.assertEqual(self.run_test(user_input), expected_output)

    def test_h_greeting(self):
        user_input = "hi"
        expected_output = "$20\n"
        self.assertEqual(self.run_test(user_input), expected_output)

    def test_no_h_greeting(self):
        user_input = "good morning"
        expected_output = "$100\n"
        self.assertEqual(self.run_test(user_input), expected_output)

    def test_hello_with_spaces(self):
        user_input = "  Hello  "
        expected_output = "$0\n"
        self.assertEqual(self.run_test(user_input), expected_output)

    def run_test(self, user_input):
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        sys.stdin = StringIO(user_input)
        exec('''user_input = input("greetings: ").strip()

if user_input.lower().startswith("hello"):
    print("$0")
elif user_input == "How you doing?":
    print("$20")
elif user_input.lower().startswith("h"):
    print("$20")
else:
    print("$100")''')

        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        return output

if __name__ == "__main__":
    unittest.main()
