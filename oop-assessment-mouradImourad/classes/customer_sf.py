from classes.customer import Customer

class Customer_sf(Customer):
    def rent_a_video(self, title, rating):
        if len(self.current_video_rentals) < 1 and rating != 'R':
            return super().rent_a_video(title, rating)
        return "Cannot rent more than one video at a time or restricted rating for family accounts."
    