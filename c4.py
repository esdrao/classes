class Produtos:
    def init (self,nome,preco,qnt):
        self.nome = nome
        self.preco = preco
        self.qnt = qnt

    def atualizar(self):
        atual = self.qnt - 1
        if self.qnt > atual:
            self.qnt = atual
            return f'{atual}'
        else:
            pass
    def total_preco(self):
        total = self.preco * self.qnt
        return f'{total}'
    
if _name_ == 'main' :
    produto1 = Produtos('Iphone 15', 7000, 8)
    produto2 = Produtos('Samsung S24', 4000, 20)
    print(produto1.atualizar())
    print(produto1.total_preco())
    print(produto2.atualizar())
    print(produto2.total_preco())
    print(produto1.atualizar())
    print(produto1.total_preco())
    print(produto2.atualizar())
    print(produto2.total_preco())