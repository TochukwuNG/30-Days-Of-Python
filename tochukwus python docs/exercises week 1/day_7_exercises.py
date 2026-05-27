# Exercises: Day 7
# 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

# 2
it_companies.add('Twitter')
print(it_companies)

# 3
it_companies.update(['Nvidia', 'Samsung', 'Huawei'])
print(it_companies)

# 4
it_companies.remove('IBM')
print(it_companies)

# 5
it_companies.discard('IBM')
print(it_companies)
'''Unlike set.remove(), the discard() method does not raise
an exception when an element is missing from the set.'''

# Exercises: Level 2
# 1
joined_set = A.union(B)
print(joined_set)

# 2
intersection = A.intersection(B)
print(intersection)

# 3
print(A.issubset(B))

# 4
print(A.isdisjoint(B))

# 5
join_a = A.union(B)
print(join_a)
join_b = B.union(A)
print(join_b)
print(join_a == join_b)

# 6
print(A.symmetric_difference(B))

# 7
del A
del B

# Exercises: Level 3
# 1
age_set = set(age)
print(f"List length: {len(age)}")
print(f"Set length: {len(age_set)}")
print("The list is bigger")

# 2
''' A String is simple a combination of characters enclosed in quotation marks
A list is a group of ordered, indexed items which can be modified, sorted,etc
A tuple  group of ordered, indexed items  but cannot be reassigned
A set is a group of unordered, unindexed and unigue items.

'''

# 3
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")
print(f"Unique words: {unique_words}")
