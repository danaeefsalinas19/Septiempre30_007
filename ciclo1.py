#crear ciclo for que permita ingresar n temperaturas donde n es un numero ingresado por teclado
#mostrar cuantas temperaturas estan por sobre cero y cuantas estan bajo o igual a cero
#ejercicio atrasado

sobrecero=0
bajocero=0
veces_ int(input("¿Cuantas temperaturas quiere ingresar?: "))

for i in range(veces): # range tope
	tempe= float(input("Ingrese temperatura: "))
	if(tempe >0):
		sobrecero=sobrecero+1
	else:
		bajocero=bajocero+1

#mostrar datos
print("la cantidad de temperaturas mayores a cero es: " + str(sobrecero))
print("la cantidad de temperaturas menores o iguales a cero es: " + str(bajocero))


