from main import parse_json
from main import mean
from main import my_function
import unittest
from unittest.mock import MagicMock, patch


class TestParseJson(unittest.TestCase):

    def test_keyword_callback_called_once(self):
        keyword_callback = MagicMock()

        json_str = '{"1": "w1 w2", "2": "ann like"}'
        required_fields = ["1"]
        keywords = ["w2"]

        parse_json(json_str, required_fields, keywords, keyword_callback)
        keyword_callback.assert_called_once_with('w2', '1')

    def test_keyword_callback_called_twice(self):
        keyword_callback = MagicMock()

        json_str = '{"1": "W1 w2", "2": "w2 w3"}'
        required_fields = ["1", "2"]
        keywords = ["w2"]

        parse_json(json_str, required_fields, keywords, keyword_callback)
        self.assertEqual(keyword_callback.call_count, 2)

    def test_keyword_callback_not_called(self):
        keyword_callback = MagicMock()

        json_str = '{"1": "W1 w3", "2": "w2"}'
        required_fields = ["1"]
        keywords = ["w2"]

        parse_json(json_str, required_fields, keywords, keyword_callback)
        keyword_callback.assert_not_called()

    @patch('builtins.print')
    def test_no_keyword_callback(self, mock_print):
        json_str = '{"1": "W1 w2", "2": "w2 w3"}'
        required_fields = ["1"]
        keywords = ["w2"]

        parse_json(json_str, required_fields, keywords)
        mock_print.assert_called_once_with('No keyword_callback')


class TestMean(unittest.TestCase):
    @patch('builtins.print')
    def test_decorator_0(self, mock_print):
        @mean(3)
        def test_func():
            pass

        test_func()
        output = mock_print.call_args[0][0]
        average_time = float(output.split()[-2])
        self.assertAlmostEqual(average_time, 0.0, places=1)

    @patch('builtins.print')
    def test_decorator_1(self, mock_print):
        my_function("a", "b")
        output = mock_print.call_args[0][0]
        average_time = float(output.split()[-2])
        self.assertAlmostEqual(average_time, 0.1, places=1)

    @patch('builtins.print')
    def test_decorator_5(self, mock_print):
        for _ in range(5):
            my_function("a", "b")
        output = mock_print.call_args[0][0]
        average_time = float(output.split()[-2])
        self.assertAlmostEqual(average_time, 0.1, places=1)


if __name__ == '__main__':
    unittest.main()
