from cal import Add
import unittest

class Testcal(unittest.TestCase):
    def test_empty(self):
        #For example "" as inputs. (for an empty string it will return 0)
        result=Add('')
        self.assertEqual(result,0)

    def test_2_unempty(self):
        result=Add('1,2')
        self.assertEqual(result,3)

    def test_3_numbers_unknown(self):
        result=Add('1,2,10')
        self.assertEqual(result,13)

    def test_4_newline(self):
        result=Add("1\n2,3")
        self.assertEqual(result,6)

    def test_5_delimiter(self):
        result=Add("//;\n1;2;,3;..4")
        self.assertEqual(result,10)

    def test_6_negative(self):
        result=Add("//;\n-1;2;,3;..4")
        with self.assertRaises(Exception) as context:
            Add("//;\n-1;2;,3;..4")
        print(context)
        self.assertTrue('Exception: negatives not allowed -1' in context.exception)




if __name__ == '__main__':
    unittest.main()