"""Classes for melon orders."""

class AbstractMelonOrder:
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5 
        if self.species == "christmas melon": 
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" and self.qty < 10: 
            total += 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
       
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    
        


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    # def get_total(self):
    #     total = super().get_total()
    #     if self.qty < 10:
    #         total = total+3
    #     return total

class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = "government"
    tax = 0
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self):
        self.passed_inspection = True
        return self.passed_inspection
        

order0 = InternationalMelonOrder("watermelon", 6, "AUS")
print(order0.get_total())


order1 = GovernmentMelonOrder("watermelon", 6)
print(order1.passed_inspection)
print(order1.mark_inspection())