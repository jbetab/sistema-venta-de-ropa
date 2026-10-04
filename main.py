from prenda_dama import PrendaDama
from prenda_caballero import PrendaCaballero
from venta import Venta
from tienda import Tienda


# funciones para leer los datos
def leer_texto(mensaje):
    #Pide un texto y lo vuelve a pedir si esta vacio
    texto = input(mensaje).strip()
    while texto == "":
        print("Este dato no puede estar vacío.")
        texto = input(mensaje).strip()
    return texto


def leer_entero(mensaje):
    #Pide un número entero y lo vuelve a pedir si esta mal
    texto = input(mensaje).strip()
    while not texto.isdigit():
        print("Escribe un número entero valido (sin signos ni decimales)")
        texto = input(mensaje).strip()
    return int(texto)


def titulo(texto):
    #Imprime un encabezado para separar cada sección
    print()
    print("=" * 60)
    print(texto)
    print("=" * 60)


# OPCIONES DEL MENU
def registrar_producto(tienda):
    # Opción 1: pide los datos y registra un producto de dama o de caballero
    titulo("Registrar producto")

    # El género decide de qué clase hija se crea el objeto
    print("Tipo de prenda:")
    print("  1. Dama")
    print("  2. Caballero")
    genero = leer_entero("Elige 1 o 2: ")
    while genero != 1 and genero != 2:
        print("Opción inválida")
        genero = leer_entero("Elige 1 o 2: ")

    # Se pide un código que no esté repetido
    codigo = leer_texto("Código del producto (ej D01): ").upper()
    while tienda.buscar_producto(codigo) is not None:
        print("Ya existe un producto con ese código")
        codigo = leer_texto("Escribe otro código: ").upper()

    nombre = leer_texto("Nombre: ")
    categoria = leer_texto("Categoría (ej Camisas, Pantalones, Vestidos): ").capitalize()

    # El precio debe ser mayor que 0
    precio = leer_entero("Precio (sin IVA): ")
    while precio <= 0:
        print("El precio debe ser mayor que 0")
        precio = leer_entero("Precio (sin IVA): ")

    stock = leer_entero("Cantidad en stock: ")

    # Se crea el objeto de la clase que corresponde según el género
    if genero == 1:
        producto = PrendaDama(codigo, nombre, categoria, precio, stock)
    else:
        producto = PrendaCaballero(codigo, nombre, categoria, precio, stock)

    tienda.registrar_producto(producto)
    print("Producto registrado correctamente")


def modificar_producto(tienda):
    #Opción 3: cambia el precio o el stock de un producto
    titulo("Modificar precio o stock")
    if len(tienda.get_productos()) == 0:
        print("No hay productos registrados")
        return

    tienda.consultar_productos()
    codigo = leer_texto("\nCódigo del producto a modificar: ").upper()
    producto = tienda.buscar_producto(codigo)
    if producto is None:
        print("No existe un producto con ese código")
        return

    print("  1. Cambiar precio")
    print("  2. Cambiar stock")
    opcion = leer_entero("Elige una opción: ")
    if opcion == 1:
        producto.set_precio(leer_entero("Nuevo precio: ")) 
    elif opcion == 2:
        producto.set_stock(leer_entero("Nuevo stock: "))
    else:
        print("Opción inválida.")
        return
    print("Producto actualizado:")
    producto.mostrar_info()


def realizar_venta(tienda):
    # Opción 4: crea una venta, agrega productos y la registra
    titulo("Realizar venta")
    if len(tienda.get_productos()) == 0:
        print("No hay productos registrados Registra productos primero")
        return

    cliente = leer_texto("Nombre del cliente: ")
    venta = Venta(cliente)

    # Se muestran los productos disponibles para que el usuario elija
    tienda.consultar_productos()
    print("\nAgrega productos a la venta (deja el código vacío para no agregar más)")

    while True:
        codigo = input("Código del producto: ").strip().upper()
        if codigo == "":
            break 
        producto = tienda.buscar_producto(codigo)
        if producto is None:
            print("No existe un producto con ese código")
        else:
            cantidad = leer_entero("Cantidad: ")
            if venta.agregar_producto(producto, cantidad):
                print(f"  Agregado: {cantidad} x {producto.get_nombre()}")

    # Si la venta tiene productos, se registra y se muestra la factura
    if tienda.registrar_venta(venta):
        print()
        venta.mostrar_factura()


# PROGRAMA PRINCIPAL
def main():
    tienda = Tienda("Moda Express")

    opcion = -1
    while opcion != 0:
        titulo("SISTEMA DE VENTAS - " + tienda.get_nombre())
        print("  1. Registrar producto")
        print("  2. Consultar productos")
        print("  3. Modificar precio o stock de un producto")
        print("  4. Realizar venta")
        print("  5. Consultar ventas realizadas")
        print("  6. Ver estadísticas y resumen general")
        print("  0. Salir")
        opcion = leer_entero("Elige una opción: ")

        if opcion == 1:
            registrar_producto(tienda)
        elif opcion == 2:
            print()
            tienda.consultar_productos()
        elif opcion == 3:
            modificar_producto(tienda)
        elif opcion == 4:
            realizar_venta(tienda)
        elif opcion == 5:
            print()
            tienda.consultar_ventas()
        elif opcion == 6:
            print()
            tienda.mostrar_resumen()
        elif opcion == 0:
            print("Hasta pronto")
        else:
            print("Opción inválida intenta de nuevo")
main()
