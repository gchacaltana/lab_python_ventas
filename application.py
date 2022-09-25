from typing import List, Dict
from config import QUANTITY_MIN, QUANTITY_MAX, PRODUCT_MAX, PRODUCT_MIN, IGV_PERCENT, VALUE_POINT, CURRENCY_SYMBOL
import random
import math

# link typing: https://docs.python.org/3/library/typing.html?highlight=typing#module-typing
# link random: https://docs.python.org/3/library/random.html

"""
Implementación del proyecto de clase python: 
Ventas de una tienda de productos de tecnología.
"""


def main():
    """
    Función principal del módulo application
    """

    # Lista de tiendas.
    stores: List[Dict[str, str | int | float]] = [
        {
            "code": "MIR",
            "name": "Miraflores",
            "min_sales": 85,
            "max_sales": 110,
            "percent_bsp": 18.75
        },
        {
            "code": "SUR",
            "name": "Surquillo",
            "min_sales": 75,
            "max_sales": 100,
            "percent_bsp": 17.95
        },
        {
            "code": "LIM",
            "name": "Centro de Lima",
            "min_sales": 90,
            "max_sales": 135,
            "percent_bsp": 18.15
        },
        {
            "code": "SJM",
            "name": "San Juan de Miraflores",
            "min_sales": 95,
            "max_sales": 140,
            "percent_bsp": 17.88
        },
        {
            "code": "CHO",
            "name": "Chorrillos",
            "min_sales": 70,
            "max_sales": 95,
            "percent_bsp": 17.80
        }
    ]

    products: List[Dict[str, str | float | int]] = [
        {
            "name": "Memoria USB Kingston 64 GB",
            "base_sale_price": 38.90,
            "percent_discount": 10
        },
        {
            "name": "Mouse inalámbrico Teraware Negro",
            "base_sale_price": 59.90,
            "percent_discount": 5
        },
        {
            "name": "Teclado inalámbrico Logitech K120",
            "base_sale_price": 39.90,
            "percent_discount": 0
        },
        {
            "name": "Batería externa G 5000 mAh",
            "base_sale_price": 49.90,
            "percent_discount": 0
        },
        {
            "name": "Micrófono Maono AU-903",
            "base_sale_price": 189.90,
            "percent_discount": 5
        },
        {
            "name": "Audífonos bluetooth True Wireless Xiaomi",
            "base_sale_price": 129.50,
            "percent_discount": 10
        },
        {
            "name": "Mouse pad gamer Teraware M",
            "base_sale_price": 55.90,
            "percent_discount": 0
        },
        {
            "name": "Cámara web Jetion PJT-DCM141",
            "base_sale_price": 89.90,
            "percent_discount": 20
        },
        {
            "name": "Hub Teraware conector usb 4",
            "base_sale_price": 49.90,
            "percent_discount": 0
        },
        {
            "name": "Cooler para laptop Teraware 5 niveles",
            "base_sale_price": 59.90,
            "percent_discount": 5
        }
    ]

    # iteramos sobre la cantidad de tiendas
    for key, store in enumerate(stores):

        # Obtenemos el total de ventas obtenidas de manera aleatoria
        # según los datos de cada tienda.
        sales: int = random.randint(
            int(store["min_sales"]), int(store["max_sales"]))

        # declarar e inicializar la lista que almacenará los tickets de venta.
        list_tickets: List[Dict[str, str|float]] = []

        # declarar e inicializar la lista que almacenará los detalles tickets de venta.
        list_detail: List[Dict[str, str|float]] = []

        # iteramos sobre la cantidad de ventas para crear los tickets de venta
        for i in range(sales):
            # Crear los tickets de venta (aleatorio)

            # Número de Ticket Objetivo: "MIR00001"
            correlative: str = str(i+1).zfill(5)

            # número de ticket
            ticket_number: str = f"{store['code']}{correlative}"

            # random.sample => devuelve lista de números únicos aleatorios.
            # link: https://docs.python.org/3/library/random.html?highlight=random%20sample#random.sample
            # Los números aleatorios obtenidos serán los indices para obtener los productos.
            list_rand_products = random.sample(
                range(len(products)), random.randint(PRODUCT_MIN, PRODUCT_MAX))
            # Ejemplo: [2,5,7]

            # variable para almacenar el importe del subtotal del ticket de venta
            ticket_subtotal: float = 0

            # variable para almacenar el importe del total de descuentos.
            ticket_discount: float = 0

            # iteramos sobre la lista aleatoria de productos para crear el detalle del ticket
            for k, v in enumerate(list_rand_products):

                # calculando el precio de venta del producto según el porcentaje BSP de la tienda
                price_sale: float = round(float(products[v]['base_sale_price']) + (
                    float(products[v]['base_sale_price']) * float(store['percent_bsp'])/100), 2)

                # calculando el importe del descuento del producto.
                discount: float = round(
                    price_sale * (float(products[v]['percent_discount'])/100), 2)

                ticket_discount += discount

                # calculando el precio final de venta del producto
                final_sale_price: float = round(
                    price_sale - abs(discount), 2)

                quantity: int = random.randint(QUANTITY_MIN, QUANTITY_MAX)

                total: float = round(final_sale_price*quantity, 2)

                ticket_subtotal += total

                detail: Dict[str, str | float] = {
                    "ticket_number": ticket_number,
                    "product_name": products[v]['name'],
                    "base_sale_price": float(products[v]['base_sale_price']),
                    "sale_price": price_sale,
                    "discount": discount,
                    "final_sale_price": final_sale_price,
                    "quantity": quantity,
                    "total": total
                }

                list_detail.append(detail)

            ticket_igv: float = ticket_subtotal*IGV_PERCENT/100
            ticket_total:float = ticket_subtotal + ticket_igv
            ticket_points:int = math.floor(ticket_subtotal/VALUE_POINT)

            # Creamos el diccionario para el ticket de venta
            ticket:Dict[str, str|float] = {
                "number": ticket_number,
                "subtotal": ticket_subtotal,
                "igv": ticket_igv,
                "total": ticket_total,
                "points": ticket_points,
                "discount": ticket_discount
            }

            list_tickets.append(ticket)

        # Mostrando reporte

        # Calculando el importe total de descuentos de todos los tickets de venta

        # Alternativa 1
        """
        total_discount:float = 0
        for k, ticket in enumerate(list_tickets):
            total_discount += ticket['discount']

        rep_total_discount = round(total_discount,2)
        """

        #Alternativa 2
        rep_total_discount:float = round(sum([float(v["discount"]) for k, v in enumerate(list_tickets)]), 2)

        # Calculando la suma total de IGV cobrado
        rep_total_igv:float = round(sum([float(v["igv"]) for k, v in enumerate(list_tickets)]), 2)

        # Calculando la suma total de ingresos
        rep_total_sale:float = round(sum([float(v["total"]) for k, v in enumerate(list_tickets)]), 2)

        # Aplicando formato de moneda a la variable rep_total_sale
        display_total_sale:str = "{}{:,.2f}".format(CURRENCY_SYMBOL, rep_total_sale)

        # Calcuando el total de puntos entregados
        rep_total_points:int = sum([int(v["points"]) for k, v in enumerate(list_tickets)])

        # Calculando el valor del ticket promedio de venta.
        ticket_avg:float = round(rep_total_sale / sales, 2)

        # Ordenemos lista de tickets (de menor a mayor)
        sorted_tickets:List[Dict[str, str | float]] = sorted(list_tickets, key=lambda x: x['total'])

        # Obtenemos la cantidad de tickets cuyo importe supera el ticket promedio
        rep_tickets_higher_than:int = len(
            [k for k, v in enumerate(sorted_tickets) if float(v['total']) > ticket_avg])

        # Obtenemos la cantidad tickets que tienen descuento.
        tickets_with_discount:int = len(
            [k for k, v in enumerate(sorted_tickets) if float(v['discount']) > 0])

        # Calculamos el porcentaje de tickets que tienen descuento
        percent_tickets_with_discount = math.floor(
            (tickets_with_discount*100) / sales)

        print("\n") # salto de linea
        print(f"Tienda: {store['name']}")
        print("*"*30) # mostrar una linea de asteriscos
        print(f"Total de Ventas: {len(list_tickets)}")
        print(f"Importe Total de Ventas: {display_total_sale}")
        print(f"Ticket Promedio de Ventas: {ticket_avg}")
        print(f"Ticket de Venta más baja: {sorted_tickets[0]['total']}")
        print(sorted_tickets[0])
        print(f"Ticket de Venta más alta: {round(float(sorted_tickets[-1]['total']),2)}")
        print(
            f"Total de Tickets mayor al promedio de venta: {rep_tickets_higher_than}")
        print(f"Total de descuento: {rep_total_discount}")
        print(
            f"Tickets con descuento: {tickets_with_discount} ({percent_tickets_with_discount}%)")
        print(f"Total IGV: {rep_total_igv}")
        print(f"Total de Puntos entregados: {rep_total_points}")


if __name__ == "__main__":
    main()
