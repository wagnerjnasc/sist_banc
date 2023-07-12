class Banco:
    def __init__(self):
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def extrato(self):
        print("Saldo atual: ", self.saldo)


# Programa principal
if __name__ == "__main__":
    banco = Banco()
    print("Sistema Bancário")

    while True:
        print("\nOperações disponíveis:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("0 - Sair")

        opcao = int(input("Selecione uma operação: "))

        if opcao == 1:
            valor = float(input("Informe o valor do depósito: "))
            banco.deposito(valor)
            print("Depósito realizado com sucesso!")

        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            banco.saque(valor)

        elif opcao == 3:
            banco.extrato()

        elif opcao == 0:
            break

        else:
            print("Opção inválida!")

    print("\nEncerrando o programa...")
