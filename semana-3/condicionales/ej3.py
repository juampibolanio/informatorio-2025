"""
Instrucciones:
1. Crea dos variables: `usuario_guardado` y `contrasena_guardada`. 
   Asígnales un nombre de usuario y una contraseña como strings.
2. Pide al usuario que ingrese su nombre de usuario con input() y guárdalo 
   en la variable `usuario_ingresado`.
3. Pide al usuario que ingrese su contraseña con input() y guárdala en la 
   variable `contrasena_ingresada`.
4. Escribe una condición que verifique si el `usuario_ingresado` es igual 
   al `usuario_guardado` Y si la `contrasena_ingresada` es igual a la 
   `contrasena_guardada`.
5. Si ambas condiciones son verdaderas, imprime "Acceso concedido. ¡Bienvenido!".
6. Si no, imprime "Error de autenticación. Usuario o contraseña incorrectos."

"""

print("=== INICIAR SESIÓN ===");

usuario_guardado = "juampibolanio";
contrasenia_guardada = "juampi123";

usuario = input("Ingrese su nombre de usuario >> ");

contrasenia = input("Ingrese su contraseña >> ");

if (usuario == usuario_guardado) and (contrasenia == contrasenia_guardada):
    print("Acceso concedido. ¡Bienvenido!");
else:
    print("Error de autenticación. Usuario o contraseña incorrectos.");