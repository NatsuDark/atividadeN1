#joguinho
#arrumar os textos
sala = 1
interacoes = 0
print("bla bla bla do começo\n")
while sala != 9 and interacoes < 7:
  if sala == 6:
print("Você está na sala: {}".format(sala))
input("Parece que essa sala só tem um unico caminho\n[1] - Continuar\n")
sala = sala + 2
elif sala == 10:
    print("Você acessou um portal mágico e será teletransportado para outra sala anterior")
    sala = random.randint(1,9)
  else:
    print("Você está na sala: {}".format(sala))
    caminhoEscolhido = int(input("Escolha seu caminho:\n[1] - Caminho vermelho\n[2] - Caminho preto\n"))
    sala = sala + caminhoEscolhido
  interacoes = interacoes + 1
if sala == 9:
  print("você conseguiu!")
else:
  print("f")
