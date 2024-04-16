import unittest
from facotrial import factorial
    
class TestFactorial(unittest.TestCase):
    
    def test_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)

    def test_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)

    def test_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)

    def test_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado, 24)

    def test_8(self):
        resultado = factorial(8)
        self.assertEqual(resultado, 40320)
        
unittest.main()