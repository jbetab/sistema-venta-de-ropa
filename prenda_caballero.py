from producto import Producto 

class PrendaCaballero(Producto):
    #Prenda de caballero Hereda todo de Producto y solo cambia el género

    GENERO = "Caballero"

    def __init__(self, codigo, nombre, categoria, precio, stock):
        super().__init__(codigo, nombre, categoria, precio, stock)
        # super() llama al constructor de Producto para que guarde l datos
