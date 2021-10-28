class CalculadoraUtil:
    def somar(self, argumento1:float, argumento2:float):
        return argumento1 + argumento2

    def dividir(self, argumento1:float, argumento2:float):
        try:
          return argumento1 / argumento2
        except:
          print(' !!! Erro: divisão por zero !!!')
          return None

    def subtrair(self, argumento1:float, argumento2:float):
        return argumento1 - argumento2

    def multiplicar(self, argumento1:float, argumento2:float):
        return argumento1 * argumento2