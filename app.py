from typing import List, Dict
from model.Store import Store
from model.Product import Product
from model.SaleTicketDetail import SaleTicketDetail
from model.SaleTicket import SaleTicket
from config import CURRENCY_SYMBOL
import utils
import random
import math


def create_list_stores() -> List[Store]:
    """
    Función que crea y devuelve una lista de objetos Store
    """
    data_stores: List[Dict[str, str | int | float]] = [
        {
            "code": "MIR",
            "name": "Miraflores",
            "min_sales": 85,
            "max_sales": 100,
            "percent_bsp": 8.75
        },
        {
            "code": "SUR",
            "name": "Surquillo",
            "min_sales": 75,
            "max_sales": 100,
            "percent_bsp": 7.95
        },
        {
            "code": "LIM",
            "name": "Centro de Lima",
            "min_sales": 90,
            "max_sales": 135,
            "percent_bsp": 8.15
        },
        {"code": "SJM", "name": "San Juan de Miraflores",
         "min_sales": 95, "max_sales": 140, "percent_bsp": 7.88},
        {"code": "CHO", "name": "Chorrillos", "min_sales": 70,
         "max_sales": 95, "percent_bsp": 7.80}
    ]

    # Lista de objetos tienda
    stores: List[Store] = []

    # Iteramos la lista de tiendas.
    for key, store in enumerate(data_stores):
        # Creamos el objeto tienda
        obj_store = Store(str(store['code']), str(store['name']), int(
            store['min_sales']), int(store['max_sales']), float(store['percent_bsp']))
        stores.append(obj_store)

    return stores


def create_list_products() -> List[Product]:
    """
    Función que crea y devuelve una lista de objetos Product
    """

    data_products: List[Dict[str, str | float | int]] = [
        {
            "name": "Memoria USB Kingston 64 GB",
            "base_sale_price": 38.90,
            "percent_discount": 10
        },
        {"name": "Mouse inalámbrico Teraware Negro",
         "base_sale_price": 59.90, "percent_discount": 5},
        {"name": "Teclado inalámbrico Logitech K120",
         "base_sale_price": 39.90, "percent_discount": 0},
        {"name": "Batería externa G 5000 mAh",
         "base_sale_price": 49.90, "percent_discount": 0},
        {"name": "Micrófono Maono AU-903",
         "base_sale_price": 189.90, "percent_discount": 5},
        {"name": "Audífonos bluetooth True Wireless Xiaomi",
         "base_sale_price": 129.50, "percent_discount": 10},
        {"name": "Mouse pad gamer Teraware M",
         "base_sale_price": 55.90, "percent_discount": 0},
        {"name": "Cámara web Jetion PJT-DCM141",
         "base_sale_price": 89.90, "percent_discount": 20},
        {"name": "Hub Teraware conector usb 4",
         "base_sale_price": 49.90, "percent_discount": 0},
        {"name": "Cooler para laptop Teraware 5 niveles",
         "base_sale_price": 59.90, "percent_discount": 5}
    ]

    # Creamos la lista de objetos Product
    products: List[Product] = []

    for key, product in enumerate(data_products):

        # Creamos el objeto Product
        obj_product = Product(str(product['name']), float(
            product['base_sale_price']), float(product['percent_discount']))
        products.append(obj_product)

    return products


def create_sales_tickets(store: Store, products: List[Product]) -> List[SaleTicket]:
    """
    Función que crea un ticket de venta.
    Retorna una lista de objetos SaleTicket.
    """

    list_tickets: List[SaleTicket] = []

    # Obtenemos la cantidad de ventas para la tienda de manera aleatoria
    sales: int = store.get_rand_sales()

    for i in range(sales):
        # Creamos del detalle del ticket de venta
        list_detail: List[SaleTicketDetail] = create_detail_sale_ticket(
            store, products)

        correlative: str = str(i+1).zfill(5)
        ticket_number: str = f"{store.code}{correlative}"

        # Creamos el objeto SaleTicket
        sale_ticket: SaleTicket = SaleTicket(ticket_number, store, list_detail)

        # Agregamos el objeto Saleticket en una lista
        list_tickets.append(sale_ticket)

    return list_tickets


