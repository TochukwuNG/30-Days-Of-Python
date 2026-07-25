import random
import string

# Exercises: Day 12
# Exercises: Level 1
# 1


def random_user_id():
    characters = string.ascii_letters + string.digits
    result_list = []
    for _ in range(6):
        result_list.append(random.choice(characters))

    return "".join(result_list)


print(random_user_id())

# 2


def user_id_gen_by_user():
    length = int(input("Enter number of characters: "))
    count = int(input("Enter number of ID's: "))
    chars = string.ascii_letters + string.digits

    id_generated = []
    for _ in range(count):
        single_id_chars = []
        for _ in range(length):
            single_id_chars.append(random.choice(chars))

        finished_id = "#" + "".join(single_id_chars)
        id_generated.append(finished_id)

    return "\n".join(id_generated)


print(user_id_gen_by_user())

# 3


def rgb_color_gen():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)

    return f"#rgb({red},{green},{blue})"


print(rgb_color_gen())

# Exercises: Level 2
# 1


def list_of_hexa_colors(length):
    hex = string.digits + string.ascii_letters[0:6]
    color_list = []
    for i in range(length):
        color = '#'
        for j in range(6):
            color += random.choice(hex)
        color_list.append(color)
    return color_list


print(list_of_hexa_colors(6))

# 2


def list_of_rgb_colors(length):
    rgb_list = []
    for _ in range(length):
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)
        rgb_list.append(f"rgb({red},{green},{blue})")

    return rgb_list


print(list_of_rgb_colors(3))

# 3


def generate_colors(type, number):
    if type == "hexa":
        return list_of_hexa_colors(number)

    elif type == "rgb":
        return list_of_rgb_colors(number)
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."


print(generate_colors("rgb", 5))

# Exercises: Level 3
# 1


def shuffle_list(lst):
    shuffled_list = random.sample(lst, len(lst))

# 2


def seven_unique_randoms():
    return random.sample(range(10), 7)


print(seven_unique_randoms())
