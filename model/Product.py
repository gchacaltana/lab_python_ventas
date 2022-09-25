class Product(object):

    def __init__(self, name: str, base_sale_price: float, percent_discount: float):
        """
        Constructor de la clase Product
        """
        self.name: str = name
        self.base_sale_price: float = base_sale_price
        self.percent_discount: float = percent_discount
        self.sale_price: float = self.base_sale_price
        self.discount: float = round(
            self.sale_price*self.percent_discount/100, 2)
        self.final_sale_price: float = self.sale_price - self.discount

    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.name

    def update_sale_price_by_percent_bsp(self, store_percent_bsp: float) -> None:
        """
        Actualiza el precio de venta del producto según el porcentaje de incremento definido 
        por cada tienda.
        """
        self.sale_price = self.base_sale_price + \
            (self.base_sale_price*store_percent_bsp/100)

        self.discount = self.sale_price * self.percent_discount/100

        self.final_sale_price = self.sale_price - self.discount
