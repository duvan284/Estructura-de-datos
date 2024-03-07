class Rectangulo :
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho
    def calcular_perimetro(self):
        return (self.longitud + self.ancho) * 2
rect1 = Rectangulo(5,3)
print(f"area : {rect1.calcular_area()}")
print(f"perimetro : {rect1.calcular_perimetro()}")
