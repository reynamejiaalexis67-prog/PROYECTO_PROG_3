from entidades.categoria import Categoria
from entidades.exceptions import precio_no_valido

class Producto:
    
    def __init__(self,nombre:str,precio:float,categoria:Categoria):
        if precio <= 0:
            raise precio_no_valido("el precio no puede ser negativo")

        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
    
    def mostrar_info(self)-> str:
        return f"{self.nombre}- ${self.precio}"
    
