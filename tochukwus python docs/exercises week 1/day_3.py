#Day 3 Exercises


age = 18
height = float(1.78)
complex_number = 2 + 3j
base = int(input("Enter base: "))
height = int(input("Enter height: "))
Area = 0.5 * base * height
print("The area of the triangle is ", Area)

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is ", perimeter)

length = int(input("Enter length: "))
width = int(input("Enter width: "))
perimeter_rectangle = 2 * (length + width)
print("Perimeter of rectangle: ", perimeter_rectangle)

radius = int(input("Enter radius: "))
PI = 3.14
area_circle = PI * radius ** 2
circumference = 2 * PI * radius
print("Area of circle: ", area_circle)
print("Circumference: ", circumference)

slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope  # solving: 0 = 2x - 2 → x = 2/2 = 1

print(f"Slope: {slope}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

Y_1 = 2
Y_2 = 10
X_1 = 2
X_2 = 6
m = (Y_2 - Y_1)/X_2 - X_1
print(m)

print(slope == m)

for x in range (-10,10):
    y = (x ** 2 + 6 * x + 9 )
    if y==0:
     print(f'Solution found. When x = {x}, y = 0 ')


python = "python"
dragon = "dragon"

print(len(python) == len(dragon))

print("on" in python and "on" in dragon)

print("jargon" in "I hope this course is not full of jargon.")

print("on" not in dragon and "on" not in python)

length_py = str(float(len(python)))
print(type(length_py))

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
   print(f"{num} is odd")


number_1 = int("2")
print(7//3 == number_1)

print(type('10') == type(10))

print(float('9.8') == 10)  # error in question changed to float

hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
pay =  hours * rate_per_hour

print("Your weekly earning is " ,pay)

years = int(input("Enter number of years you have lived: "))
seconds = years * 60 * 60 *24 * 365
print("You have lived for ", seconds ,"seconds." )

for a in range (1,6):
   print(a, 1, a, a**2, a**3)



