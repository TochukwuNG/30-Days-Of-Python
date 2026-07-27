# 💻 Exercises: Day 13

# 1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [i for i in numbers if i <= 0]

print(filtered)

# 2
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for j in list_of_lists for i in j]
print(flattened_list)

# 3
lst = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(*lst, sep='\n')

# 4
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for row in countries
    for country, capital in row
]

print(flattened_countries)

# 5
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [
    {'country': country.upper(), 'city': city.upper()}
    for row in countries
    for country, city in row
]

print(*dict_countries, sep='\n')

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_str = [elements[0] + " " + elements[1]
              for row in names for elements in row]
print(concat_str)

# 7


def slope(x1, y1, x2, y2): return (y2 - y1)/(x2 - x1)


print(slope(1, 2, 5, 7))
