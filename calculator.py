# TI-84 Style Calculator in Python (Terminal Version)
# Colors using ANSI escape codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

import math

def print_title():
    print(f"{CYAN}==============================")
    print(f"    TI-84 Python Calculator   ")
    print(f"=============================={RESET}")

def menu():
    print(f"{YELLOW}Select Operation:{RESET}")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Trig Functions (sin, cos, tan)")
    print("8. Logarithms (log, ln)")
    print("9. Factorial (!)")
    print("10. Basic Statistics (mean, median, mode)")
    print("11. Quit")

def get_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def statistics():
    data = input("Enter numbers separated by spaces: ").split()
    data = [float(x) for x in data]
    n = len(data)
    mean = sum(data) / n
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n//2-1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    # Mode calculation
    freq = {}
    for num in data:
        freq[num] = freq.get(num, 0) + 1
    mode = max(freq, key=freq.get)
    print(f"{GREEN}Mean: {mean}, Median: {median}, Mode: {mode}{RESET}")

def calculator():
    while True:
        print_title()
        menu()
        choice = input(f"{MAGENTA}Enter choice (1-11): {RESET}")
        
        if choice == "1":
            a, b = get_numbers()
            print(f"{GREEN}Result: {a + b}{RESET}")
        elif choice == "2":
            a, b = get_numbers()
            print(f"{GREEN}Result: {a - b}{RESET}")
        elif choice == "3":
            a, b = get_numbers()
            print(f"{GREEN}Result: {a * b}{RESET}")
        elif choice == "4":
            a, b = get_numbers()
            if b != 0:
                print(f"{GREEN}Result: {a / b}{RESET}")
            else:
                print(f"{RED}Error: Division by zero!{RESET}")
        elif choice == "5":
            a, b = get_numbers()
            print(f"{GREEN}Result: {a ** b}{RESET}")
        elif choice == "6":
            a = float(input("Enter number: "))
            if a >= 0:
                print(f"{GREEN}Result: {math.sqrt(a)}{RESET}")
            else:
                print(f"{RED}Error: Negative number!{RESET}")
        elif choice == "7":
            func = input("Enter trig function (sin, cos, tan): ").lower()
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            if func == "sin":
                print(f"{GREEN}Result: {math.sin(rad)}{RESET}")
            elif func == "cos":
                print(f"{GREEN}Result: {math.cos(rad)}{RESET}")
            elif func == "tan":
                print(f"{GREEN}Result: {math.tan(rad)}{RESET}")
            else:
                print(f"{RED}Invalid function!{RESET}")
        elif choice == "8":
            func = input("Enter log type (log, ln): ").lower()
            num = float(input("Enter number: "))
            if num > 0:
                if func == "log":
                    print(f"{GREEN}Result: {math.log10(num)}{RESET}")
                elif func == "ln":
                    print(f"{GREEN}Result: {math.log(num)}{RESET}")
                else:
                    print(f"{RED}Invalid function!{RESET}")
            else:
                print(f"{RED}Error: Number must be positive!{RESET}")
        elif choice == "9":
            n = int(input("Enter number: "))
            if n >= 0:
                fact = 1
                for i in range(1, n+1):
                    fact *= i
                print(f"{GREEN}Result: {fact}{RESET}")
            else:
                print(f"{RED}Error: Negative number!{RESET}")
        elif choice == "10":
            statistics()
        elif choice == "11":
            print(f"{CYAN}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice!{RESET}")
        input(f"{BLUE}Press Enter to continue...{RESET}")

calculator()
