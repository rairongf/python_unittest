import unittest
from utils.calculadora import CalculadoraUtil as cl

class TestCalculadora(unittest.TestCase):
    
    # SOMA 
    def testSomar(self):
        self.assertEqual(cl.somar(self, 2, 4), 6, "Resposta esperada: 6")
    
    def testSomarFloat(self):
        self.assertAlmostEqual(cl.somar(self, 2.1, 1.3), 3.4, places=2, msg="Resposta esperada: 3.4") 

    # SUBTRAÇÃO 
    def testSubtrair(self):
        self.assertEqual(cl.subtrair(self, 2, 1), 1, "Resposta esperada: 1")
    
    def testSubtrairFloat(self):
        self.assertAlmostEqual(cl.subtrair(self, 2.1, 3.3), -1.2, places=2, msg="Resposta esperada: -1.2") 
    
    # MULTIPLICAÇÃO 
    def testMultiplicar(self):
        self.assertEqual(cl.multiplicar(self, 2, 2), 4, "Resposta esperada: 4")

    def testMultiplicarFloat(self):
        self.assertAlmostEqual(cl.multiplicar(self, 2.1, 3), 6.3, places=2, msg="Resposta esperada: 6.3")
   
    # DIVISÃO 
    def testDividir(self):
        self.assertEqual(cl.dividir(self, 9, 3), 3, "Resposta esperada: 3")
    
    def testDividirFloat(self):
        self.assertAlmostEqual(cl.dividir(self, 3.72, 1.2), 3.1, places=2, msg="Resposta esperada: 3.1") 

    def testDividirZero(self):
        self.assertEqual(cl.dividir(self, 2, 0), None, "Resposta esperada: None")

if __name__ == '__main__':
    unittest.main()