# Write your independent Customer account type classes here
from classes.customer import Customer


class Customer_sx(Customer):
    def __init__(self, id, first_name, last_name, account_type, current_video_rentals, rent_a_video):
        super().__init__(id, first_name, last_name, account_type)
        def __init__(self, rent_a_video):
            self.rent_a_video = rent_a_video
    # Standard account: Max 1 rental, all ratings allowed
   # No changes needed, default behavior from Customer class suffice


class Customer_px(Customer):
    # Premium account: Max 3 rentals, all ratings allowed
    def __init__(self, id, first_name, last_name, account_type, current_video_rentals, rent_a_video):
        super().__init__(id, first_name, last_name, account_type)
        def __init__(self, rent_a_video):
            self.rent_a_video = rent_a_video

    def max_rentals(self):
        return 3

class Customer_sf(Customer):
    # Standard Family account: Max 1 rental, no "R" rated movies
    def __init__(self, id, first_name, last_name, account_type, current_video_rentals, rent_a_video):
        super().__init__(id, first_name, last_name, account_type)
        def __init__(self, rent_a_video):
            self.rent_a_video = rent_a_video

    def can_rent_rating(self, rating):
            return rating != 'R'

class Customer_pf(Customer):
    # Premium Family account: Max 3 rentals, no "R" rated movies
    def __init__(self, id, first_name, last_name, account_type, current_video_rentals, rent_a_video):
        super().__init__(id, first_name, last_name, account_type)
        def __init__(self, rent_a_video):
            self.rent_a_video = rent_a_video

    def max_rentals(self):
        return 3

    def can_rent_rating(self, rating):
        
        return rating != 'R'