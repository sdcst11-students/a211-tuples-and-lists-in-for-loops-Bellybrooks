# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

import abc


people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")
a=int(input("enter a number less then 10:"))
if a >=0 and a< len (people):
    print("the element at position",a, "is:",people[a])
else:
    print("invalid input. enter a number less then",len(people))