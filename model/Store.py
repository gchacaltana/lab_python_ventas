import random


class Store(object):

    def __init__(self, code: str, name: str, min_sales: int, max_sales: int, percent_bsp: float):
        """
        Constructor de la clase Store
        """
        self.code: str = code
        self.name: str = name
        self.min_sales: int = min_sales
        self.max_sales: int = max_sales
        self.percent_bsp: float = percent_bsp
    
    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.name

    def get_rand_sales(self) -> int:
        """
        Devuelve un número de ventas de manera aleatoria basada en el rango
        de ventas mínimas y máximas de la tienda.
        """
        return random.randint(self.min_sales, self.max_sales)
