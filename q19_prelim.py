import unittest

def check(x):

    return x == 'PEDRO'

class MyTest(unittest.TestCase):

    def test(self):
        self.assertTrue(check('PEDRO'))

if __name__=='__main__':

    unittest.main()