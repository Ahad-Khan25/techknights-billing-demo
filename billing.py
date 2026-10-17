def calc_total(amounts):
    """Return the sum of all item amounts."""
    return sum(amounts)


def apply_discount(total, percent):
    """Return the total after a percentage discount."""
    return total - (total * percent / 100)