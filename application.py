from typing import List, Dict
import random

# link typing: https://docs.python.org/3/library/typing.html?highlight=typing#module-typing
# link random: https://docs.python.org/3/library/random.html

"""
Implementación del proyecto de clase python: Ventas de una tienda de productos de tecnología.
"""

def main():
    """
    Función principal del módulo application
    """

    # Lista de tiendas.
    stores: List[Dict[str, str]] = [
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

    products: List[Dict[str, str]] = [
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
        sales:int = random.randint(store["min_sales"],store["max_sales"])

        # iteramos sobre la cantidad de ventas
        for i in range(sales):
            # Número de Ticket Objetivo: "MIR00001"
            correlative: str = str(i+1).zfill(5)

            # número de ticket
            ticket_number: str = f"{store['code']}{correlative}"

            # random.sample => devuelve lista de números únicos aleatorios.
            # link: https://docs.python.org/3/library/random.html?highlight=random%20sample#random.sample
            # Los números aleatorios obtenidos serán los indices para obtener los productos.
            list_rand_products = random.sample(range(len(products)), random.randint(1,3))
            # Ejemplo: [2,5,7]

            # iteramos sobre la lista aleatoria de productos para crear el detalle del ticket
            for k,v in enumerate(list_rand_products):
                print(products[v]['name'])

        #print(f"{store['name']} Total de Tickets: {sales}")

if __name__ == "__main__":
    main()