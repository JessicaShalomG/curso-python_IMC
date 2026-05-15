nombre = input("Por favor escribe tu primer nombre: ")

apellido_paterno = input("Por favor escribe tu apellido paterno: ")

apellido_materno = input("Por favor escribe tu apellido materno: ")

edad = int(input("Por favor escribe tu edad en numero: "))

estatura = float(input ("ahora, su estatura en metros por favor: "))

peso = float (input("cual es su peso en kilogramos?:"))


if not nombre :
    print("por favor escribe tu nombre")
elif not apellido_paterno:
    print ("por favor escribe tu apellido paterno")
elif not apellido_materno:
    print ("por favor escribe tu apellido materno")
elif edad :
    print ("por favor escribe tu edad")    
elif estatura :
    print ("por favor escribe tu estatura")    
elif peso :
    print ("por favor escribe tu peso")    

    
else:
    print("ok. vamos a calcular tu IMC")

#Calculo del IMC,con la formula proporcionada 
IMC = peso / estatura**2
print(f"Bueno, {nombre} {apellido_paterno} {apellido_materno}, tu IMC es: {IMC}" )

#Hacemos las distintas validaciones
if IMC >= 0 and IMC <= 15.99 :
    print ("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
    print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
    print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
    print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
    print ("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
    print ("obesidad media")
elif IMC >= 40.00:
    print ("obesidad morbida")