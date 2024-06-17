from classes.customer import Customer

class Customer_pf(Customer):
    def rent_a_video(self, title, rating=None):
        if len(self.current_video_rentals) < 3 and rating != 'R':
            return super().rent_a_video(title, rating)
        return "Cannot rent more than three videos at a time or restricted rating for family accounts."
    
class Customer_sx(Customer):
    def rent_a_video(self, title, rating=None):
        if len(self.current_video_rentals) < 1:
            return super().rent_a_video(title, rating)
        return "Cannot rent more than one video at a time"
    
class Customer_px(Customer):
    def rent_a_video(self, title, rating=None):
        if len(self.current_video_rentals) < 3:
            return super().rent_a_video(title, rating)
        return "Cannot rent more than three videos at a time."

class Customer_sf(Customer):
    def rent_a_video(self, title, rating=None):
        if len(self.current_video_rentals) < 1 and rating != 'R':
            return super().rent_a_video(title, rating)
        return "Cannot rent more than one video at a time or restricted rating for family accounts."
    