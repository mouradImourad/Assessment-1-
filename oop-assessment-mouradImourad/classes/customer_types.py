# Write your independent Customer account type classes here
from classes.customer import Customer


class Customer_sx(Customer):
    # Standard account: Max 1 rental, all ratings allowed
   # No changes needed, default behavior from Customer class suffices
    pass  

class Customer_px(Customer):
    # Premium account: Max 3 rentals, all ratings allowed
    def max_rentals(self):
        return 3

class Customer_sf(Customer):
    # Standard Family account: Max 1 rental, no "R" rated movies
    def can_rent_rating(self, rating):
        return rating != 'R'

class Customer_pf(Customer):
    # Premium Family account: Max 3 rentals, no "R" rated movies
    def max_rentals(self):
        return 3

    def can_rent_rating(self, rating):
        return rating != 'R'