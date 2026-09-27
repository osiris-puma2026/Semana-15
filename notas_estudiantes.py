# Programa para registrar las notas de estudiantes

# Diccionario para almacenar los nombres y las notas
estudiantes = {}

while True:
    print("\n--- REGISTRO DE ESTUDIANTES ---")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar un estudiante
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = input("Ingrese la nota del estudiante: ")

        estudiantes[nombre] = nota
        print("Estudiante agregado correctamente.")

    # Mostrar los estudiantes
    elif opcion == "2":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nEstudiantes registrados:")
            for nombre, nota in estudiantes.items():
                print("Estudiante:", nombre, "- Nota:", nota)

    # Buscar un estudiante
    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante que desea buscar: ")

        if nombre in estudiantes:
            print("Estudiante encontrado.")
            print("Estudiante:", nombre)
            print("Nota:", estudiantes[nombre])
        else:
            print("El estudiante no existe.")

    # Salir del programa
    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")