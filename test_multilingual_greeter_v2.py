from unittest import TestCase
from unittest.mock import patch
from io import StringIO

import multilingual_greeter_v2


class MultilingualGreeterV2Test(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_mode_options(self, stdout_mock):
        modes = {
            1: "User Mode",
            2: "Admin Mode"
        }
        expected = "1: User Mode\n" \
                   "2: Admin Mode\n" \


        multilingual_greeter_v2.print_mode_options(modes)
        self.assertEqual(expected, stdout_mock.getvalue())


    @patch('builtins.input', return_value="1")
    def test_choose_mode(self, user_input):
        actual = multilingual_greeter_v2.choose_mode()
        self.assertEqual(1, actual)


    def test_language_choose_mode_is_valid(self):
        mode_choice = {
            0: "Exit",
            1: "User Mode",
            2: "Admin Mode"
        }

        test_cases = [
            (1, True),
            (2, True),
            (3, False),
            (4, False),
            (5, False),
            (10, False),
            ('PIG LATIN', False)
        ]

        for key, expected in test_cases:
            with self.subTest(f"{key}, {expected}"):
                self.assertEqual(expected, multilingual_greeter_v2.choose_mode_is_valid(mode_choice, key))


    @patch('builtins.input', return_value='Y')
    def test_admin_greeter(self):
        actual = multilingual_greeter_v2.admin_greeter('Y')
        self.assertEqual('Y', actual)

