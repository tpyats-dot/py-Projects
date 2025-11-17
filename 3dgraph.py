import math

# Settings
WIDTH = 60
HEIGHT = 30
X_RANGE = (-10, 10)
Y_RANGE = (-10, 10)

# Ask the user for a function
func_input = input("Enter a function f(x, y): ")

def f(x, y):
    try:
        return eval(func_input)
    except:
        return 0

# Generate the 3D plot as ASCII
for i in range(HEIGHT):
    y = Y_RANGE[1] - (i / HEIGHT) * (Y_RANGE[1] - Y_RANGE[0])
    line = ""
    for j in range(WIDTH):
        x = X_RANGE[0] + (j / WIDTH) * (X_RANGE[1] - X_RANGE[0])
        z = f(x, y)
        # Convert z to ASCII char
        if z > 5:
            char = "^"
        elif z > 2:
            char = "*"
        elif z > 0:
            char = "."
        elif z > -2:
            char = "-"
        elif z > -5:
            char = "~"
        else:
            char = "_"
        line += char
    print(line)
