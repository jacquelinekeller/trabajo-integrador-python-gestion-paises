# Trabajo Integrador Obligatorio
# Integrantes: Jacqueline Keller, Lautaro Lavallen
# Comisión 24

# Cargar datos desde el archivo csv
def cargar_csv(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            # Ignorar líneas vacías
            if linea == "":
                continue
            datos = linea.split(",")

            # Verificar cantidad de campos
            if len(datos) != 4:
                print(f"\nError en formato de línea {i + 1}. Registro omitido.")
                continue
            try:
                pais = {
                    "nombre": datos[0].strip().title(),
                    "poblacion": int(datos[1]),
                    "superficie": int(datos[2]),
                    "continente": datos[3].strip().title()
                }
                paises.append(pais)
            except ValueError:
                print(f"\nError de datos en línea {i + 1}. Registro omitido.")
        print("\nArchivo cargado exitosamente.")
    except FileNotFoundError:
        print("\nNo se encontró el archivo.")
    return paises

# Guardar cambios en el archivo csv
def guardar_csv(nombre_archivo, lista_paises):
    try:
        with open(nombre_archivo, mode="w", encoding="utf-8") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")

            for pais in lista_paises:
                linea = (
                    f"{pais['nombre']},"
                    f"{pais['poblacion']},"
                    f"{pais['superficie']},"
                    f"{pais['continente']}\n"
                )
                archivo.write(linea)
        print("\nCambios guardados correctamente.")
    except OSError:
        print("\nError al guardar el archivo.")

# Validar opción de menú
def validar_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print("\nError: opción inválida.")

# Validar número entero positivo
def validar_entero_positivo(mensaje, permitir_vacio=False):
    while True:
        entrada = input(mensaje).strip()

        if permitir_vacio and entrada == "":
            return ""
        try:
            numero = int(entrada)
            if numero > 0:
                return numero
            print("\nError: el valor debe ser mayor a 0.")
        except ValueError:
            print("\nError: ingrese un número entero válido.")

# Validar continente
def validar_continente(mensaje, permitir_vacio=False):

    continentes_validos = ["america", "europa", "asia", "africa", "oceania", "antartida"]

    while True:
        continente = input(mensaje).strip().title()
        if permitir_vacio and continente == "":
            return ""
        if continente == "":
            print("\nError: el continente no puede estar vacío.")
            continue
        if continente.lower() in continentes_validos:
            return continente
        print("\nError: continente inválido.")

# Mostrar menú principal
def mostrar_menu():
    print("\n==== GESTIÓN DE PAÍSES ====")
    opciones = [
        "Mostrar países",
        "Agregar país",
        "Actualizar país",
        "Buscar país",
        "Filtrar países",
        "Ordenar países",
        "Mostrar estadísticas",
        "Guardar cambios",
        "Salir"
    ]

    for i in range(len(opciones)):
        print(f"{i + 1}- {opciones[i]}")
    opcion = validar_opcion("Seleccione una opción: ", ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    return opcion


# Mostrar lista de países
def mostrar_paises(lista_paises):

    if len(lista_paises) == 0:
        print("\nNo hay países para mostrar.")
        return
    print("\n=== LISTA DE PAÍSES ===")
    for pais in lista_paises:
        print(f"Nombre: {pais['nombre']}")
        print(f"Continente: {pais['continente']}")
        print(f"Población: {pais['poblacion']} habitantes")
        print(f"Superficie: {pais['superficie']} km2")
        print("-" * 40)

# Buscar si un país existe
def existe_pais(lista_paises, nombre):
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            return pais
    return None

# Agregar país
def agregar_pais(lista_paises):
    print("\n=== AGREGAR PAÍS ===")

    while True:
        nombre = input("Ingrese el nombre del país: ").strip().title()
        if nombre == "":
            print("\nError: el nombre no puede estar vacío.")
        elif existe_pais(lista_paises, nombre):
            print("\nError: este país ya está cargado.")
        else:
            break

    continente = validar_continente("Ingrese el continente: ")
    poblacion = validar_entero_positivo("Ingrese la población: ")
    superficie = validar_entero_positivo("Ingrese la superficie (km2): ")
    nuevo_pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}

    lista_paises.append(nuevo_pais)
    print("\nPaís agregado correctamente.")

# Actualizar país
def actualizar_pais(lista_paises):
    print("\n=== ACTUALIZAR PAÍS ===")

    # Repetir hasta encontrar país o cancelar
    while True:
        nombre = input("Ingrese el nombre del país a modificar (o ENTER para salir): ").strip().title()

        if nombre == "":
            print("\nActualización cancelada.")
            return

        pais = existe_pais(lista_paises, nombre)

        if pais:
            break
        else:
            print("\nError: país no encontrado. Intente nuevamente.")

    print("\nDeje vacío si no desea modificar el valor.")
    print(f"Población actual: {pais['poblacion']}")
    print(f"Superficie actual: {pais['superficie']}")
    print(f"Continente actual: {pais['continente']}")

    # Modificar población
    nueva_poblacion = validar_entero_positivo("Nueva población: ", permitir_vacio=True)
    if nueva_poblacion != "":
        pais["poblacion"] = nueva_poblacion

    # Modificar superficie
    nueva_superficie = validar_entero_positivo("Nueva superficie (km2): ", permitir_vacio=True)
    if nueva_superficie != "":
        pais["superficie"] = nueva_superficie

    # Modificar continente
    nuevo_continente = validar_continente("Nuevo continente: ", permitir_vacio=True)
    if nuevo_continente != "":
        pais["continente"] = nuevo_continente

    print("\nPaís actualizado correctamente.")


# Buscar país
def buscar_pais(lista_paises):
    print("\n=== BUSCAR PAÍS ===")

    while True:
        nombre = input("Ingrese el nombre del país (o ENTER para salir): ").strip().title()

        if nombre == "":
            print("\nBúsqueda cancelada.")
            return
        
        pais = existe_pais(lista_paises, nombre)
        if pais:
            mostrar_paises([pais])
            return  # termina cuando lo encuentra
        else:
            print("\nError: país no encontrado. Intente nuevamente.")

# Filtrar países
def filtrar_paises(lista_paises):
    print("\n=== FILTRAR PAÍSES ===")
    print("1- Filtrar por continente")
    print("2- Filtrar por población mínima")
    print("3- Filtrar por superficie mínima")

    opcion = validar_opcion("Seleccione una opción: ", ["1", "2", "3"])
    resultados = []

    # Filtrar por continente
    if opcion == "1":
        continente = validar_continente("Ingrese el continente: ")

        for pais in lista_paises:
            if pais["continente"].lower() == continente.lower():
                resultados.append(pais)

    # Filtrar por población mínima
    elif opcion == "2":
        poblacion_minima = validar_entero_positivo("Ingrese la población mínima: ")

        for pais in lista_paises:
            if pais["poblacion"] >= poblacion_minima:
                resultados.append(pais)

    # Filtrar por superficie mínima
    elif opcion == "3":
        superficie_minima = validar_entero_positivo("Ingrese la superficie mínima: ")

        for pais in lista_paises:
            if pais["superficie"] >= superficie_minima:
                resultados.append(pais)

    if len(resultados) == 0:
        print("\nNo se encontraron países.")
    else:
        mostrar_paises(resultados)

# Ordenar países
def ordenar_paises(lista_paises):
    print("\n=== ORDENAR PAÍSES ===")
    print("1- Ordenar por nombre")
    print("2- Ordenar por población")
    print("3- Ordenar por superficie")
    opcion = validar_opcion("Seleccione una opción: ", ["1", "2", "3"])

    print("\n1- Ascendente")
    print("2- Descendente")
    orden = validar_opcion("Seleccione el orden: ", ["1", "2"])

    # Asociar cada opción con una clave del diccionario
    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    clave = claves[opcion]

    # Crear una copia de la lista
    lista_ordenada = lista_paises.copy()
    n = len(lista_ordenada)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            valor1 = lista_ordenada[j][clave]
            valor2 = lista_ordenada[j + 1][clave]

            # Para nombres se comparan en minúsculas
            if clave == "nombre":
                valor1 = valor1.lower()
                valor2 = valor2.lower()
            intercambio = False

            if orden == "1":
                if valor1 > valor2:
                    intercambio = True
            else:
                if valor1 < valor2:
                    intercambio = True
            if intercambio:
                auxiliar = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j + 1]
                lista_ordenada[j + 1] = auxiliar

    mostrar_paises(lista_ordenada)

