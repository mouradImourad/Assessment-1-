# Write you Customer Class here
"""
* five instances attributes

* _id getter
* current_video_rentals getter
 - current_video_rentals setter # should only accept [] of video titles if it is not list
   the setter should raise an exception 'Current Video Rentals should only be a list'
* creat_a_customer_dict --> static method

* add_a_customer --> cls method
* get_customer_by_id --> cls method

* get_customer_rented_videos --> inst method
* rent_a_video --> inst method
* return_a_video --> inst method

"""
class Customer:
    def __init__(self, id, first_name, last_name, account_type, current_video_rentals):
        self._id = id                     
        self._account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self._current_video_rentals = []

    def __repr__(self):
        return f"{self._id} {self._account_type} {self.first_name} {self.last_name} {self._current_video_rentals}"
    


    @property
    def get_id(self):
        return self._id

    @property
    def get_current_video_rentals(self):
        return self._current_video_rentals

    @get_current_video_rentals.setter
    def get_current_video_rentals(self, value):
        if not isinstance(value, list):
            raise ValueError("Current Video Rentals should only be a list")
        self._current_video_rentals = value



    @staticmethod
    def create_a_customer_dict():
        return {'id': 1, 'first_name': 'Monica', 'last_name': 'Gellar', 'account_type': 'sx'}



    
    @classmethod
    def add_a_customer(cls, customer):
        pass 


    @classmethod
    def get_customer_by_id(cls, customer_id):
        pass

    
    def get_customer_rented_videos(self):
        pass


    
    def rent_a_video(self, video_title, video_rating):
        pass


    def return_a_video(self, video_title):
        pass












