import unittest

def es_divisible_entre_tres_o_cinco(x):
    if  x%3 ==0 or x%5 == 0:
        return True
    else:
        return False

class Multiplos_Tres_O_Cinco(unittest.TestCase):

    def test_prueba_que_uno_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(1), False)
       
    def test_prueba_que_dos_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(2), False)

    def test_prueba_que_tres_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(3), True)

    def test_prueba_que_cuatro_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(4), False)

    def test_prueba_que_cinco_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(5), True)

    def test_prueba_que_seis_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(6), True)
   
    def test_prueba_que_siete_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(7), False)

    def test_prueba_que_ocho_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(8), False)

    def test_prueba_que_nueve_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(9), True)

    def test_prueba_que_diez_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(10), True)

    def test_prueba_que_once_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(11), False)

    def test_prueba_que_doce_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(12), True)

    def test_prueba_que_trece_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(13), False)

    def test_prueba_que_cartorce_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(14), False)

    def test_prueba_que_quince_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(15), True)

    def test_prueba_que_dieciseis_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(16), False)

    def test_prueba_que_diecisiete_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(17), False)

    def test_prueba_que_dieciocho_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(18), True)

    def test_prueba_que_diecinueve_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(19), False)

    def test_prueba_que_veinte_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(20), True)

    def test_prueba_que_veintiuno_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(21), True)

    def test_prueba_que_veintidos_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(22), False)

    def test_prueba_que_veintitres_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(23), False)

    def test_prueba_que_veinticuatro_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(24), True)

    def test_prueba_que_veinticinco_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(25), True)

    def test_prueba_que_veintiseis_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(26), False)

    def test_prueba_que_veintisiete_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(27), True)

    def test_prueba_que_veintiocho_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(28), False)

    def test_prueba_que_veintinueve_no_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(29), False)

    def test_prueba_que_treinta_deberia_ser_divisible_entre_tres_o_cinco(self):
        self.assertEqual(es_divisible_entre_tres_o_cinco(30), True)

if __name__ == '__main__':
    unittest.main()
