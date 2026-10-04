class Producto:
    #Clase base contiene lo que comparten todos los productos de la tienda

    # Pertenecen a la clase no a un objeto en particular son iguales para todos los productos
    IVA = 0.19                      
    GENERO = "General"              
    total_productos_creados = 0     

    def __init__(self, codigo, nombre, categoria, precio, stock):
        #ATRIBUTOS DE INSTANCIA
        # Son propios de cada objeto utilizando el encapsulamiento
        self.__codigo = codigo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = 0               
        self.__stock = 0                
        self.__unidades_vendidas = 0    

        # Se usan los métodos set para que el precio y el stock se validen
        self.set_precio(precio)
        self.set_stock(stock)

        # Cada vez que se crea un producto, se suma 1 al contador de la clase
        Producto.total_productos_creados += 1

    # metodos get para cosnultar los atributos privados

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def get_unidades_vendidas(self):
        return self.__unidades_vendidas

    def get_genero(self):
        # self.GENERO toma el valor de dama o caballero
        return self.GENERO

    # metodos set para validar 
    
    def set_nombre(self, nombre):
        if nombre != "":
            self.__nombre = nombre

    def set_categoria(self, categoria):
        if categoria != "":
            self.__categoria = categoria

    def set_precio(self, precio):
        # El precio debe ser mayor que 0
        if precio > 0:
            self.__precio = precio
        else:
            print("Precio inválido debe ser mayor que 0")

    def set_stock(self, stock):
        # El stock no puede ser negativo
        if stock >= 0:
            self.__stock = stock
        else:
            print("Stock inválido no puede ser negativo")

    # comportamientos
    def calcular_precio_con_iva(self):
        #Devuelve el precio del producto sumándole el IVA
        return self.__precio * (1 + Producto.IVA)

    def vender(self, cantidad):
        #Descuenta del stock la cantidad vendida Devuelve True si se pudo vender y False si no hay suficiente stock
        if cantidad <= 0 or cantidad > self.__stock:
            return False
        self.__stock -= cantidad                # baja el inventario
        self.__unidades_vendidas += cantidad    # sube el acumulado de ventas
        return True

    def mostrar_info(self):
        #Imprime en pantalla la información del producto
        print(f"[{self.__codigo}] {self.__nombre} | Categoría: {self.__categoria} | "
              f"Género: {self.get_genero()} | Precio: ${self.__precio:,.2f} | "
              f"Stock: {self.__stock} | Vendidas: {self.__unidades_vendidas}")
