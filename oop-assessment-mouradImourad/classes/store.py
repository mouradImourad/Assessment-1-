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
from classes.customer_types import *
from classes.video import Video

class Store:
    def __init__(self,name):
        self.name = name
        self.load_data()

    def __repr__(self):
        return f"{self.name}"
    
    def customer_type_maker(self, customer_dict=None):
        account_type = customer_dict["account_type"]
        if account_type == 'pf':
            return Customer_pf(**customer_dict)
        elif account_type == 'sf':
            return Customer_sf(**customer_dict)
        elif account_type == 'sx':
            return Customer_sx(**customer_dict)
        elif account_type == 'px':
            return Customer_px(**customer_dict) 
    
    def load_data(self):
        self.load_customers('data/customers.csv')
        self.load_videos('data/videos.csv')
    
    def load_customers(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'customers' in filename:
                for row in reader:
                    customer_dict = Customer.create_a_customer_dict(row['id'], row['first_name'], row['last_name'], row['account_type'])
                    customer = self.customer_type_maker(customer_dict)
                    if customer.id not in Customer.customers:
                        Customer.add_a_customer(customer)

    def load_videos(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'videos' in filename:
                for row in reader:
                    video = Video(row['id'], row['title'], row['rating'], row['release_year'], row['copies_available'])
                    Video.add_a_video(video)

    def run_the_store(self):
        while True:
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
                self.handle_customer_videos()
            elif choice == '3':
               self.add_a_customer()
            elif choice == '4':
                self.rent_a_video()
            elif choice == '5':
                self.return_a_video()
            elif choice == '6':
                return "Thank you, please come again!"
                break
            else:
                print("Not a valid choice Please enter a number between 1-6")
    
    def handle_customer_videos(self):
        try:
            customer_id = int(input("Enter customer ID: "))
            customer = Customer.get_customer_by_id(customer_id)
            if customer:
                print(customer.get_customer_rented_videos())
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input. Please enter a valid title")
    
    def add_a_customer(self):
        while True:
            try:
                _id = input("Enter customer ID: ")
                if not _id.isdigit():
                    raise ValueError("Customer ID must be an integer.")
                _id = int(_id)

                first_name = input("Enter first name: ")
                if not first_name.isalpha():
                    raise ValueError("First name must contain only letters")
                
                last_name = input("Enter last name: ")
                if not last_name.isalpha():
                    raise ValueError("Last name must contain only letters.")
                
                account_type = input("Enter account type: ")
                if account_type not in ['pf', 'sf', 'sx', 'px']:
                    raise ValueError("Account type must be one of 'pf', 'sf', 'sx, 'px'")

                customer_dict = Customer.create_a_customer_dict(int(_id), first_name, last_name, account_type)
                customer = self.customer_type_maker(customer_dict)
                if customer:
                    if customer.id not in Customer.customers:
                        Customer.add_a_customer(customer)
                        print("New customer added: {customer}")
                    else:
                        print(f"Customer with ID {customer.id} already exists.")
                else:
                    print("Failed to add customer.")
            except ValueError:
                print("Invalid input. Customer ID must be an integer.")
            except Exception as e:
                print("An error ccurred {str(e)}")
            finally:
                break

    def rent_a_video(self):
        try:
            customer_id = int(input("Enter customer ID: "))
            customer = Customer.get_customer_by_id(customer_id)
            if customer:
                title = input("Enter a video title: ")
                video = Video.get_a_video_by_title(title)
                rating = video.rating
                if video and video.copies_available > 0:
                    customer.rent_a_video(video.title, rating)
                    video.copies_available -= 1
                else:
                    print("Video not available for rent.")
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input. Customer ID must be an integer.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def return_a_video(self):
        try:
            customer_id = int(input("Enter customer ID: "))
            customer = Customer.get_customer_by_id(customer_id)
            if customer:
                title = input("Enter a video title to return: ")
                video = Video.get_a_video_by_title(title)
                if video:
                    result = customer.rent_a_video(title, video.rating)
                    video.copies_available += 1
                    print(result)
                else:
                    print("Video not found")
            else:
                print("Customer not found.")
        except ValueError:
            print("Invalid input. Customer ID must be an integer.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")