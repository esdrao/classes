class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
       

    def __str__(self):
        return f'{self.nome} {self.idade} {self.altura}'   
    
if __name__ == "__nome__":
    p1 =  input('diga seu nome: ')   
    pessoa = Pessoa(p1 , 17, 1.85)

 print(pessoa)         