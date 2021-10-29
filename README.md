# Seminario Python_unittest

## :scroll: Sobre o projeto

Projeto criado para a disciplina de Engenharia de Software - C214
Instituto Nacional de Telecomunicações - INATEL

O python_unittest é uma calculadora basica criada com o intuito de realizar testes de unidade com o Python Unittest

### Funções implementadas na calculadora
- :heavy_plus_sign: Soma
- :heavy_minus_sign: Subtração
- :heavy_multiplication_x: Multiplicação
- :heavy_division_sign: Divisão

<br/>

---
## :books: Sobre o Unittest

A estrutura de teste de unidade unittest foi originalmente inspirada por JUnit e é bem semelhante aos principais frameworks de teste de unidade em outras linguagens. Ele suporta automação de teste, compartilhamento de configuração e código de desligamento para testes, agregação de testes em coleções e independência dos testes do framework.

Abaixo um exemplo demonstrando como testar uma simples função.
```
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()
```
O resultado de python foo.py você confere abaixo.
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
O exemplo seguinte demonstra como testar uma pequena classe.
```
import unittest

class MyFun:
    def fun(self, n):
        return n + 1

class MyFunTest(unittest.TestCase):
    def testFun(self):
        obj = MyFun()
        self.assertEqual(obj.fun(3), 4)

if __name__ == '__main__':
    unittest.main()
```
O resultado é semelhante ao anterior.
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Todas as fontes utilizadas e mais informações se encontram nos links abaixo:

- [Unittest](https://docs.python.org/3/library/unittest.html)
- [Primeiros passos com testes unitarios](http://devfuria.com.br/python/tdd-primeiros-passos-com-testes-unitarios/)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/#choosing-a-test-runner)


<br/>

---
## :computer: Pré-requisitos

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)
- [Pycharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)

<br/>

---

## :point_right: Como Executar

- Para clonar o repositório em algum lugar na sua máquina, basta utilizar o comando abaixo:
```bash
$ git clone https://github.com/rairongf/python_unittest.git
```
- Para iniciar a calculadora execute o comando abaixo:
```
python src/main.py
```
- Para realizar os teste utilize o comando abaixo:
```
python src/testCalculadora.py
```

## Colaboradores
- Rafaela Ferraz [@rafaferraz](https://github.com/rafaferraz)
- Leonardo de Moura Brandão [@odrah](https://github.com/odrah)
- Rairon Ferreira [@rairongf](https://github.com/rairongf)
