"""
To do list :

x create store class
x create customers class 
3. create video class 
4. create customers types subclasses 
5. load the customers from csv 
6. load the videos from csv
7. add new customer
8. rent video
9. return video 
10.creat menu 

"""


from classes.customer import Customer

from classes.store import Store

block_buster = Store("Block Buster")
print(block_buster)

Alex = Customer(100, "Alex", "Hamilton", "sx", "the Godfather")
print(Alex)
