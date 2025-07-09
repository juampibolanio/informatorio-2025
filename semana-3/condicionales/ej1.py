
#Ejercicio 1: Verificación de Edad para Entrar a un Club 

#Crea una variable llamada edad y asígnale un número entero (por ejemplo, la edad de una persona).

#Escribe una condición que verifique si la edad es mayor o igual a 18.

#Si la condición es verdadera, imprime un mensaje que diga: "Puedes pasar al club."

#Si la condición es falsa, imprime un mensaje que diga: "Lo siento, no puedes pasar. Eres menor de edad."

print("Verificación de edad para entrar a un club");

try:
    edad = int(input("Ingrese su edad: "));
    if edad >= 18:
        print("Usted es mayor de edad, puede pasar");
    else:
        print("Lo sentimos, usted es menor de edad, no puede pasar.");
except: 
    print("Debe ingresar un número válido.")