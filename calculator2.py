# TI-84 Terminal Graphing Calculator
import math

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def print_title():
    print(f"{CYAN}==============================")
    print(f"   TI-84 Python Graphing Calc  ")
    print(f"=============================={RESET}")

def menu():
    print(f"{YELLOW}Select Operation:{RESET}")
    print("1. Arithmetic (+, -, *, /)")
    print("2. Powers / Roots")
    print("3. Trigonometry (sin, cos, tan)")
    print("4. Logarithms (log, ln)")
    print("5. Factorial")
    print("6. Statistics (mean, median, mode, std)")
    print("7. Matrices (add, multiply, determinant, transpose)")
    print("8. Graph a function (y=f(x))")
    print("9. Quit")

def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def statistics():
    data = list(map(float, input("Enter numbers separated by spaces: ").split()))
    n = len(data)
    mean = sum(data) / n
    sorted_data = sorted(data)
    median = sorted_data[n//2] if n % 2 != 0 else (sorted_data[n//2-1]+sorted_data[n//2])/2
    # Mode
    freq = {}
    for num in data:
        freq[num] = freq.get(num,0)+1
    mode = max(freq, key=freq.get)
    # Standard deviation
    variance = sum((x - mean)**2 for x in data)/n
    std_dev = math.sqrt(variance)
    print(f"{GREEN}Mean: {mean}, Median: {median}, Mode: {mode}, Std Dev: {std_dev}{RESET}")

# Matrix functions
def matrix_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mat = []
    for r in range(rows):
        row = list(map(float, input(f"Enter row {r+1} numbers separated by spaces: ").split()))
        if len(row) != cols:
            print(f"{RED}Row length does not match columns!{RESET}")
            return matrix_input()
        mat.append(row)
    return mat

def matrix_addition(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        print(f"{RED}Cannot multiply: incompatible dimensions!{RESET}")
        return None
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def matrix_transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def matrix_determinant(M):
    # Only 2x2 or 3x3 for simplicity
    if len(M) == 2 and len(M[0]) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    elif len(M) == 3 and len(M[0]) == 3:
        a,b,c = M[0]
        d,e,f = M[1]
        g,h,i = M[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    else:
        print(f"{RED}Determinant only supported for 2x2 or 3x3 matrices.{RESET}")
        return None

# Graphing function using ASCII
def graph_function():
    func_str = input("Enter function of x (e.g., x**2, math.sin(x)): y = ")
    x_min = float(input("Enter x min: "))
    x_max = float(input("Enter x max: "))
    y_min = float(input("Enter y min: "))
    y_max = float(input("Enter y max: "))
    width = 60
    height = 20
    grid = [[" "]*width for _ in range(height)]

    for i in range(width):
        x = x_min + i*(x_max - x_min)/width
        try:
            y = eval(func_str)
        except:
            print(f"{RED}Error evaluating function!{RESET}")
            return
        j = int((y_max - y)*(height-1)/(y_max - y_min))
        if 0 <= j < height:
            grid[j][i] = "*"

    # Draw axes
    x_axis = int((y_max)/(y_max - y_min)*(height-1))
    y_axis = int((-x_min)/(x_max - x_min)*(width-1))
    if 0 <= x_axis < height:
        for i in range(width):
            if grid[x_axis][i] == " ":
                grid[x_axis][i] = "-"
    if 0 <= y_axis < width:
        for i in range(height):
            if grid[i][y_axis] == " ":
                grid[i][y_axis] = "|"
            elif grid[i][y_axis] == "-":
                grid[i][y_axis] = "+"

    print(f"{GREEN}")
    for row in grid:
        print("".join(row))
    print(f"{RESET}")

def calculator():
    while True:
        print_title()
        menu()
        choice = input(f"{MAGENTA}Enter choice (1-9): {RESET}")
        
        if choice == "1":
            a, b = get_numbers()
            op = input("Enter operation (+, -, *, /): ")
            if op == "+": print(f"{GREEN}Result: {a+b}{RESET}")
            elif op == "-": print(f"{GREEN}Result: {a-b}{RESET}")
            elif op == "*": print(f"{GREEN}Result: {a*b}{RESET}")
            elif op == "/": print(f"{GREEN}Result: {a/b if b!=0 else 'Error'}{RESET}")
            else: print(f"{RED}Invalid operation{RESET}")
        elif choice == "2":
            a = float(input("Enter number: "))
            b = float(input("Enter power/root: "))
            print(f"{GREEN}Result: {a**b}{RESET}")
        elif choice == "3":
            func = input("Trig function (sin, cos, tan): ").lower()
            angle = float(input("Angle in degrees: "))
            rad = math.radians(angle)
            if func == "sin": print(f"{GREEN}Result: {math.sin(rad)}{RESET}")
            elif func == "cos": print(f"{GREEN}Result: {math.cos(rad)}{RESET}")
            elif func == "tan": print(f"{GREEN}Result: {math.tan(rad)}{RESET}")
            else: print(f"{RED}Invalid function{RESET}")
        elif choice == "4":
            func = input("Log type (log, ln): ").lower()
            num = float(input("Enter number: "))
            if num <= 0: print(f"{RED}Number must be positive{RESET}")
            else:
                if func == "log": print(f"{GREEN}Result: {math.log10(num)}{RESET}")
                elif func == "ln": print(f"{GREEN}Result: {math.log(num)}{RESET}")
                else: print(f"{RED}Invalid function{RESET}")
        elif choice == "5":
            n = int(input("Enter number: "))
            if n < 0: print(f"{RED}Cannot factorial negative{RESET}")
            else:
                fact = 1
                for i in range(1,n+1): fact *= i
                print(f"{GREEN}Result: {fact}{RESET}")
        elif choice == "6":
            statistics()
        elif choice == "7":
            print("Matrix Operations: add, multiply, transpose, determinant")
            op = input("Enter operation: ").lower()
            if op in ["add","multiply"]:
                print("Matrix A:")
                A = matrix_input()
                print("Matrix B:")
                B = matrix_input()
                if op == "add": 
                    result = matrix_addition(A,B)
                else:
                    result = matrix_multiplication(A,B)
                if result: print(f"{GREEN}Result: {result}{RESET}")
            elif op == "transpose":
                print("Matrix:")
                M = matrix_input()
                print(f"{GREEN}Result: {matrix_transpose(M)}{RESET}")
            elif op == "determinant":
                print("Matrix:")
                M = matrix_input()
                det = matrix_determinant(M)
                if det != None: print(f"{GREEN}Determinant: {det}{RESET}")
            else:
                print(f"{RED}Invalid matrix operation{RESET}")
        elif choice == "8":
            graph_function()
        elif choice == "9":
            print(f"{CYAN}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice!{RESET}")
        input(f"{BLUE}Press Enter to continue...{RESET}")

calculator()

