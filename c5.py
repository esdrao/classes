class Triangulo:
    def init (self,base,altura1,altura2):
        self.base = base
        self.altura1 = altura1
        self.altura2 = altura2

    def area(self):
        if self.altura1 >= self.altura2:
            return f'{(self.base * self.altura1)/ 2}'
        elif self.altura2 > self.altura1:
            return f'{(self.base * self.altura2)/ 2}'
    
    def perimetro(self):
        return f'{self.base + self.altura1 + self.altura2}'
            

if _name_ == 'main':
    triangulo1 = Triangulo(7,7,7)
    triangulo2 = Triangulo(7,9,8)
    triangulo3 = Triangulo(7,10,9)
    
    print(triangulo1.area())
    print(triangulo1.perimetro())
    print(triangulo2.area())
    print(triangulo2.perimetro())
    print(triangulo3.area())
    print(triangulo3.perimetro())