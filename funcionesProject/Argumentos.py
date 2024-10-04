# ejemeplo de argumento predeterminado
def my_function (country = "Colombia"):
    print("I am from" + country)

#invocamos la funcion
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#argumento arbitrario *args
def mostrarEstudiantes(*args):
    print("El estudiante:" + args[2])
mostrarEstudiantes("Email","tobias","linus")

# Argumentos de palabras claves
def mostrarCarros (carro1, carro2, carro3):
    print("el carro es : " + carro3)
mostrarCarros(carro1= "BMW",carro3="FERRARI",carro2= "FORD")

#argumento arbitrario **kwargs
def mostrarCliente(**kwargs):
    print("su apellido es: " + kwargs["apellido"])
mostrarCliente(nombre = "tobias", apellido = "Resfsnes")