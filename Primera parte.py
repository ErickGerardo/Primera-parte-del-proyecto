import json
try:
    with open("datos_almacenados.json", "r") as archivo_db:
        print("Leyendo base de datos...")
        lista_estudiantes = json.load(archivo_db)
        print("Base de datos cargada exitosamente")
except:
    print("Creando nueva base de datos...")

lista_estudiantes = []
def calcular_promedio(lista_notas):
    total_suma = 0
    for nota in lista_notas:
        total_suma = total_suma + nota
    cantidad_notas = len(lista_notas)
    promedio = total_suma / cantidad_notas
    return promedio
def ingresar_nuevo_estudiante():
    nombre = input("Ingrese nombre: ")
    carnet = input("Ingrese carnet: ")
    lista_notas = []
    opcion_notas = input("Desea ingresar una nota? (y / n): ")
    while opcion_notas == 'y' or opcion_notas == 'Y':
        nueva_nota = input("Ingrese la nota: ")
        nueva_nota = int(nueva_nota)
        lista_notas.append(nueva_nota)
        opcion_notas = input("Desea ingresar otra nota? (y / n): ")
    promedio_estudiante = calcular_promedio(lista_notas)
    cursos = len(lista_notas)
    estudiante = {
        'Nombre': nombre,
        'Carnet': carnet,
        'Notas': lista_notas,
        'Promedio': promedio_estudiante,
        'Cursos asignados': cursos,
    }
    lista_estudiantes.append(estudiante)
    return
def numero_de_estudiantes():
    cantidad = len(lista_estudiantes)
    print(f'Numero de estudiantes ingresados: ', {cantidad})
    return
def mostrar_lista_estudiantes():
    print(lista_estudiantes)
    return
def menu():
    mensaje = """Ingrese la opcion que desea\n
    1. Ingresar un nuevo estudiante\n
    2. Ver la lista de estudiantes\n
    3. Mostrar la cantidad de estudiantes\n
    0. Salir\n
    > 
    """
    opcion = input(mensaje)
    opcion = int(opcion)
    print ("La opcion ingresada es: ", opcion)
    if opcion == 1:
        # ingresar un nuevo estudiante
        ingresar_nuevo_estudiante()
    if opcion == 2:
        # mostrar lista estudiantes
        mostrar_lista_estudiantes()
    if opcion == 3:
        # mostrar cantidad de estudiante
        numero_de_estudiantes()
    if opcion == 0:
        # salir
        print("Gracias :D")
        with open("datos_almacenados.json", "w") as archivo_db:
            print("Guardando base de datos...")
            json.dump(lista_estudiantes, archivo_db)
        return
    menu()
    return

menu()