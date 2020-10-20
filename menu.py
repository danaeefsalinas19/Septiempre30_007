
import os

def Numeros():
	print("*** Opción de números ***")
	#ingresar n numeros, donde n es un numero ingresado por teclado, calcular y mostrar:
	#cantidad de numeros positivos, negativos, de iguales a cero
	veces=int(input("Cuantos numeros desea ingresar?: "))
	positivos=0
	negativos=0
	cero=0

	for x in range(veces):
		numero=int(input("Ingrese un número: "))
		if(numero>0):
			positivos=positivos+1
		elif(numero<0):
			negativos=negativos+1
		else:
			cero=cero+1


	print("Cantidad de números positivos: " + str(positivos)+
	"\nCantidad de números negativos: " + str(negativos)+
	"\nCantidad de números iguales a cero: " + str(cero))


	pausa=input("Presione una tecla para continuar")


def Datos():
	print("*** Opción de datos de personas ***")

    #ingresar para n personas donde n es un número ingresado por teclado: nombre y edad. 
    #calcular y mostrar: cantidad de personas mayores de edad y cantidad de menores de edad. 
    #subir la modificación a github con el siguiente mensaje: "se programo la opción 2 del menú"

	personas=int(input("Cuantas personas desea ingresar?: "))
	mayores=0
	menores=0

	for n in range(personas):
		edad=int(input("Ingrese edad: "))
		if (edad>=18):
			mayores=mayores+1
		elif(edad<=17):
			menores=menores+1

	print("Cantidad de personas mayores de edad: " + str(mayores)+
	"\nCantidad de personas menores de edad: " + str(menores))
	




	pausa=input("Presione una tecla para continuar")

seguir=True
while(seguir):
	os.system('cls')
	print("1.Opción números")
	print("2.Opción datos de personas")
	print("3.Finalizar")
	op=int(input("Ingrese opción 1,2,3: "))
	if(op==1):
		Numeros()   	#invocamos a una funcion o def
	if(op==2):
		Datos() 		#invocamos a una funcion o def 
	if(op==3):
		seguir=False
		breaks

