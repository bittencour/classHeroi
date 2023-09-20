while True:
    nomeHeroi = input("Qual o nome do seu herói? ")
    if len(nomeHeroi) != 0:
        break
    else:
        print("Nome de Herói invalido, digite o nome, novamente")

nivelHeroi = int(input("Quantos XP seu herói possui? "))
if nivelHeroi <= 1000:
    print("O Herói de nome " + nomeHeroi + " está no nível de Ferro")
elif nivelHeroi <= 2000:
    print("O Herói de nome " + nomeHeroi + " está no nível de Bronze")
elif nivelHeroi <= 5000:
    print("O Herói de nome " + nomeHeroi + " está no nível de Prata")
elif nivelHeroi <= 7000:
    print("O Herói de nome " + nomeHeroi + " está no nível de Ouro")
elif nivelHeroi <= 8000:
    print("O Herói de nome " + nomeHeroi + " está no nível de Platina")
elif nivelHeroi <= 9000:
    print("O Herói de nome " + nomeHeroi + " está no nível de Ascendente")
elif nivelHeroi <= 10000:
    print("O Herói de nome " + nomeHeroi + " está no nível de Imortal")
elif nivelHeroi >= 10001:
    print("O Herói de nome " + nomeHeroi + " está no nível de Radiante")


