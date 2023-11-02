import unittest
from metacl import CustomMeta, CustomClass

class TestCustomClass(unittest.TestCase):
    def test_custom_x_class(self):
        self.assertEqual(CustomClass.custom_x, 50)

    def test_class(self):
        self.assertRaises(AttributeError, getattr, CustomClass, 'x')

    def test_custom_x(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)

    def test_custom_val(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_val, 99)

    def test_custom_line(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_line(), 100)

    def test_str(self):
        inst = CustomClass()
        self.assertEqual(str(inst), "Custom_by_metaclass")

    def test_x(self):
        inst = CustomClass()
        self.assertRaises(AttributeError, getattr, inst, 'x')

    def test_val(self):
        inst = CustomClass()
        self.assertRaises(AttributeError, getattr, inst, 'val')

    def test_line(self):
        inst = CustomClass()
        self.assertRaises(AttributeError, getattr, inst, 'line')

    def test_yyy(self):
        inst = CustomClass()
        self.assertRaises(AttributeError, getattr, inst, 'yyy')

    def test_dynamic(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        self.assertEqual(inst.custom_dynamic, "added later")
        self.assertRaises(AttributeError, getattr, inst, 'dynamic')


if __name__ == '__main__':
    unittest.main()
