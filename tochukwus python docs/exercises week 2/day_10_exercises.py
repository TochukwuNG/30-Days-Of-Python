# 💻 Exercises: Day 10
# Exercises: Level 1

# 1
for number in range(11):
    print(number)

a = 0
while a <= 10:
    print(a)
    a += 1

# 2
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

# 3

for b in range(1, 8):
    print("#" * b)

# 4
for c in range(8):
    for j in range(8):
        print("#", end=" ")

    print()

# 5
for x in range(11):
    print(f"{x} x {x} = {x * x}")

# 6
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for skills in lst:
    print(skills)

# 7
even = 0
for even in range(0, 101):
    if even % 2 == 0:
        print(even)

# 8
odd = 0
for odd in range(101):
    if odd % 2 != 0:
        print(odd)


# level 2
# 1
total = 0
for c in range(101):
    total += c
print(f"The sum of all numbers is {total}.")

# 2
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print(
    f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")


# Exercises: Level 3
# 1

# 2

fruit_list = ['banana', 'orange', 'mango', 'lemon']
reversed = []
for fruit in range(len(fruit_list) -1, -1, -1):
    reversed.append(fruit_list[fruit])
print(reversed)

