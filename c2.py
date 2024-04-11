class Animal:
    def _init_(self, nome, idade, espécie):
        self.nome= nome
        self.idade= idade
        self.espécie= espécie
     
    def emitir(self):
        return f"{self.nome} ROAAAAR"
 
    def informar(self):
        return f"{self.nome}, {self.idade}, {self.espécie}"
    
if _name_ == '_main_':
    leao = Animal("jujuba","30","leão")
    cachorro = Animal("mel", "4","cachorro")
    
    print(leao.emitir())
    print(leao.informar())
    print(cachorro.informar())