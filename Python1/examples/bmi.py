# Body Mass Index calculator

print("Mass (kg): ")
mass = int(input())

print("Height (cm): ")
height = int(input())

height = height / 100.0

bmi = mass / (height * height)
print("BMI = ", bmi)
