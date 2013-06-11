import unittest

def fibo(x):
    if x == 1 or x==2:
        return x
    return fibo(x-1) + fibo(x-2)

class FibonacciTest(unittest.TestCase):
    def test_prueba_que_el_fibonacci_de_1_es_1(self):
        """
        Prueba que el fibonacci de 1 sea 1.
        """
        self.assertEqual(fibo(1), 1)

    def test_prueba_que_el_fibonacci_de_2_es_2(self):
        """
        Prueba que el fibonacci de 2 sea 2.
        """
        self.assertEqual(fibo(2), 2)
    
    def test_prueba_que_el_fibonacci_de_3_es_3(self):
        """
        Prueba que el fibonacci de 3 sea 3.
        """
        self.assertEqual(fibo(3), 3)

    def test_prueba_que_el_fibonacci_de_4_es_5(self):
        """
        Prueba que el fibonacci de 4 sea 5 .
        """
        self.assertEqual(fibo(4), 5)
        
    def test_prueba_que_el_fibonacci_de_5_es_8(self):
        """
        Prueba que el fibonacci de 5 sea 8.
        """
        self.assertEqual(fibo(5), 8)

    def test_prueba_que_el_fibonacci_de_6_es_13(self):
        """
        Prueba que el fibonacci de 6 sea 13.
        """
        self.assertEqual(fibo(6), 13)

    def test_prueba_que_el_fibonacci_de_7_es_21(self):
        """
        Prueba que el fibonacci de 7 sea 3.
        """
        self.assertEqual(fibo(7), 21)

    def test_prueba_que_el_fibonacci_de_8_es_34(self):
        """
        Prueba que el fibonacci de 8 sea 34.
        """
        self.assertEqual(fibo(8), 34)

    def test_prueba_que_el_fibonacci_de_9_es_55(self):
        """
        Prueba que el fibonacci de 9 sea 55.
        """
        self.assertEqual(fibo(9), 55)
    
    def test_prueba_que_el_fibonacci_de_10_deberia_ser_89(self):
        """
        Prueba que el fibonacci de 10 es 89
        """
        self.assertEqual(fibo(10), 89)
    
    def test_prueba_que_el_fibonacci_de_16_deberia_ser_1597(self):
        """
        Prueba que el fibonacci de 16 es 1597
        """
        self.assertEqual(fibo(16), 1597)

if __name__ == '__main__':
#    unittest.main()
     print fibo(4000)
