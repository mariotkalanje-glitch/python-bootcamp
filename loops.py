for i in range(5):
    print(f'Hello Mariot! This is line {i + 1}')
fruits = ["banana", "apple", "mango", "orange"]

for fruit in fruits:
    print(f"I like {fruit}")
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Mariot")
greet("Fred")
greet("Sarah")
def greet_all(names):
    for name in names:
        print(f"Hello, {name}! Welcome to Python.")

my_friends = ["Mariot", "Fred", "Sarah", "Anna"]
greet_all(my_friends)
def count_down(number):
    while number > 0:
        print(f"Counting down: {number}")
        number = number - 1
    print("Blast off!")

count_down(5)
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(10, 5)
print(f"10 + 5 = {answer}")

answer2 = add_numbers(100, 250)
print(f"100 + 250 = {answer2}")