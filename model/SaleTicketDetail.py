from math import prod
from model.Product import Product


class SaleTicketDetail(object):

    def __init__(self, product: Product, quantity: int):
        """
        Constructor de la Clase SaleTicketDetail
        """
        self.product: Product = product
        self.quantity: int = quantity
        self.total: float = round(self.product.final_sale_price*self.quantity, 2)
