from classes.customer import Customer

class Customer_pf(Customer):
    def rent_a_video(self, title, rating):
        if len(self.current_video_rentals) < 3 and rating != 'R':
            return super().rent_a_video(title, rating)
        return "Cannot rent more than three videos at a gtime or restricted rating for family accounts."
    