import unittest

def es_primo(x):
    i = 2
    while (i < x):
        if x%i==0:
            return False
        i += 1
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

def es_factor(x, y):
    return y%x == 0

class EsFactorTest(unittest.TestCase):

    def test_prueba_que_3_deberia_ser_factor_de_12(self):
        """
        Prueba que el 3 deberia ser factor de 12
        """
        self.assertEqual(es_factor(3, 12), True)

    def test_prueba_que_5_deberia_ser_factor_de_20(self):
        """
        Prueba que el 5 deberia ser factor de 20
        """
        self.assertEqual(es_factor(5, 20), True)

    def test_prueba_que_6_deberia_ser_factor_18(self):
        """
        Prueba que el 6 deberia ser factor de 18
        """
        self.assertEqual(es_factor(6, 18), True)

    def test_prueba_que_5_no_deberia_ser_factor_de_6(self):
        """
        Prueba que el 5 no deberiaser factor de 6
        """
        self.assertEqual(es_factor(5, 6), False)

    def test_prueba_que_7_no_deberia_ser_factor_de_8(self):
        """
        Prueba que 7 no deberia ser factor de 8
        """
        self.assertEqual(es_factor(7, 8), False)

    def test_prueba_que_8_no_deberia_ser_factor_de_9(self):
        """
        Prueba que 8 no deberia ser factor de 9
        """
        self.assertEqual(es_factor(8, 9), False)

def factores_primos(x):
    vector_factores_primos = []
    i = 2
    while (i < x):
        if es_factor(i, x) and es_primo(i):
            vector_factores_primos.append(i)
        i += 1
    return vector_factores_primos        

class FactoresPrimosTest(unittest.TestCase):

    def test_prueba_que_5_7_13_y_29_deberian_ser_factores_primos_de_13195(self):
        self.assertEqual(factores_primos(13195), [5, 7, 13, 29])
       
def mayor_factor_primo(x):
    return max(factores_primos(x))

class MayorFactorPrimoTest(unittest.TestCase):
    
    def test_prueba_que_el_mayor_factor_primo_de_13195_deberia_ser_29(self):
        self.assertEqual(mayor_factor_primo(13195), 29)

if __name__ == '__main__':
#    unittest.main()
    print(mayor_factor_primo(600851475143))
