from entidades.categoria import Categoria
    
class Carrito:
    #constructor de clase 
    def __init__(self):
            #lista donde se guardaran los productos 
        self.productos = []
        
        
    def agregar_producto(self, producto):
        self.productos.append(producto)


    # metodo para calcular el subtotal
    def calcular_subtotal(self):
        subtotal = 0

        # recorremos todos los productos
        for producto in self.productos:
            subtotal += producto.precio
        return subtotal


    # metodo para calcular el iva
    def calcular_iva(self):
        iva = self.calcular_subtotal() * 0.16
        return iva


    # metodo para calcular descuento
    # si el producto es de reposteria
    def calcular_descuento(self):
        descuento = 0
        for producto in self.productos:
            # verificamos si el producto es reposteria
            if producto.categoria == Categoria.REPOSTERIA:
                descuento += producto.precio * 0.10
        return descuento


    # metodo para calcular el total final
 # metodo para calcular total
    def calcular_total(self):

        # si no hay productos
        if len(self.productos) == 0:

            return 0

        total = self.calcular_subtotal() + self.calcular_iva() - self.calcular_descuento()

        return total