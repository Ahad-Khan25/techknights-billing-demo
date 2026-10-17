def calc_total(amounts):
    return sum(amounts)


def calculate_total(amounts):
    return sum(amounts)

def apply_discounts(price, percent):
    return price * (1 - percent / 100)


def apply_disc(price, percent):
    """Backward compatible wrapper for apply_discounts.
    Maintains original API expected by tests.
    """
    return apply_discounts(price, percent)
