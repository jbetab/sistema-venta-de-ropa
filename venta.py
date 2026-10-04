from producto import Producto  

class Venta:
    #Representa una venta un cliente y los productos que compra

    # iguales para todas las ventas
    DESCUENTO = 0.20                # descuento del 20 %
    UNIDADES_PARA_DESCUENTO = 3     # el descuento aplica con MÁS de 3 unidades
    total_ventas_creadas = 0        # contador de ventas

    def __init__(self, cliente):
        # atributos de instancia privados
        self.__numero = 0       # el número real se asigna cuando la venta se registra
        self.__cliente = cliente
        self.__productos = []
        self.__cantidades = []

    # metodos get
    def get_numero(self):
        return self.__numero

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_cantidades(self):
        return self.__cantidades

    # comportamientos
    def asignar_numero(self):
        #Le da a la venta su número consecutivo
        Venta.total_ventas_creadas += 1
        self.__numero = Venta.total_ventas_creadas

    def agregar_producto(self, producto, cantidad):
        #Agrega el producto a la venta y descuenta el stock
        # producto.vender revisa el stock y lo descuenta
        if producto.vender(cantidad):
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)
            return True
        print(f"  No se pudo agregar {cantidad} x {producto.get_nombre()} "
              f"(stock disponible: {producto.get_stock()})")
        return False

    def calcular_total_unidades(self):
        #Suma cuántas unidades se compraron en total en esta venta
        total = 0
        for cantidad in self.__cantidades:
            total += cantidad
        return total

    def calcular_subtotal(self):
        #Suma precio por cantidad de cada producto
        subtotal = 0
        for i in range(len(self.__productos)):
            subtotal += self.__productos[i].get_precio() * self.__cantidades[i]
        return subtotal

    def calcular_iva(self):
        #Calcula el 19 % de IVA sobre el subtotal
        return self.calcular_subtotal() * Producto.IVA

    def calcular_descuento(self):
        #Si se compraron MÁS de 3 unidades, aplica 20 % sobre el total
        #subtotal + IVA Si no el descuento es 0
        if self.calcular_total_unidades() > Venta.UNIDADES_PARA_DESCUENTO:
            return (self.calcular_subtotal() + self.calcular_iva()) * Venta.DESCUENTO
        return 0

    def calcular_total(self):
        #Total a pagar = subtotal + IVA - descuento
        return self.calcular_subtotal() + self.calcular_iva() - self.calcular_descuento()

    def mostrar_factura(self):
        #Imprime el detalle de la venta
        print(f" Venta #{self.__numero} | Cliente: {self.__cliente}")
        # Se recorre cada producto comprado junto con su cantidad
        for i in range(len(self.__productos)):
            producto = self.__productos[i]
            cantidad = self.__cantidades[i]
            valor = producto.get_precio() * cantidad
            print(f"  {cantidad} x {producto.get_nombre()} (${producto.get_precio():,.2f} = ${valor:,.2f}")
        print(f"  Subtotal:  ${self.calcular_subtotal():,.2f}")
        print(f"  IVA 19%:   ${self.calcular_iva():,.2f}")
        print(f"  Descuento: ${self.calcular_descuento():,.2f}")
        print(f"  TOTAL:     ${self.calcular_total():,.2f}")
