
#lista ordenada desde el 0 ej: duna2 = 0 - ciencia ficcion = 1 - 165 = 2 - pg-13 = 3
peliculas = {
    'MOV001': ['Duna 2', 'Ciencia Ficción', 165, 'PG-13'],
    'MOV002': ['Barbie', 'Comedia', 114, 'APT'],
    'MOV003': ['Oppenheimer', 'Drama', 180, '+18'],
    'MOV004': ['Spider-Man: No Way Home', 'Acción', 148, 'PG-13'],
    'MOV005': ['Coco', 'Animación', 105, 'APT']
}
#lista ordenada desde 0 ej: 4500 = 0 - 25 = 1
funciones = {
    'MOV001': [4500, 25],
    'MOV002': [3500, 40],
    'MOV003': [5000, 10],
    'MOV004': [4000, 35],
    'MOV005': [3000, 50]
}
#FUNCIONES DE MI MENU
#OPC1
def mostrar_por_clasificacion(clasificacion):
    clasificacion = clasificacion.upper()  # Ignorar may/min
    print(f"\nPelículas con clasificación {clasificacion}:\n")
    encontrada = False

    for codigo, datos in peliculas.items():
        if datos[3].upper() == clasificacion:
            print(f"Código: {codigo} | Nombre: {datos[0]} | Asientos: {funciones[codigo][1]}")
            encontrada = True

    if not encontrada:
        print("No se encontraron películas con esa clasificación.")
#OPC2
# Función auxiliar para obtener el precio
def obtener_precio(item):
    return item[1][0]  # item = ('MOV001', [4500, 25]) → precio = 4500

# OPC2 
def buscar_por_precio(p_min, p_max):
    print("\nPelículas en orden ascendente:\n")
    # Filtrar solo las funciones en el rango
    resultados = [
        (codigo, datos) for codigo, datos in funciones.items()
        if p_min <= datos[0] <= p_max
    ]
    resultados.sort(key=obtener_precio) #nidea use chatgpt :(
    if resultados:
        for codigo, datos in resultados:
            print(f"Código: {codigo} | Nombre: {peliculas[codigo][0]} | Precio: {datos[0]:.0f} | Asientos: {datos[1]}")
    else:
        print("No hay funciones en ese rango de precios.")
    


#OPC 3
def actualizar_precio(codigo, nuevo_precio):
        print("¡Precio actualizado con éxito!")
        funciones[codigo][0] = nuevo_precio
        print(f"\n Pelicula actualizada: Codigo: {codigo} | Nombre: {peliculas[codigo][0]} ! Nuevo precio: {funciones[codigo][0]:.0f}")
        

def menu_principal():
    while True:
        print("""
            ---CinePlus - Gestión de Cine---
                *** MENÚ PRINCIPAL ***
        1. Mostrar funciones por clasificación
        2. Buscar funciones por precio
        3. Actualizar precio de función
        4. Salir
        """)
        try:
            opc_menu = int(input("Ingrese una opción: "))
        except ValueError:
            print("ERROR: Formato inválido.")
            input("Presione ENTER para continuar...")
            continue
        if opc_menu not in [1,2,3,4]:
            print("ERROR: Opción Inválida.")
            input("Presione ENTER para continuar...")
            continue
        elif opc_menu == 4:
            print("Programa finalizado. ¡Gracias por usar CinePlus!")
            break
        elif opc_menu == 1:
            entrada = input("Ingrese una clasificación (APT, PG-13, +18): ")
            mostrar_por_clasificacion(entrada)
        elif opc_menu == 2:
            try:
                minimo = float(input("Precio mínimo: "))
                maximo = float(input("Precio máximo: "))
                if minimo > maximo:
                    print("El mínimo no puede ser mayor que el máximo.")
                else:
                    buscar_por_precio(minimo, maximo)
            except ValueError:
                print("Debe ingresar valores enteros!!")
                input("Presione ENTER para continuar...")
                continue
        elif opc_menu == 3:
            op_tres = True
            while op_tres:
                codigo = input("Escribe el codigo de la pelicula (ej:MOV001 ): ").upper()
                if codigo not in peliculas:
                    print("El código de la película no existe.")
                    input("Presione ENTER para continuar...")
                    break
                else:
                    try:
                        precio_n = float(input(f"Escriba el nuevo precio para {peliculas[codigo][0]}: "))
                    except ValueError:
                        print("ERROR: Debe ingresar valores Enteros.")
                        input("Presione ENTER para continuar...")
                        continue
                    if precio_n <= 0:
                        print("El precio debe ser mayor a cero.")
                        continue
                    else:
                        actualizar_precio(codigo, precio_n)
                        while True:
                            repetir = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                            if repetir == "s":
                                break  
                            elif repetir == "n":
                                op_tres = False
                                break 
                            else:
                                print("ERROR: Opción inválida.")


#programa principal
menu_principal()

