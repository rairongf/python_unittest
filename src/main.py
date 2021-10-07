from utils.calculadora import CalculadoraUtil

calculadora = CalculadoraUtil()

def inputs():
  arg1 = float(input("\n Digite o valor do primeiro argumento:  "))
  arg2 = float(input(" Digite o valor do segundo argumento:  "))
  print(" ")
  return arg1,arg2

def case0():
  print('\n Fechando programa...')

def case1():
  arg1,arg2 = inputs()
  resultado = calculadora.somar(argumento1=arg1, argumento2=arg2)
  print(" Resultado:")
  print(f" {arg1} + {arg2} = {resultado}")

def case2():
  arg1,arg2 = inputs()
  resultado = calculadora.subtrair(argumento1=arg1, argumento2=arg2)
  print(" Resultado:")
  print(f" {arg1} - {arg2} = {resultado}")

def case3():
  arg1,arg2 = inputs()
  resultado = calculadora.multiplicar(argumento1=arg1, argumento2=arg2)
  print(" Resultado:")
  print(f" {arg1} x {arg2} = {resultado}")

def case4():
  arg1,arg2 = inputs()
  resultado = calculadora.dividir(argumento1=arg1, argumento2=arg2)
  print(" Resultado:")
  print(f" {arg1} / {arg2} = {resultado}")


switch = {
  "0": case0,
  "1": case1,
  '2': case2,
  '3': case3,
  '4': case4,
}
operacao = -1

while operacao != "0":
  print("\n\n #### MENU #### ")
  print(" ! Escolha qual operação deseja realizar e digite sua opção abaixo ! ")
  print(" # 1 => SOMAR ")
  print(" # 2 => SUBTRAIR ")
  print(" # 3 => MULTIPLICAR ")
  print(" # 4 => DIVIDIR ")
  print(" ! Digite 0 para fechar o programa ! ")
  operacao = input("\n Qual operação deseja fazer?   ")
  
  case = switch.get(operacao)
  case()

  input("\n Pressione qualquer tecla para continuar...")
  