def create_detail_sale_ticket(store: Store, products: List[Product]) -> List[SaleTicketDetail]:
    """
    Función que crea el detalle de un ticket de venta.
    Retorna una lista de objetos SaleTicketDetail.
    """

    # random.sample => devuelve lista de números únicos aleatorios.
    # link: https://docs.python.org/3/library/random.html?highlight=random%20sample#random.sample
    # Los números aleatorios obtenidos serán los indices para obtener los productos.
    list_rand_products = random.sample(
        range(len(products)), random.randint(1, 3))

    list_detail: List[SaleTicketDetail] = []

    # iteramos sobre la lista obtenida
    for k, v in enumerate(list_rand_products):
        quantity: int = random.randint(1, 3)

        # Obtenemos el objeto producto según el indice
        product: Product = products[v]

        # Actualizamos el precio de venta del producto
        product.update_sale_price_by_percent_bsp(store.percent_bsp)

        # Creamos el objeto detail
        detail: SaleTicketDetail = SaleTicketDetail(product, quantity)

        # Agregamos el objeto detail en la lista
        list_detail.append(detail)

    return list_detail


def main():
    """
    Función principal del módulo app.py
    """

    # Crear la lista de objetos Store
    stores: List[Store] = create_list_stores()

    # Crear la lista de objetos Product
    products: List[Product] = create_list_products()

    print("\n")
    print("*"*30)
    print("REPORTE DE VENTAS DEL DIA")
    print("*"*30)
    print("\n")

    for key, store in enumerate(stores):
        # creamos la lista de objetos SaleTicket (tickets de venta) para la tienda
        list_sales_tickets: List[SaleTicket] = create_sales_tickets(
            store, products)

        # Total de tickets de ventas
        total_sales = len(list_sales_tickets)

        # Calcular la suma total de ventas
        rep_total_sale = round(
            sum([ticket.total for k, ticket in enumerate(list_sales_tickets)]), 2)

        # Calcular la suma total de descuentos
        rep_total_discount: float = round(
            sum([ticket.total_discount for k, ticket in enumerate(list_sales_tickets)]), 2)

        # Calculando la suma total de IGV cobrado
        rep_total_igv: float = round(
            sum([ticket.igv for k, ticket in enumerate(list_sales_tickets)]), 2)

        # Calcuando el total de puntos entregados
        rep_total_points: int = sum(
            [ticket.points for k, ticket in enumerate(list_sales_tickets)])

        # Calculando el valor del ticket promedio de venta.
        ticket_avg: float = round(rep_total_sale / total_sales, 2)

        # Ordenemos lista de tickets (de menor a mayor)
        sorted_tickets: List[SaleTicket] = sorted(
            list_sales_tickets, key=lambda x: x.total)

        # Obtenemos la cantidad de tickets cuyo importe supera el ticket promedio
        rep_tickets_higher_than: int = len(
            [k for k, ticket in enumerate(sorted_tickets) if ticket.total > ticket_avg])

        # Obtenemos la cantidad tickets que tienen descuento.
        tickets_with_discount: int = len(
            [k for k, ticket in enumerate(sorted_tickets) if ticket.total_discount > 0])

        # Calculamos el porcentaje de tickets que tienen descuento
        percent_tickets_with_discount = math.floor(
            (tickets_with_discount*100) / total_sales)

        # Mostramos en pantalla valores calculados.
        print(f"Tienda: {store.name}")
        print(f"Cod. Tienda: {store.code}")
        print(f"Ventas: {total_sales}")
        print(
            f"Total de Ventas: {utils.get_currency_format(CURRENCY_SYMBOL,rep_total_sale)}")
        print(
            f"Total de Descuento: {utils.get_currency_format(CURRENCY_SYMBOL,rep_total_discount)}")
        print(
            f"Tickets con descuento: {tickets_with_discount} ({percent_tickets_with_discount}%)")
        print(
            f"Total de IGV: {utils.get_currency_format(CURRENCY_SYMBOL, rep_total_igv)}")
        print(f"Total de Puntos: {rep_total_points}")
        print(
            f"Ticket Promedio: {utils.get_currency_format(CURRENCY_SYMBOL, ticket_avg)}")
        print(
            f"Ticket de Venta más baja: {utils.get_currency_format(CURRENCY_SYMBOL, sorted_tickets[0].total)}")
        print(
            f"Ticket de Venta más alta: {utils.get_currency_format(CURRENCY_SYMBOL, sorted_tickets[-1].total)}")
        print(
            f"Total de Tickets mayor al promedio de venta: {rep_tickets_higher_than}")

        print("\n")
        print("-"*30)
        print("\n")


if __name__ == "__main__":
    main()
