
import os

def Numeros():
	print("*** Opción de números ***")
	#ingresar n numeros, donde n es un numero ingresado por teclado, calcular y mostrar:
	#cantidad de numeros positivos, negativos, de iguales a cero
	veces=int(input("Cuantos numeros desea ingresar?: "))
	postivos=0
	negativos=0
	cero=0

	for x in range(veces):
		numero=int(input("Ingrese un número: "))
		if(numero>0):
			positivos=positivos+1
		elif(nume<0):
			negativos=negativos+1
		else:
			cero=cero+1


	print("Cantidad de números positivos: " + str(positivos)+
	"\nCantidad de números negativos: " + str(negativos)+
	"\nCantidad de números iguales a cero: " + str(cero))


	pausa=input("Presione una tecla para continuar")

def Datos():
	print("*** Opción de datos de personas ***")

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
		break
