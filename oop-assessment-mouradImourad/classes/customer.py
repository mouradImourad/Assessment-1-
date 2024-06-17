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
    
    def __init__(self, id=None, first_name=None, last_name=None, account_type=None, current_video_rentals=None):
        self._id = id
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = account_type
        self._current_video_rentals = current_video_rentals or []

    def __repr__(self):
        return f"{self._id} {self._account_type} {self.first_name} {self.last_name} {self._current_video_rentals}"
    


    @property
    def id(self):
        return self._id

    @property
    def current_video_rentals(self):
        return self._current_video_rentals

    @current_video_rentals.setter
    def current_video_rentals(self, value):
        if not isinstance(value, list):
            raise ValueError("Current Video Rentals should only be a list")
        self._current_video_rentals = value
    
    @staticmethod
    def create_a_customer_dict(id, first_name, last_name, account_type):
        return {'id': id,
                'first_name': first_name,
                'last_name': last_name,
                'account_type': account_type
                }
    
    @classmethod
    def add_a_customer(cls, customer):
        if not isinstance(customer, Customer):
            raise ValueError("This function will only accept an instance of the Customer class")
        if customer.id in cls.customers:
            raise ValueError(f"Customer with ID {customer.id} already exists.")
        cls.customers[customer.id] = customer
        return f"{customer.first_name} has been added into our database!"
    
    @classmethod
    def get_customer_by_id(cls, customer_id):
        return cls
    
    def get_customer_rented_videos(self):
        rentals = ",".join(self.current_video_rentals)
        return f"{self.first_name} has the following rentals: {rentals}"
    
    def rent_a_video(self, title, rating=None):
        if title not in self._current_video_rentals:
            self._current_video_rentals.append(title)
        return self.get_customer_rented_videos()

    def return_a_video(self, title):
        if title in self._current_video_rentals:
            self._current_video_rentals.remove(title)
        return self.get_customer_rented_videos()












