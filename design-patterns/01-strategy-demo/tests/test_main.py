from decimal import Decimal

from app.main import CheckoutService, RegularDiscount, VipDiscount


def test_regular_discount_keeps_price() -> None:
    checkout = CheckoutService(strategy=RegularDiscount())
    assert checkout.final_price(Decimal("100.00")) == Decimal("100.00")


def test_vip_discount_applies_twenty_percent_off() -> None:
    checkout = CheckoutService(strategy=VipDiscount())
    assert checkout.final_price(Decimal("100.00")) == Decimal("80.00")