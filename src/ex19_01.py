#!/usr/bin/env python
#-*- coding : utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses." % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket!\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+8, 5+9)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 5, amount_of_crackers - 3)

print "Get input from user:"
amount_of_cheese_input = int(raw_input("Amount of cheese > "))
amount_of_crackers_input = int(raw_input("Amount of crackers > "))

cheese_and_crackers(amount_of_cheese_input, amount_of_crackers_input)

