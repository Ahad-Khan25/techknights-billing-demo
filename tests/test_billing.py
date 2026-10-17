import billing


def test_calculate_total():
    assert billing.calc_total([10, 20]) == 30


def test_apply_discount():
    assert billing.apply_discount(100, 10) == 90