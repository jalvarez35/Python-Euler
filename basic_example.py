import unittest

class ExampleTest(unittest.TestCase):
    def test_uno_mas_dos_deberia_dar_tres(self):
        """
        Prueba que la suma de uno mas dos sea igual a tres
        """
        self.assertEqual(1+2, 3)

if __name__ == "__main__":
    unittest.main()
