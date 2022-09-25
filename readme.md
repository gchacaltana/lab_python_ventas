![API Store](https://i.im.ge/2022/09/26/1w8lCz.repo-rand-sales.jpg)

# Ventas aleatorias con Python

Este repositorio contiene la implementación del ejercicio propuesto "Aplicación de ventas aleatorias de una tienda de productos tecnológicos".

* El archivo application.py, contiene la implementación del ejercicio desarrollado con una programación estructurada.

* El archivo app.py, contiene la implementación del ejercicio desarrollado con una programación orientada a objetos.

## Paquete Mypy

* Creamos el entorno virtual para nuestro proyecto

```bash
py -m venv venv
```

* Activamos nuestro entorno virtual

```bash
source venv/Scripts/activate
```

* Instalamos el paquete mypy

```bash
pip install mypy
```

* Ejecutar mypy

```bash
mypy application.py --check-untyped-defs --ignore-missing-imports
```