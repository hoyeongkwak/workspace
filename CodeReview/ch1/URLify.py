# O(N)
import unittest

def urlify(string, length):
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

class Test(unittest.TestCase):
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_unlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
