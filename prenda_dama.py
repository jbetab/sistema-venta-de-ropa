from producto import Producto 
class PrendaDama(Producto):
    #Prenda de dama Hereda todo de Producto y solo cambia el género

    GENERO = "Dama"

    def __init__(self, codigo, nombre, categoria, precio, stock):
        super().__init__(codigo, nombre, categoria, precio, stock)
         # super() llama al constructor de Producto para que guarde l datos
