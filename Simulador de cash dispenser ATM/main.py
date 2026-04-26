from datetime import datetime, timedelta, timezone

brasilia = timezone(timedelta(hours=-3))
data_atual = datetime.now(brasilia)
repetidor = "=" * 70


def atm(operacao):
    if operacao = 2:


    elif operacao = 1:


    elif operacao = 0:


def menu(data_hora):
    print(repetidor)
    print(f"UNICSUL - Simulador de Saque de ATM – versão 2026 {data_hora.strftime('%d/%m/%Y')}")
    print()
    print("0 – Mostrar quantidade de notas disponíveis de cada valor")
    print("1 – Abastecer ATM com quantidade de notas para cada valor")
    print("2 – Sacar dinheiro no ATM")
    print("9 – Sair")


while True:
    data_hora = datetime.now(brasilia)
    menu(data_hora)
    operacao = input("Escolha operação: ")

    if operacao == "9":
        print("Operação Encerrada")
        print(repetidor)
        break

    elif operacao in ("0", "1", "2"):
        operacao = int(operacao)
        atm(operacao)






    else:
        print("Opção Invalida")

