"""Randomly pick customer and print customer info"""

# Add code starting here
# Hint: remember to import any functions you need from
    # other files or libraries

from random import choice 
from customer import Customer
from customer_info import organize_customer_data

def pick_customer(Customer_list):
    """ Choose a random winner from list of customers. """

    chosen_customer = choice(Customer_list)

    print "Contact {name} at {email} to notify them they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )

Customers  = organize_customer_data('customers.txt')
print pick_customer(Customers)
