from model.SaleTicketDetail import SaleTicketDetail
from model.Store import Store
from typing import List
from config import IGV_PERCENT, VALUE_POINT
import math


class SaleTicket(object):
    """
    Clase Ticket de Venta
    """

    def __init__(self, number: str, store: Store, list_detail: List[SaleTicketDetail]):
        """
        Constructor de la clase SaleTicket
        """
        self.number: str = number
        self.store:Store = store
        self.list_detail: List[SaleTicketDetail] = list_detail
        self.calculate_amounts()
        self.calculate_total_discount()
    
    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.number

    def calculate_amounts(self) -> None:
        """
        Actualiza los montos calculados que dependen del detalle del ticket
        """
        self.subtotal = sum([detail.total for key, detail in enumerate(self.list_detail)])
        self.igv: float = self.subtotal*IGV_PERCENT/100
        self.total: float = self.subtotal + self.igv
        self.points: int = math.ceil(self.subtotal/VALUE_POINT)

    def calculate_total_discount(self) -> None:
        """
        Calcula el valor del importe total de descuentos
        """
        self.total_discount = sum([detail.product.discount for key, detail in enumerate(self.list_detail)])