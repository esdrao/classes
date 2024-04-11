class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def __str__(self):
        return f'{self.nome} {self.idade} {self.especie}'
    
    def menu():
        print('''====Animais====
1 = Cachorros
2 = Gatos''')

    def som(animal):
        if animal == 1:
            print('Au au')
        elif animal == 2:
            print('Miau')

if __name__ == "__main__":
    Animal.menu()

    res = int(input())

    Animal.som(res)