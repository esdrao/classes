class Conta_bancária:
    def _init_(self, numero_conta, saldo, titular):
        self.numero_conta= numero_conta
        self.saldo= saldo
        self.titular= titular

    def depositar(self):
        deposito = int(input("Quanto dinheiro você deseja depositar?: R$"))
        self.saldo += deposito
        return f"O deposito inserido foi de R${deposito}."
    
    def sacar(self):
        saque = int(input("Quanto você quer sacar?: R$"))
        self.saldo -= saque
        return f"O dinheiro que será sacado é de R$ {saque}."
    
    def saldo(self):
        return f"O valor atual do titular {self.titular} é R${self.saldo}."
    
if _name_ == '_main_':
    Pedro = Conta_bancária("12345",30,"Pedro")
    Berg = Conta_bancária("6789", 100,"Berg")

    print(Pedro.depositar())
    print(Berg.sacar())