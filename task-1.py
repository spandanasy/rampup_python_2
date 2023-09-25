import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_area(*args):
    if len(args) == 3 and args[2].lower() == "triangle":
        if all(isinstance(arg, (int, float)) and arg >= 0 for arg in args[:2]):
            return calculate_triangle_area(args[0], args[1])
        else:
            raise ValueError("Please Avoid Negative values")
    elif len(args) == 2:
        if all(isinstance(arg, (int, float)) and arg >= 0 for arg in args):
            return calculate_rectangle_area(args[0], args[1])
        else:
             raise ValueError("Please Avoid Negative values")
    elif len(args) == 1:
        if isinstance(args[0], (int, float)) and args[0] >= 0:
            return calculate_circle_area(args[0])
        else:
             raise ValueError("Please Avoid Negative values")

    raise ValueError("Invalid number of arguments or shape")

# Get user input for the shape's parameters
try:
    user_input = input("Enter the arguments separated by commas: ").split(',')
    args = [float(arg) if arg.replace(".", "", 1).isdigit() else arg.strip() for arg in user_input]
    area = calculate_area(*args)
    if len(args) == 2:
        print("Shape: Rectangle")
    elif len(args) == 1:
        print("Shape: Circle")
    elif len(args) == 3 and args[2].lower() == "triangle":
        print("Shape: Triangle")
    print(f"The area is: {area}")
except ValueError as e:
    print(e)
