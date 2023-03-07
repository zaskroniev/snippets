def calculate_brutto(netto:float, vat:float) -> float:
    """
    Function that calculates brutto for netto and vat
    :param netto: value of netto
    :param vat: value of vat like 0.23 for 23%
    :return: value of brutto
    """
    brutto = netto * (1+vat)
    return brutto
