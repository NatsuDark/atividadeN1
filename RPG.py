#joguinho
#arrumar os textos
sala = 1
interacoes = 0
print("-" * 25)
print("\nBem vindo ao Jogo da Masmorra.\n")
print("-" * 25)
print("Nesse jogo, você e um grupo de heróis estão em uma corrida contra outras guildas.\n Vocês percorrerão por um labirinto, em busca de um tesouro sagrado.")
print("Lidere seu grupo até a sala 9, onde se encontra o tesouro, antes que outro grupo de heróis chegue antes e pegue todo o tesouro!")
while sala != 9 and interacoes < 7:
  if sala == 6:
print("Você se encontra na sala {}".format(sala))
input("Parece que essa sala só tem um unico caminho...\n[1] - Continuar\n")
sala = sala + 2
elif sala == 10:
    print("Antes que você desse conta, já era tarde demais. Ao abrir a porta, você e o seu grupo foram sugados por um portal. Você fecha os seus olhos.")
    print("Ao abrir os seus olhos novamente, você percebe que todo o seu grupo ainda estão no labirinto, porém estão mais longe do seu destino.")
    print("O portal fez você e seu time perderem tempo.")
    sala = random.randint(1,9)
  else:
    print("Você está na sala: {}".format(sala))
    caminhoEscolhido = int(input("Escolha seu caminho:\n[1] - Caminho vermelho\n[2] - Caminho preto\n"))
    sala = sala + caminhoEscolhido
  interacoes = interacoes + 1
if sala == 9:
  print("Ao entrar na sala, os seus olhos brilham. Vocês encontraram centenas de moedas de outro. Era o tesouro. Não há mais ninguém à vista, fora o seu grupo.")
  print("O mago do seu grupo logo se apressa, e abre um portal para a base do seu grupo. Vocês se apressam e transportam todo o ouro para lá.")
  print("Após vocês saquearem o tesouro e entrarem no portal, vocês ouvem a porta da sala se abrindo.")
  print("Vocês vêem um outro grupo de heróis que conseguiram chegar na sala, mas é tarde demais. Vocês fecham o portal, com um sorriso no rosto.")
  print("\nVOCÊ CONSEGUIU!")
else:
  print("Enquanto vocês vagavam pelo labirinto perdidos, vocês vêem um outro grupo de heróis indo na direção opostas ao seu grupo, com sacos de ouros.")
  print("Vocês sabem o que isso significava: eles encontraram o tesouro primeiro, e já o saquearam, vocês demoraram demais.")
  print("\nFIM DE JOGO")
