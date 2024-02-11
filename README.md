# Calculadora-IMC
Código para calcular el IMC de una persona

personas = int(input("Ingrese el número de personas: "))                                                #Se genera la variable personas para validar que haya al menos una persona a la cual se le calculará
                                                                                                         su IMC.
while personas > 0:
    nombre = input("Ingrese su nombre: ")                                                                #Antes del if se crean las variables para solicitar al usuario sus datos.
    apellido_paterno = input("Ingrese su apellido paterno: ")
    apellido_materno = input("Ingrese su apellido materno: ")

    if not (nombre.isalpha() and apellido_paterno.isalpha() and apellido_materno.isalpha()):             #El if esta verificando que los datos que ingrese el usuario sean del tipo correspondiente.
        print("Dato ingresado no válido. Por favor, use solo letras para los nombres y apellidos.")
        break
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso [kg]: "))
    estatura = float(input("Ingrese su estatura [m]: "))

    imc = peso / (estatura ** 2)                                                                         #Se crea la variable IMC que realiza la formula para calcular el IMC del usuario con sus valores
    if imc <= 18.5:                                                                                       correspondientes.
        print("Bajo_Peso")
    elif 18.5 <= imc and imc < 25.0:                                                                     #Se crean las condiciones para saber que tipo de peso tiene el usuario.
        print("Normal")
    elif 25.0 <= imc and imc < 30.0:
        print("Sobre_Peso")
    elif 30.0 <= imc and imc < 35.0:
        print("Obesidad_Leve")
    elif 35.0 <= imc and imc < 40.0:
        print("Obesidad_Media")
    elif imc >= 40.0:
        print("Obesidad_Mórbida")

    print(f"Su IMC es: {imc:.2f}")

    personas -= 1
                                                                                                          #Reflexión: El bootcamp me ha dejado el conocimiento de manejar las condiciones, a diferenciar los 
                                                                                                           tipos de datos y la creación de variables.
                                                                                                            
