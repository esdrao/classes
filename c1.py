import time

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor    
    
    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano} {self.cor}'
   
    def ligar():
        print('seu carro está iniciando')
    
    def acelear():
        print('seu carro esta acelerando')
    
    def desligar():
        print('seu carro está desligando')
    
    


if __name__ == "__main__":
    carro1 = Carro('fiat', 'uno', 2022, 'azul')
    print(carro1)
    time.sleep(1)
    Carro.ligar()
    time.sleep(1)
    Carro.acelear()
    time.sleep(1)
    Carro.desligar