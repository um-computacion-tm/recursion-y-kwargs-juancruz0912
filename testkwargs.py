import unittest
from kwars import buscar_datos, database

class TestKwargs(unittest.TestCase):
    
    def test_p1(self):
        resultado = buscar_datos('Pablo', 'Diego', 'Ruiz', 'Picasso',**database)
        self.assertEqual(resultado, "p1")

    def test_p2(self):
        resultado = buscar_datos('Juan Cruz', 'Rupcic', 'Gattoni',**database)
        self.assertEqual(resultado, "p2")

    def test_p4(self):
        resultado = buscar_datos('Pablo', 'Martinez',**database)
        self.assertEqual(resultado, "p4")

    def test_noexiste(self):
        resultado = buscar_datos('Emanuel', 'Yudica',**database)
        self.assertEqual(resultado, "la persona no existe")

unittest.main()