"""
To do list :

x create store class
x create customers class 
X create video class 
x create customers types subclasses  
- Viewing the current video inventory for the store
- Viewing a customer's current rented videos
  - Get a customer _by id_
  - Display a list of currently rented titles
- Adding a new customer
  - You should not have an initial list of video rentals assigned to a newly created customer
  - No duplicate ID's
- Renting a video out to a customer
  - Get video _by title_
  - Decrement video copies
- Returning a video from a customer
  - Get video _by title_
  - Increment video copies
- Exiting the application

"""
from classes.video import Video

from classes.customer import Customer

from classes.store import Store

block_buster = Store("Block Buster")
print(block_buster)

Alex = Customer(100, "Alex", "Hamilton", "sx", "the Godfather")
print(Alex)

Godfather = Video(5, "Godfather", "G", 1995, 5)
print(Godfather)

all_customers = Customer.load_all_customers()
print(all_customers)
# Blockbuster.customers = all_customers

