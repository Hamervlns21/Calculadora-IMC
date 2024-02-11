# #Calcular el IMC de una persona
# IMC           CLASIFICACION
# ---------------------------

# < 18.5        -> Bajo Peso
# 18.5 - 24.9   -> Normal
# 25.0 - 29.9   -> Sobre Peso
# 30.0 - 34.9   -> Obesidad Leve
# 35.0 - 39.9   -> Obesidad Media
# > 40.0        -> Obesidad Mórbida

personas = int(input("Ingrese el número de personas: "))

while personas > 0:
    nombre = input("Ingrese su nombre: ")
    apellido_paterno = input("Ingrese su apellido paterno: ")
    apellido_materno = input("Ingrese su apellido materno: ")

    if not (nombre.isalpha() and apellido_paterno.isalpha() and apellido_materno.isalpha()):
        print("Dato ingresado no válido. Por favor, use solo letras para los nombres y apellidos.")
        break
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso [kg]: "))
    estatura = float(input("Ingrese su estatura [m]: "))

    imc = peso / (estatura ** 2)
    if imc <= 18.5: 
        print("Bajo_Peso")
    elif 18.5 <= imc and imc < 25.0:
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