# 💻 Exercises: Day 8
# 1
dog = {}

# 2
dog["name"] = "Ben"
dog["color"] = "Brown"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 6
print(dog)

# 3
student_dictionary = {"first_name": "Tochukwu", "last_name": "Nwachukwu", "gender": "Male", "age": 18,
                      "marital_status": "single", "skills": ['JavaScript', 'HTML', 'CSS', 'Python'], "country": "Nigeria", "city": "Abuja", "Address": "Gwarimpa"}
print(student_dictionary)

# 4
print(len(student_dictionary))

# 5
print(type(student_dictionary["skills"]))

# 6
student_dictionary["skills"].append('C')
print(student_dictionary)

# 7
student_keys = student_dictionary.keys()
print(student_keys)

# 8
student_values = student_dictionary.values()
print(student_values)

# 9
tup = student_dictionary.items()
print(tup)

# 10
del student_dictionary["marital_status"]
print(student_dictionary)

# 11
del dog
