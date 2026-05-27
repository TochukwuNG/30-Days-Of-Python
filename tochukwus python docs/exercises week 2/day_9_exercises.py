'''Exercises: Day 9
Exercises: Level 1'''

# 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2
my_age = 18
your_age = int(input("Enter your age: "))
difference_1 = your_age - my_age
difference_2 = my_age - your_age
if my_age < your_age:
    if difference_1 == 1:
        print(f"You are {difference_1} year older than me.")
    else:
        print(f"You are {difference_1} years older than me.")
elif my_age == your_age:
    print("We are the same age")
else:
    print("I am older than you.")


# 3
a = int(input("Enter your number one: "))
b = int(input("Enter your number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2

grade = int(input("Enter your grade: "))
if 90 <= grade <= 100:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


# 2
month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    print("The season is Autumn")
elif month in ["December", "January", "February"]:
    print("The season is Winter")
elif month in ["March", "April", "May"]:
    print("The season is Spring")
elif month in ["June", "July", "August"]:
    print("The season is Summer")

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
user_input = input("Enter a Fruit: ")
if user_input not in fruits:
    fruits.append(user_input)
    print(fruits)
else:
    print('That fruit already exist in the list')

# 4
# Part 1 - Check skills key and print middle skill
person = {
    'first_name': 'Tochukwu',
    'last_name': 'Nwachukwu',
    'age': 18,
    'country': 'Nigeria',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if "skills" in person:
    skills = person["skills"]
    middle = skills[len(skills)//2]
    print(f"Middle skill: {middle}")

#Part 2 - Check if Python is in skills
if "skills" in person:
    if "Python" in person["skills"]:
        print('Python' in person['skills'])
    else:
        print("The person does not have Python skill")


# Part 3 - Check developer type
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')

# Part 4 - Check if married and lives in Finland
if person['is_married'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")
