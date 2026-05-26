# Exercises: Day 6
# Exercises: Level 1
# 1
empty = ()

# 2
brothers = ('David', 'Daniel')
sisters = ('Fibi', 'Phoebe')
print(brothers)
print(sisters)


# 3
siblings = brothers + sisters
print(siblings)

# 4
print(len(siblings))

# 5
family_members = siblings + ('Phil', 'Cecilia')
print(family_members)


# Exercises: Level 2
# 1
siblings = family_members[0:4]
parents =family_members[4:]
print(siblings)
print(parents)

#2
fruits = ('mango', 'banana', 'orange')
vegetables = ('tomato', 'potato', 'carrot')
animal_products = ('milk', 'meat', 'butter')

food_stuff_tp = fruits +vegetables +animal_products
print(food_stuff_tp)

#3
food_stuff_lt = list(food_stuff_tp)

#4
middle_index = len(food_stuff_lt) // 2
print(food_stuff_lt[middle_index])

#5
first = food_stuff_lt[0:3]
last = food_stuff_lt[-3:]
print(f"The first is {first}, the last is {last}")

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
