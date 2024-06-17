from classes.customer import Customer

class Customer_px(Customer):
    def rent_a_video(self, title, rating):
        if len(self.current_video_rentals) < 3:
            return super().rent_a_video(title, rating)
        return "Cannot rent more than three videos at a time."