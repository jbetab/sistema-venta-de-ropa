class Tienda:
    #uarda los productos y las ventas, y calcula las estadísticas

    def __init__(self, nombre):
        # Atributos de instancia privados
        self.__nombre = nombre
        self.__productos = []   # lista con todos los productos registrados
        self.__ventas = []      # lista con todas las ventas realizadas

    # metodso get 
    def get_nombre(self):
        return self.__nombre

    def get_productos(self):
        return self.__productos

    def get_ventas(self):
        return self.__ventas

    # productos
    def buscar_producto(self, codigo):
        #Busca un producto por su código devuelve el producto o None si no existe
        for producto in self.__productos:
            if producto.get_codigo() == codigo:
                return producto
        return None

    def registrar_producto(self, producto):
        #Agrega un producto a la tienda siempre que su código no esté repetido
        if self.buscar_producto(producto.get_codigo()) is not None:
            print(f"Ya existe un producto con el código {producto.get_codigo()}")
            return False
        self.__productos.append(producto)
        return True

    def consultar_productos(self):
        #Muestra la información de todos los productos registrados
        print(f"Productos de {self.__nombre}")
        if len(self.__productos) == 0:
            print("No hay productos registrados")
        for producto in self.__productos:
            producto.mostrar_info()

    # ventas
    def registrar_venta(self, venta):
        #Guarda la venta en la tienda No guarda ventas vacías
        if venta.calcular_total_unidades() == 0:
            print("La venta no tiene productos no se registra")
            return False
        venta.asignar_numero()      # número consecutivo de la venta
        self.__ventas.append(venta)
        return True

    def consultar_ventas(self):
        #Muestra la factura de todas las ventas realizadas
        print("Ventas realizadas")
        if len(self.__ventas) == 0:
            print("No hay ventas registradas")
        for venta in self.__ventas:
            venta.mostrar_factura()

    # estadistica de las ventas

    def calcular_promedio_ventas(self):
        #Promedio del valor total de las ventas = suma de totales / cantidad de ventas
        if len(self.__ventas) == 0:
            return 0    # evita dividir entre cero si aún no hay ventas
        suma = 0
        for venta in self.__ventas:
            suma += venta.calcular_total()
        return suma / len(self.__ventas)

    def categoria_mas_vendida(self):
        #Devuelve [categoria, unidades] de la categoría con más unidadesvendidas, o None si todavía no hay ventas
        categorias = []
        unidades = []
        for producto in self.__productos:
            categoria = producto.get_categoria()
            if categoria in categorias:
                # La categoría ya está en la lista: se suman las unidades
                posicion = categorias.index(categoria)
                unidades[posicion] += producto.get_unidades_vendidas()
            else:
                # Categoría nueva: se agrega a las dos listas
                categorias.append(categoria)
                unidades.append(producto.get_unidades_vendidas())

        if len(categorias) == 0:
            return None

        # Se busca la posición con mayor cantidad de unidades vendidas
        mayor = 0
        for i in range(len(categorias)):
            if unidades[i] > unidades[mayor]:
                mayor = i
        if unidades[mayor] == 0:
            return None     # nada se ha vendido todavía
        return [categorias[mayor], unidades[mayor]]

    def producto_mas_vendido(self):
        #Devuelve el producto con más unidades vendidas o None si no hay ventas
        mas_vendido = None
        for producto in self.__productos:
            if mas_vendido is None or producto.get_unidades_vendidas() > mas_vendido.get_unidades_vendidas():
                mas_vendido = producto
        if mas_vendido is None or mas_vendido.get_unidades_vendidas() == 0:
            return None
        return mas_vendido

    def calcular_unidades_por_genero(self, genero):
        #Suma las unidades vendidas de los productos de un género
        total = 0
        for producto in self.__productos:
            if producto.get_genero() == genero:
                total += producto.get_unidades_vendidas()
        return total

    def genero_mas_vendido(self):
        #Compara las ventas de dama y caballero y devuelve un texto con el resultado
        dama = self.calcular_unidades_por_genero("Dama")
        caballero = self.calcular_unidades_por_genero("Caballero")
        if dama == 0 and caballero == 0:
            return "Aún no hay ventas"
        if dama > caballero:
            return f"Dama ({dama} unidades vs {caballero} de Caballero)"
        if caballero > dama:
            return f"Caballero ({caballero} unidades vs {dama} de Dama)"
        return f"Empate ({dama} unidades cada uno)"

    # estadisticas de los productos

    def producto_precio_maximo(self):
        #Devuelve el producto más caro None si no hay productos
        mayor = None
        for producto in self.__productos:
            if mayor is None or producto.get_precio() > mayor.get_precio():
                mayor = producto
        return mayor

    def producto_precio_minimo(self):
        #Devuelve el producto más barato None si no hay productos
        menor = None
        for producto in self.__productos:
            if menor is None or producto.get_precio() < menor.get_precio():
                menor = producto
        return menor

    def producto_stock_maximo(self):
        #Devuelve el producto con más unidades en inventario
        mayor = None
        for producto in self.__productos:
            if mayor is None or producto.get_stock() > mayor.get_stock():
                mayor = producto
        return mayor

    def producto_stock_minimo(self):
        #Devuelve el producto con menos unidades en inventario
        menor = None
        for producto in self.__productos:
            if menor is None or producto.get_stock() < menor.get_stock():
                menor = producto
        return menor

    # resumen
    def mostrar_resumen(self):
        #Imprime todas las estadísticas de la tienda
        print(f"Resumen general de {self.__nombre}")
        print(f"Productos registrados: {len(self.__productos)}")
        print(f"Ventas realizadas: {len(self.__ventas)}")
        print(f"Promedio de ventas: ${self.calcular_promedio_ventas():,.2f}")

        # Categoría más vendid None si no hay ventas
        categoria = self.categoria_mas_vendida()
        if categoria is None:
            print("Categoría más vendida: aún no hay ventas")
        else:
            print(f"Categoría más vendida: {categoria[0]} ({categoria[1]} unidades)")

        # Producto más vendido None si no hay ventas
        producto = self.producto_mas_vendido()
        if producto is None:
            print("Producto más vendido: aún no hay ventas")
        else:
            print(f"Producto más vendido: {producto.get_nombre()} "
                  f"({producto.get_unidades_vendidas()} unidades)")

        print(f"Género más vendido: {self.genero_mas_vendido()}")

        # Precios y stock máximo y mínimo solo si hay productos registrados
        if len(self.__productos) > 0:
            p_max = self.producto_precio_maximo()
            p_min = self.producto_precio_minimo()
            s_max = self.producto_stock_maximo()
            s_min = self.producto_stock_minimo()
            print(f"Precio máximo: ${p_max.get_precio():,.2f} ({p_max.get_nombre()})")
            print(f"Precio mínimo: ${p_min.get_precio():,.2f} ({p_min.get_nombre()})")
            print(f"Stock máximo: {s_max.get_stock()} ({s_max.get_nombre()})")
            print(f"Stock mínimo: {s_min.get_stock()} ({s_min.get_nombre()})")
