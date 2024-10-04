#Ejemplo para calcular el area del triangulo

#creo las entradas
base = int (input("ingrese la base del triangulo:"))
altura  = int (input("ingrese la altura del triangulo:"))

#creo el proceso
def calcularAreaTriangulo(a,b):
    area = (b*a)/2
    #print("el area del trinagulo es :", area)
    return area

resultado= calcularAreaTriangulo(base,altura) + 4 #me puede retornar una funcion
print(f"el area del triangulo es:  {resultado}") # se puede con ,


