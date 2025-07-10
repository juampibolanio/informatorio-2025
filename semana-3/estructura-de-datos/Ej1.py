# -----------------------------------------------------------------------------
# Ejercicio 1: Lista de Tareas (Listas) 📝
# -----------------------------------------------------------------------------
"""
Instrucciones:
1. Crea una lista vacía llamada `tareas`.
2. Usa el método `.append()` para agregar tres tareas (strings) a la lista.
   Por ejemplo: "Estudiar Python", "Hacer la compra", "Llamar al dentista".
3. Muestra todas las tareas de la lista usando un bucle `for`.
4. Simula que completaste la segunda tarea. Usa el método `.remove()` para
   eliminarla de la lista.
5. Imprime la lista de tareas actualizada para ver el resultado.

"""

print("=== MI LISTA DE TAREAS ===");
tareas = [];

def listarTareas(tareas):
    for tarea in tareas:
        print(tarea);

print("=========================");
print("Vacio")
listarTareas(tareas);

tareas.append("Limpiar la casa.");
tareas.append("Estudiar programación.");
tareas.append("Sacar a pasear a los perros.");
tareas.append("Ir al supermercado.");

print("=========================");

listarTareas(tareas);

print("=========================");

tareas.remove("Limpiar la casa.");

listarTareas(tareas)
