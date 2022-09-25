
def get_currency_format(currency_symbol,amount) -> str:
    """
    Método para formatear una variable numérica en string con formato de moneda
    """
    return "{}{:,.2f}".format(currency_symbol, amount)
