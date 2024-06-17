from classes.customer import Customer

class Customer_sx(Customer):
    def rent_a_video(self, title, rating):
        if len(self.current_video_rentals) < 1:
            return super().rent_a_video(title, rating)
        return "Cannot rent more than one video at a time"