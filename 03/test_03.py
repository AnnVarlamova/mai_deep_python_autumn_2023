import unittest
import io
from unittest.mock import patch
from main import CustomList

class TestCustomList(unittest.TestCase):
    def test_add(self):
        first = CustomList([10, 6, 3])
        second = CustomList([5, 6])
        self.assertEqual(first + second, CustomList([15, 12, 3]))
        self.assertEqual(first + [1], CustomList([11, 6, 3]))
        self.assertEqual([-80] + first, CustomList([-70, 6, 3]))

    def test_sub_rsub(self):
        first = CustomList([1, 2, 3])
        second = CustomList([4, 5, 6])
        self.assertEqual(first - second, CustomList([-3, -3, -3]))
        self.assertEqual(first - [4, 5, 6], CustomList([-3, -3, -3]))
        self.assertEqual([4, 5, 6] - first, CustomList([3, 3, 3]))

    def test_comparison(self):
        list1 = CustomList([9, 2, 6])
        list2 = CustomList([3, 5, 6])
        list3 = CustomList([1, 2, 3, 4])

        self.assertTrue(list1 == list1)
        self.assertTrue(list1 != list2)
        self.assertTrue(list1 > list2)
        self.assertTrue(list1 >= list2)
        self.assertTrue(list2 < list1)
        self.assertTrue(list2 <= list1)
        self.assertTrue(list1 > list3)
        self.assertTrue(list1 >= list3)
        self.assertTrue(list3 < list1)
        self.assertTrue(list3 <= list1)

    def test_str(self):
        result = CustomList([5, 0])
        self.assertEqual(str(result), "[5, 0], sum = 5")

    def test_copy(self):
        result = CustomList([1, 2, 3])
        new_res = result.copy()
        self.assertIsNot(result, new_res)
        self.assertEqual(result, new_res)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_list(self, mock_stdout, mock_input):
        result = CustomList([1, 2, 3])
        result + "not_a_list"
        self.assertEqual(mock_stdout.getvalue(), "Not a list\n")



if __name__ == '__main__':
    unittest.main()
