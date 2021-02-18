print("Digite pedra, papel ou tesoura!")
p1 = input()
p2 = input()

if p1 == p2:
  print("Empate")

elif p1=="pedra" and p2=="tesoura":
  print("jogador 1 ganha!")


elif p1=="tesoura" and p2=="pedra":
  print("jogador 2 ganha!")

elif p1=="tesoura" and p2=="papel":
  print("jogador 1 ganha!")

elif p1=="papel" and p2=="tesoura":
  print("jogador 2 ganha!")
  
elif p1=="papel" and p2=="pedra":
  print("jogador 1 ganha!")

elif p1=="pedra" and p2=="papel":
  print("jogador 2 ganha!")