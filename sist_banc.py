class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        self.saldo += valor
        self.depositos.append(valor)

    def saque(self, valor):
        if self.saldo >= valor and len(self.saques) < 3 and valor <= 500:
            self.saldo -= valor
            self.saques.append(valor)
        else:
            print("Não foi possível realizar o saque.")

    def extrato(self):
        print("Extrato bancário:")
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Programa principal
if __name__ == "__main__":
    sistema = SistemaBancario()
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
            sistema.deposito(valor)
            print("Depósito realizado com sucesso!")

        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            sistema.saque(valor)

        elif opcao == 3:
            sistema.extrato()

        elif opcao == 0:
            break

        else:
            print("Opção inválida!")

    print("\nEncerrando o programa...")
