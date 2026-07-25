# 💻 Exercises: Day 11
# Exercises: Level 1

def add_two_numbers(a, b):
    print(f"a + b = {a + b}")


add_two_numbers(2, 3)

# 2


def area_of_circle(r):
    print(f"The Area of the Circle is = {(3.14 * r ** 2)}")


area_of_circle(5)

# 3


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) == int:
            total += num
        else:
            print("Invalid")
    print(f"The total is = {total}")


add_all_nums(1, 2, 3, 4, 5)

# 4


def convert_temperature(c):
    coverted = (c * 9/5) + 32
    print(f"The Temperature in Fahrenheit is {coverted} degrees")


convert_temperature(25)

# 5


def check_season(month):
    if month in ["September", "October", "November"]:
        print("The season is Autumn")
    elif month in ["December", "January", "February"]:
        print("The season is Winter")
    elif month in ["March", "April", "May"]:
        print("The season is Spring")
    elif month in ["June", "July", "August"]:
        print("The season is Summer")


check_season("January")

# 6


def calculate_slope(y2, y1, x2, x1):
    slope = (y2 - y1) / (x2-x1)
    print(f"The slope is {slope}")


calculate_slope(9, 3, 4, 1)

# 7


def solve_quadratic_eqn(a, b, c):
    d = (((b**2) - 4 * a * c) ** 0.5) / (2 * a)
    solution_1 = -b + d
    solution_2 = -b - d
    print(f"The solutions are {solution_1} and {solution_2}")


solve_quadratic_eqn(1, 8, 2)

# 8


def print_list(given_list):
    for members in given_list:
        print(members)


print_list(["dog", "cat", 18, "extra", True, False])


# 9
def reverse_list(a_given_list):
    new_lst = []
    for members in a_given_list[::-1]:
        new_lst.append(members)
    print(new_lst)


reverse_list([1, 2, 3, 4, 5])

# 10


def capitalize_list_items(cap):
    capitalised_list = []
    for elements in cap:
        capitalised_list.append(elements.capitalize())
    print(capitalised_list)


capitalize_list_items(["dog", "cat", "extra"])

# 11


def add_item(lst, item):
    lst.append(item)

    return (lst)


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))

# 12


def remove_item(lst1, item1):
    if item1 in lst1:
        lst1.remove(item1)

    return (lst1)


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

# 13


def sum_of_numbers(num):
    total = 0
    for numbers in range(0, num+1):
        total += numbers
    print(total)


sum_of_numbers(10)

# 14


def sum_of_odds(odd):
    if odd % 2 == 0:
        print("pick an odd number next time")
        return
    total = 0
    for numbers in range(0, odd + 1):
        if numbers % 2 != 0:
            total += numbers

    print(total)


sum_of_odds(91)

# 15


def sum_of_even(even):
    if even % 2 != 0:
        print("pick an even number next time")
        return
    total = 0
    for numbers in range(0, even + 1):
        if numbers % 2 == 0:
            total += numbers

    print(total)


sum_of_even(90)

# Exercises: Level 2

# 1


def evens_and_odds(pos):
    count_evens = count_odds = 0
    for numbers in range(pos+1):
        if numbers % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1

    print(
        f"The number of odds are {count_odds}. \nThe number of evens are {count_evens}.")


evens_and_odds(100)

# 2


def factorial(whole):
    total = 1
    for i in range(1, whole + 1):
        total *= i
    return total


print(factorial(5))

# 3


def is_empty(self):
    if len(self) == 0:
        print("the list is empty")
    else:
        print("the list is not empty")


is_empty([])


# 3
def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    mean = total / len(numbers)
    return mean


print(calculate_mean([2, 3, 7, 9, 5]))


def calculate_median(numbers):
    sorted_nums = sorted(numbers) 
    
    length = len(sorted_nums)
    
    if length % 2 != 0:
        return sorted_nums[length // 2]
    else:
        middle_right = sorted_nums[length // 2]
        middle_left = sorted_nums[(length // 2) - 1]
        return (middle_left + middle_right) / 2

print(calculate_median([2, 3, 7, 9, 5]))

print(calculate_median([2, 3, 7, 5]))

def calculate_mode(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
   
    max_count = 0
    mode = numbers[0] 
    
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            mode = num
            
    return mode



def calculate_range(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    return highest - lowest


def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    squared_diffs = []
 
    for num in numbers:
        difference = num - mean
        squared = difference ** 2
        squared_diffs.append(squared)
        
    return calculate_mean(squared_diffs)

def calculate_std(numbers):
    variance = calculate_variance(numbers)

    return variance ** 0.5

my_data = [10, 12, 23, 23, 16, 23, 21, 16]

print("Mean:", calculate_mean(my_data))
print("Median:", calculate_median(my_data))
print("Mode:", calculate_mode(my_data))
print("Range:", calculate_range(my_data))
print("Variance:", calculate_variance(my_data))
print("Standard Dev:", calculate_std(my_data))



#4
def greet(name = "Guest"):
    return "Hello, " + name + "!"
print(greet())
print(greet("Gid"))

#5
def show_args(**args):
    formatted_items = []
    for k1, v1 in args.items():
            formatted_items.append(f"{k1}: {v1}")
        
    final_string = ", ".join(formatted_items)
    print(f"Received: {final_string}")
                  

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")


#Exercises: Level 3
#1
def is_prime(number):
    for num in range(2,number):
        if number % num ==0:
            return ("The number is not prime")
    return ("The number is prime")
print(is_prime(47))

#2
def are_all_unique(lst):
    if len(lst) == len(set(lst)):
        return "They are Unique"
    else:
        return "They are Not Unique"

print(are_all_unique([1, 2, 3, 4]))    
print(are_all_unique([1, 2, 3, 3, 4])) 

#3
def data_type(lst):
    if len(lst) == 0:
        return True
    
    first_type = type(lst[0])
    for elements in lst:
        if type(elements) != first_type:
            return False
        else:
            return True
        
print(data_type([1, 2, 3, 4]))          
print(data_type(["apple", "dog", 99]))

#4
def is_valid_variable(variable):
    if variable.isidentifier() == True:
        return ("It's True")
    else:
        return ("It's False")
print(is_valid_variable("my_var_1"))  
print(is_valid_variable("1st_var"))   
print(is_valid_variable("my var"))   

