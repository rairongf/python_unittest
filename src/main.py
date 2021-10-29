from utils.calculadora import CalculadoraUtil
import colored
from colored import stylize

calculadora = CalculadoraUtil()

def inputs():
  arg1 = float(input(stylize("\n Digite o valor do primeiro argumento:  ", colored.fg("orange_1"))))
  arg2 = float(input(stylize(" Digite o valor do segundo argumento:  ", colored.fg("orange_1"))))
  print(" ")
  return arg1,arg2

def case0():
  print(stylize('\n Fechando programa... 👋', colored.fg("red")))

def case1():
  arg1,arg2 = inputs()
  resultado = calculadora.somar(argumento1=arg1, argumento2=arg2)
  print(stylize(" Resultado:", colored.fg("chartreuse_3b")))
  print(stylize(f" {arg1} + {arg2} = {resultado}", colored.fg("chartreuse_3b")))

def case2():
  arg1,arg2 = inputs()
  resultado = calculadora.subtrair(argumento1=arg1, argumento2=arg2)
  print(stylize(" Resultado:", colored.fg("chartreuse_3b")))
  print(stylize(f" {arg1} - {arg2} = {resultado}", colored.fg("chartreuse_3b")))

def case3():
  arg1,arg2 = inputs()
  resultado = calculadora.multiplicar(argumento1=arg1, argumento2=arg2)
  print(stylize(" Resultado:", colored.fg("chartreuse_3b")))
  print(stylize(f" {arg1} * {arg2} = {resultado}", colored.fg("chartreuse_3b")))

def case4():
  arg1,arg2 = inputs()
  resultado = calculadora.dividir(argumento1=arg1, argumento2=arg2)
  if resultado == None:
    return
  print(stylize(" Resultado:", colored.fg("red_1")))
  print(stylize(f" {arg1} / {arg2} = {resultado}", colored.fg("red_1")))


switch = {
  "0": case0,
  "1": case1,
  '2': case2,
  '3': case3,
  '4': case4,
}
operacao = -1

while operacao != "0":
  print(stylize("\n\n #### MENU #### ", colored.fg("orange_1"), colored.attr("bold")))
  print(stylize(" ! Escolha qual operação deseja realizar e digite sua opção abaixo ! ", colored.fg("orange_1")))
  print(stylize(" # 1️⃣  => SOMAR ", colored.fg("medium_purple_2a")))
  print(stylize(" # 2️⃣  => SUBTRAIR ", colored.fg("medium_purple_2a")))
  print(stylize(" # 3️⃣  => MULTIPLICAR ", colored.fg("medium_purple_2a")))
  print(stylize(" # 4️⃣  => DIVIDIR ", colored.fg("medium_purple_2a")))
  print(stylize(" ! Digite 0 para fechar o programa ! ", colored.fg("orange_1")))
  operacao = input(stylize("\n Qual operação deseja fazer?   ", colored.fg("orange_1")))
  
  case = switch.get(operacao)
  case()

  input(stylize("\n Pressione qualquer tecla para continuar...", colored.fg("red")))
  
