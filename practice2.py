# Creating a dictionary with Key-Value pairs
student = {
    "name": "Mariot",
    "city": "Mwanza",
    "day": 2
}

# Printing the whole dictionary
print(student)

# Grabbing one specific detail using its Key
print(student["city"])

# Checking a condition to make a decision
if student ["day"] == 1:
    print ("welcome to your first day of coding!")
else: 
    print("Keep up the great momentum!")


if student ["day"] == 1:
    print("Welcome to Day 1: Foundations")
elif student ["day"] == 2:
    print("Welcome to Day 2: Pandas DataFrames!")
else:
    print("Welcome to Day 3: Data Cleansing!")




