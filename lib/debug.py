#!/usr/bin/env python3
# import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

visitor1 = Visitor("Kat")
visitor2 = Visitor("Mike")
visitor3 = Visitor("Serina")
visitor4 = Visitor("Brandon")

park1 = NationalPark("Zion")
park2 = NationalPark("Yosemite")
park3 = NationalPark("Acadia")

trip1 = Trip(visitor1, park1, "April 29th", "May 8th")
trip2 = Trip(visitor1, park2, "August 11th", "August 17th")
trip3 = Trip(visitor2, park2, "August 11th", "August 17th")

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

print("banana")
    # ipdb.set_trace()
