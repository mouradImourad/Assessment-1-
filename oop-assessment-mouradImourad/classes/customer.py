# Write you Customer Class here

class Customer:

    def __init__(self, id, first_name, last_name, account_type, current_video_rentals=None):
        self._id = id
        self._account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self._current_video_rentals = current_video_rentals 

    def __repr__(self):
        return f"{self._id} {self._account_type} {self.first_name} {self.last_name} {self._current_video_rentals}"
    

