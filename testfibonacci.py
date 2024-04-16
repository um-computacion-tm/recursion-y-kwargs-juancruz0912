import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    
    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)

    def test_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)

    def test_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)

    def test_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)

    def test_with_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)


    def test_8(self):
        resultado = fibonacci(8)
        self.assertEqual(resultado, 21)

    def test_20(self):
        resultado = fibonacci(20)
        self.assertEqual(resultado, 6765)

    def test_30(self):
        resultado = fibonacci(30)
        self.assertEqual(resultado, 832040) 


if __name__ == "__main__":
    unittest.main()