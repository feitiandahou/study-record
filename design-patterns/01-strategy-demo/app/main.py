from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol


class DiscountStrategy(Protocol):
    def apply(self, original_price: Decimal) -> Decimal:
        ...


class RegularDiscount:
    def apply(self, original_price: Decimal) -> Decimal:
        return original_price


class VipDiscount:
    def apply(self, original_price: Decimal) -> Decimal:
        return original_price * Decimal("0.80")


@dataclass(slots=True)
class CheckoutService:
    strategy: DiscountStrategy

    def final_price(self, original_price: Decimal) -> Decimal:
        return self.strategy.apply(original_price).quantize(Decimal("0.01"))


def describe_checkout(label: str, service: CheckoutService, amount: Decimal) -> str:
    return f"{label}: original={amount:.2f}, final={service.final_price(amount):.2f}"


def main() -> None:
    amount = Decimal("100.00")
    regular_checkout = CheckoutService(strategy=RegularDiscount())
    vip_checkout = CheckoutService(strategy=VipDiscount())

    print(describe_checkout("regular", regular_checkout, amount))
    print(describe_checkout("vip", vip_checkout, amount))


if __name__ == "__main__":
    main()