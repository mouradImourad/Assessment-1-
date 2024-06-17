# Write your Store Class here

""" 
Store class based on the given data in the README.md will include: 
-one instance attribute "name" --> type(str)
-three instance method 
* load_data 


* customer_type_maker
* run_the_store

""" 
import csv
from classes.customer import Customer
from classes.customer_pf import Customer_pf
from classes.customer_sf import Customer_sf
from classes.customer_sx import Customer_sx
from classes.customer_px import Customer_px
from classes.video import Video

class Store:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"
    
    def customer_type_maker(self, customer_dict):
        account_type = customer_dict["account_type"]
        if account_type == 'pf':
            return Customer_pf(**customer_dict)
        elif account_type == 'sf':
            return Customer_sf(**customer_dict)
        elif account_type == 'sx':
            return Customer_sx(**customer_dict)
        elif account_type == 'px':
            return Customer_px(**customer_dict) 
    
    def load_data(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'customers' in filename:
                for row in reader:
                    customer_dict = Customer.create_a_customer_dict(row['id'], row['first_name'], row['last_name'], row['account_type'])
                    customer = self.customer_type_maker(customer_dict)
                    Customer.add_a_customer(customer)
            elif 'videos' in filename:
                for row in reader:
                    video = Video(row['id'], row['title'], row['rating'], row['release_year'], row['copies_available'])
                    Video.add_a_video(video)

    def customer_type_maker(self, customer_info):
        pass

    def run_the_store(self):
        print("== Welcome to Code Platoon Video! ==")
        print("1. View store video inventory")
        print("2. View customer rented videos")
        print("3. Add new Customer")
        print("4. Rent video")
        print("5. Return Video")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            Video.list_inventory()
        elif choice == '2':
            customer_id = int(input("Enter customer ID: "))
            customer = Customer.get_customer_by_id(customer_id)
            if customer:
                print(customer.get_customer_rented_videos())
            else:
                print("Customer not found.")
        elif choice == '3':
            _id = int(input("Enter customer ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            account_type = input("Enter account type (sx/px/sf/pf): ")
            customer_dict = Customer.create_a_customer_dict(_id, first_name, last_name, account_type)
            customer = self.customer_type_maker(customer_dict)
            print(Customer.add_a_customer(customer))
        elif choice == '4':
            customer_id = int(input("Enter customer ID: "))
            title = input("Enter video title: ")
            customer - Customer.get_customer_by_id(customer_id)
            video = Video.get_a_video_by_title(title)
            if customer and video and video.copies_available > 0:
                print(customer.rent_a_video(title, video.rating))
                video.copies_available -= 1
            else:
                print("Unable to rent video.")
        elif choice == '5':
            customer_id: int(input("Enter customer ID: " ))
            title = input("Enter video title: ")
            customer = Customer.get_customer_by_id(customer_id)
            video = Video.get_a_video_by_title(title)
            if customer and video:
                print(customer.return_a_video(title))
                video.copies_available += 1
            else:
                print("Unable to return video.")


