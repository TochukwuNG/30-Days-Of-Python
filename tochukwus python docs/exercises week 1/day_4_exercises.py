# 1
string_1 = 'Thirty', 'Days', 'Of', 'Python'
final_str = ' '.join(string_1)
print(final_str)

# 2
string_2 = 'Coding', 'For', 'All'
final_string = " ".join(string_2)
print(final_string)

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
sliced = company[0:6]
print(sliced)

# 10
print(company.find("Coding"))

# 11
print(company.replace("Coding", "Python"))

# 12
string_3 = "Python for Everyone"
print(string_3.replace("Everyone", "All"))

# 13
print(company.split())

# 14
string_4 = ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
print(string_4.split(", "))

# 15
print(company[0])

# 16
print(len(company)-1)

# 17
print(company[10])

# 18
name_1 = 'Python For Everyone'
print(name_1[0] + name_1[7] + name_1[11])

# 19
name_2 = 'Coding For All'
print(name_2[0] + name_2[7] + name_2[11])

# 20
print(company.index("C"))

# 21
print(company.index("F"))

# 22
print(company.rfind("l"))

# 23
sentence = (
    'You cannot end a sentence with because because because is a conjunction')

print(sentence.index("because"))

# 24
print(sentence.rindex("because"))

# 25
sliced_out = sentence[31:54]
print(sliced_out)

# 26
print(sentence.find("because"))

# 27
sliced_out_2 = sentence[31:54]
print(sliced_out_2)

# 28
print(company.startswith("Coding"))

# 29
print(company.endswith("Coding"))

# 30
trailing = '   Coding For All      '
print(trailing.strip())

# 31
sentence_1 = ("30DaysOfPython")
sentence_2 = ("thirty_days_of_python")
print(sentence_1.isidentifier())
print(sentence_2.isidentifier())

# The 2nd variable returns True

# 32
list_1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined = "# ".join(list_1)
print(joined)

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name\tAge\tCountry\tCity")
age = 250
print(f"Asabeneh\t{age}\tFinland\tHelsinki")

# 35
radius = 10
area = 3.14 * radius ** 2
result = 'The area of a circle with radius {} is {} meters square.'.format(
    str(radius), str(area))
print(result)

# 36
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
