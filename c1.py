class Carro:
    def _init_(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano    
        
    def _str_(self):
        return f'{self.placa} {self.modelo} {self.ano}'