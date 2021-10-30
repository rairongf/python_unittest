# Seminário - Python Unittest

## :scroll: Sobre o projeto

Projeto criado para a disciplina de Engenharia de Software - C214
<br/>
Instituto Nacional de Telecomunicações - INATEL

O ``python_unittest`` é uma calculadora básica criada com o intuito de realizar testes de unidade com o **Python Unittest**.

### Funções implementadas na calculadora
:heavy_plus_sign: Soma
<br/>

:heavy_minus_sign: Subtração
<br/>

:heavy_multiplication_x: Multiplicação
<br/>

:heavy_division_sign: Divisão

## :books: Sobre o Unittest

A estrutura de teste de unidade `unittest` foi originalmente inspirada pelo **JUnit** e é bem semelhante aos principais frameworks de teste de unidade presentes em outras linguagens.

Ele suporta: 
- Automação de testes,
- Compartilhamento de configuração e código de desligamento para testes,
- Agregação de testes em coleções e independência dos testes do framework.

Abaixo está um exemplo que demonstra como testar uma simples função:
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
O resultado você confere abaixo:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
O exemplo seguinte demonstra como testar uma pequena classe:
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
O resultado é semelhante ao anterior:
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

## ⚙ Sobre o Pipenv

O Pipenv é uma ferramenta que visa trazer o melhor de todos os mundos de empacotamento (bundler, composer, npm, cargo, yarn, etc) para o ecossistema Python, casando o instalador de pacotes ``pip`` e ``virtualenv`` e substituindo o ``requirements.txt``.

Ele cria e gerencia automaticamente um *virtualenv* para seus projetos, além de adicionar ou remover pacotes do seu ``Pipfile`` ao instalar ou desinstalar pacotes. Ele também gera o sempre importante ``Pipfile.lock``, o seu querido arquivo de configuração de dependências do sistema.

### Instalar ``pipenv``
```
pip install pipenv
```
### Criar arquivo ``Pipfile`` e o ``virtualenv``
```
pipenv --three
```
A flag ``--three`` se refere ao Python 3. Caso queira utilizar com o Python 2 utilize ``--two``.
### Instalar dependências
```
pipenv install colored
```
Caso o objetivo seja instalar uma dependência para o ambiente de desenvolvimento, utilize a flag ``--dev``.
## :computer: Pré-requisitos

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)
- [Pycharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows) ou [VSCode](https://code.visualstudio.com/)

## :point_right: Como Executar

- Para clonar o repositório em algum lugar na sua máquina, basta utilizar o comando abaixo:
```bash
$ git clone https://github.com/rairongf/python_unittest.git
```
- Instale o `pipenv` executando o comando abaixo:
```
python -m pip install pipenv
```
- Para iniciar a calculadora, execute o comando abaixo:
```
pipenv run python src/main.py
```
- Para realizar os testes, utilize o comando abaixo:
```
pipenv run python src/testCalculadora.py
```

## Colaboradores
- Rafaela Ferraz [@rafaferraz](https://github.com/rafaferraz)
- Leonardo de Moura Brandão [@odrah](https://github.com/odrah)
- Rairon Ferreira [@rairongf](https://github.com/rairongf)
