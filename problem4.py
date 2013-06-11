import unittest

def es_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

class NumeroPalindromeTest(unittest.TestCase):
    def test_prueba_que_111_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(111), True)

    def test_prueba_que_123_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(123), False)

    def test_prueba_que_121_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(121), True)

    def test_prueba_que_232_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(232), True)

    def test_prueba_que_250_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(250), False)

    def test_prueba_que_500_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(500), False)

    def test_prueba_que_636_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(636), True)

    def test_prueba_que_777_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(777), True)

    def test_prueba_que_890_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(890), False)
    
    def test_prueba_que_106837_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(106837), False)

    def test_prueba_que_998001_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(998001), False)

    def test_prueba_que_103896_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(103896), False)
    
    def test_prueba_que_998001_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(998001), False)
    
    def test_prueba_que_70512_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(70512), False)

    def test_prueba_que_166788_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(166788), False)

    def test_prueba_que_87600_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(87600), False)
    
    def test_prueba_que_131400_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(131400), False)
    
    def test_prueba_que_250000_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(250000), False)
    
    def test_prueba_que_345543_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(345543), True)
    
    def test_prueba_que_106938_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(106938), False)
    
    def test_prueba_que_906609_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(906609), True)
    
    def test_prueba_que_831138_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(831138), True)
    
    def test_prueba_que_819918_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(819918), True)
    
    def test_prueba_que_792297_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(792297), True)
    
    def test_prueba_que_514415_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(514415), True)
    
    def test_prueba_que_5225_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(5225), True)
    
    def test_prueba_que_8008_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(8008), True)
    
    def test_prueba_que_8448_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(8448), True)
    
    def test_prueba_que_7887_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(7887), True)
    
    def test_prueba_que_8338_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(8338), True)
    
    def test_prueba_que_8668_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(8668), True)
    
    def test_prueba_que_8574_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(8574), False)
    
    def test_prueba_que_1234_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(1234), False)
    
    def test_prueba_que_4389_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(4389), False)
    
    def test_prueba_que_9301_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(9301), False)
    
    def test_prueba_que_1992_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(1992), False)

    def test_prueba_que_67276_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(67276), True)
    
    def test_prueba_que_28982_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(28982), True)
    
    def test_prueba_que_87678_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(87678), True)
    
    def test_prueba_que_11611_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(11611), True)

    def test_prueba_que_14285_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(14285), False)

    def test_prueba_que_15125_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(15125), False)
    
    def test_prueba_que_75824_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(75824), False)
    
    def test_prueba_que_85673_no_deberia_ser_palindrome(self):
        self.assertEqual(es_palindrome(85673), False)

if __name__ == '__main__':
    unittest.main()
