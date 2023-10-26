#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
numbers = (5,-2,12,-8,14,16)
squared_numbers=[]
for num in numbers:
    if num >0:
        squared_numbers.append(num**2)
        print("the squared numbers in the list are:", squared_numbers)