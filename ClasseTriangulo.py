import math
class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perímetro(self):
        return self.a + self.b +  self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"

    def calcular_area(self):
        s = self.perímetro()/2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return round(area, 2) #Aproxima o valor a duas casas decimais

    def retangulo(self):
        lados = [self.a, self.b, self.c]
        lados.sort()
        return lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2 #Teorema de Pitágoras

def imprimir_detalhes(triangulo):
    print("Parâmetros do triângulo:", triangulo.a, triangulo.b, triangulo.c)
    print("Perímetro:", triangulo.perímetro())
    print("Tipo de triângulo:", triangulo.tipo_lado())
    print("Área do triângulo:",triangulo.calcular_area())
    print("É um triângulo retângulo?", triangulo.retangulo())
    print("_"*50)

triangulo = Triangulo(5,7,9)
triangulo2 = Triangulo(5,5,8)
triangulo3 = Triangulo(3,4,5)

imprimir_detalhes(triangulo)
imprimir_detalhes(triangulo2)
imprimir_detalhes(triangulo3)
