import unittest

def check(x):

    return x >= 50

class MyTest(unittest.TestCase):

    def test(self):
        self.assertTrue(check(65))
    

if __name__=='__main__':

    unittest.main()