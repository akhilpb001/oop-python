from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OKAY = 0.5
    BAD = 0.2


class Bike(object):
    def __init__(self, cost, make, model, year, condition):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition

        self.sale_price = self.update_sale_price()
        self.sold = False

    def update_sale_price(self):
        """
        Set the current sale price based on the make, model, age, and condition
        """
        original_value = lookup_msrp_value(self.make, self.model)
        current_year = datetime.now().year
        current_value = original_value * (1 - (current_year - self.year) * 0.015)
        current_value = current_value * self.condition.value
        self.sale_price = current_value
        return self.sale_price

    def sell(self):
        """
        Mark as sold and determine the profit received from selling the bike
        """
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, cost, new_condition):
        """
        Service the bike and update sale price
        """
        self.cost += cost
        self.condition = new_condition
        self.update_sale_price()
        return self.sale_price


def lookup_msrp_value(make, model):
    """
    Determine original sale price of a bike when new
    """
    return 1000
