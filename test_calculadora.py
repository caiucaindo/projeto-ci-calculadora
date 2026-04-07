import unittest
from calculadora import somar

class TestCalculadora(unittest.TestCase):
    
    def test_somar_numeros_positivos(self):
        resultado = somar(2, 3)
        self.assertEqual(resultado, 5)
        
    def test_somar_numeros_negativos(self):
        resultado = somar(-1, -1)
        self.assertEqual(resultado, -2)

if __name__ == '__main__':
    unittest.main()


# Explicação: O unittest é uma ferramenta que já vem instalada no Python.
# O código acima simplesmente chama a função somar que fizemos na aula passada e verifica se 2 + 3 realmente dá 5. 
# Se der, o teste passa (verde). Se alguém estragar a função no futuro, o teste falha (vermelho).