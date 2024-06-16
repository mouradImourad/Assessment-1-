# Write your Store Class here

""" 
Store class based on the given data in the README.md will include: 
-one instance attribute "name" --> type(str)
-three instance method 
* load_data 
* customer_type_maker
* run_the_store

""" 
class Store:
    def __init__(self,name):
        self.name = name
   
    def __repr__(self):
        return f" {self.name}"    

    def customer_type_maker(self, customer_info):
        pass

    def run_the_store(self):
        pass

