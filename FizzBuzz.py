print("Digite um valor entre 0 e 100")
Valor = input()

if int(Valor)>100 or int(Valor)<0:
 print("Erro:Digite um valor entre 0 e 100")

elif int(Valor) == 0:
  print(0)

elif ((int(Valor) % 3 == 0) and (int(Valor) % 5 == 0)):
  print("FizzBuzz")

elif int(Valor) % 3 == 0:
  print("Fizz")

elif int(Valor) % 5 == 0:
  print("Buzz")

else:
 print(Valor)