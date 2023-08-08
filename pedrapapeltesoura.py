import random

def Jogador():
    escolha_jogador = input("Escolha entre Pedra, Papel ou Tesoura: ").strip().lower()
    while escolha_jogador not in ['pedra', 'papel', 'tesoura']:
        print("Escolha inválida. Tente novamente.")
        escolha_jogador = input("Escolha entre Pedra, Papel ou Tesoura: ").strip().lower()
    return escolha_jogador

def Computador():
    escolha_pc = ['pedra', 'papel', 'tesoura']
    return random.choice(escolha_pc)

def Vencedor(escolha_jogador, escolha_pc):
    if escolha_jogador == escolha_pc:
        return 'Empate'
    elif (escolha_jogador == 'pedra' and escolha_pc == 'tesoura') or \
         (escolha_jogador == 'papel' and escolha_pc == 'pedra') or \
         (escolha_jogador == 'tesoura' and escolha_pc == 'papel'):
        return 'Você venceu!'
    else:
        return 'Você perdeu!'

def Inicio():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    
    while True:
        print("\nMENU:")
        print("1. Jogar")
        print("2. Sair")
        choice = input("Escolha uma opção (1 ou 2): ").strip()

        if choice == '1':
            escolha_jogador = Jogador()
            escolha_pc = Computador()
            print(f"\nVocê escolheu: {escolha_jogador}")
            print(f"O computador escolheu: {escolha_pc}\n")
            resultado = Vencedor(escolha_jogador, escolha_pc)
            print(resultado)
        elif choice == '2':
            print("Terminamos por aqui!")
            print("Obrigado por jogar!!.")
            break
        else:
            print("Opção inválida. Escolha 1 ou 2.")

if __name__ == "__main__":
    Inicio()