# Mostrar estadísticas
def mostrar_estadisticas(lista_paises):
    print("\n=== ESTADÍSTICAS ===")

    if len(lista_paises) == 0:
        print("\nNo hay países cargados.")
        return
    cantidad_paises = len(lista_paises)

    suma_poblacion = 0
    suma_superficie = 0

    pais_mayor_poblacion = lista_paises[0]
    pais_mayor_superficie = lista_paises[0]

    for pais in lista_paises:
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = pais

        if pais["superficie"] > pais_mayor_superficie["superficie"]:
            pais_mayor_superficie = pais

    promedio_poblacion = suma_poblacion / cantidad_paises
    promedio_superficie = suma_superficie / cantidad_paises

    print(f"\nCantidad de países: {cantidad_paises}")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print( f"País con mayor población: " f"{pais_mayor_poblacion['nombre']} " f"({pais_mayor_poblacion['poblacion']} habitantes)")
    print(f"País con mayor superficie: " f"{pais_mayor_superficie['nombre']} " f"({pais_mayor_superficie['superficie']} km2)")

# PROGRAMA PRINCIPAL
# Cargar datos del archivo
paises = cargar_csv("paises.csv")

# Ciclo principal del programa
while True:
    opcion = mostrar_menu()

    if opcion == "1":
        mostrar_paises(paises)
    elif opcion == "2":
        agregar_pais(paises)
    elif opcion == "3":
        actualizar_pais(paises)
    elif opcion == "4":
        buscar_pais(paises)
    elif opcion == "5":
        filtrar_paises(paises)
    elif opcion == "6":
        ordenar_paises(paises)
    elif opcion == "7":
        mostrar_estadisticas(paises)
    elif opcion == "8":
        guardar_csv("paises.csv", paises)
    elif opcion == "9":
        guardar = input("\n¿Desea guardar los cambios antes de salir? (S/N): ").strip().upper()

        if guardar == "S":
            guardar_csv("paises.csv", paises)
        print("\nFin del programa.")

        break