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
    customers = {}
    
    def __init__(self, _id, first_name, last_name, _account_type, _current_video_rentals=None):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = _account_type
        self._current_video_rentals = _current_video_rentals or []

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
    def create_a_customer_dict(_id, first_name, last_name, _account_type):
        return {'id': _id,
                'first_name': first_name,
                'last_name': last_name,
                'account_type': _account_type
                }
    
    @classmethod
    def add_a_customer(cls, customer):
        if not isinstance(customer, cls):
            raise valueError("This funciton will only acept an instance 0f the Customer class")
        if customer._id in cls.customers:
            return f"Customer with ID {customer._id} already exists!"
        cls.customers[customer._id] = customer
        return f"{customer.first_name} has been added into our database!"
    
    @classmethod
    def get_customer_by_id(cls, _id):
        return cls.customers.get(_id, None)
    
    def get_customer_rented_videos(self):
        rentals = "/".join(self.current_video_rentals)
        return f"{self.first_name} has the following rentals:\n{rentals}"
    
    def rent_a_video(self, title, rating):
        self._current_video_rentals.append(title)
        return f"{self.first_name} has the following rentals:\n{self.current_video_rentals}"


    def return_a_video(self, title):
        self._current_video_rentals.remove(title)
        return f"{self.first_name} has the following rentals:\n{self.current_video_rentals}"












