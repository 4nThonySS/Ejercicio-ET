juegos = {
    'C001': ['Catan', 'Devir', 'Estrategia', 3, 4],
    'C002': ['Dixit', 'Libellud', 'Creatividad', 3, 6],
    'C003': ['Carcassonne', 'Z-Man Games', 'Estrategia', 2, 5],
    'C004': ['Uno', 'Mattel', 'Familiar', 2, 10],
    'C005': ['Terraforming Mars', 'Stronghold Games', 'Estrategia', 1, 5],
    'C006': ['Jungle Speed', 'Asmodee', 'Reflejos', 2, 8],
}
#juegos: codigo: [nombre, editorial, tipo, min_jugadores, max_jugadores]
#inventario: codigo: [precio, stock disponible]
inventario = {
    'C001': [29990, 8],
    'C002': [18990, 5],
    'C003': [25990, 0],
    'C004': [6990, 20],
    'C005': [39990, 3],
    'C006': [15990, 10],
}

def stock_editorial(editorial):
    editorial = editorial.lower()
    total_stock = 0

    for codigo, datos in juegos.items():
        if datos[1].lower() == editorial:
            stock = inventario[codigo][1]
            total_stock += stock

    if total_stock == 0:
        print("No se encontraron juegos para esa editorial.")
    else:
        print(f"Stock total de la editorial '{editorial}': {total_stock}")


def busqueda_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return

    resultados = []

    for codigo, datos in inventario.items():
        precio, stock = datos
        if p_min <= precio <= p_max and stock > 0:
            nombre = juegos[codigo][0]
            resultados.append(f"{nombre} -- {codigo}")

    if not resultados:
        print("No hay juegos en ese rango de precios.")
    else:
        resultados.sort()
        print("Juegos encontrados:")
        for juego in resultados:
            print(juego)


def programa():
    while True:
        print("""
            *** MENÚ PRINCIPAL ***
        1. Stock por editorial
        2. Búsqueda por precio
        3. Actualizar precio
        4. Salir
              """)
        try:
            opc_menu = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: Formato Inválido.")
            continue
        if opc_menu not in [1,2,3,4]:
            print("ERROR: Opción Inválida.")
            continue
        elif opc_menu == 4:
            print("Finalizando programa.")
            break
        elif opc_menu == 3:
            print("Actualizar")
        elif opc_menu == 2:
            p_min = input("Ingrese el precio mínimo: ")
            p_max = input("Ingrese el precio máximo: ")
            busqueda_precio(p_min, p_max)
        else:
            edit = input("Escribe el nombre de alguna editorial: ")
            stock_editorial(edit)







programa()