import unittest

def es_primo(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

class PrimoTest(unittest.TestCase):

    def test_prueba_que_el_2_deberia_ser_primo(self):
        """
        Prueba que el 3 deberia ser primo
        """
        self.assertEqual(es_primo(2), True)

    def test_prueba_que_el_4_no_deberia_ser_primo(self):
        """
        Prueba que el 4 no deberia ser primo
        """
        self.assertEqual(es_primo(4), False)

    def test_prueba_que_el_5_deberia_ser_primo(self):
        """
        Prueba que el 5 deberia ser primo
        """
        self.assertEqual(es_primo(5), True)

    def test_prueba_que_el_6_no_deberia_ser_primo(self):
        """
        Prueba que el 6 no deberia ser primo
        """
        self.assertEqual(es_primo(6), False)

    def test_prueba_que_el_31_deberia_ser_primo(self):
        """
        Prueba que el 31 deberia serprimo
        """
        self.assertEqual(es_primo(31), True)

    def test_prueba_que_el_32_no_deberia_ser_primo(self):
       """
       Prueba que el 32 no deberia ser primo
       """
       self.assertEqual(es_primo(32), False)

if __name__ == '__main__':
    unittest.main()
