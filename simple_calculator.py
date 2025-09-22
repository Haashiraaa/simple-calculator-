#simple_calculator.py

import math
from functools import reduce
from operator import sub, truediv

END_PROGRAM = '0000'
user_number = []
last_result = None

def add(n):
    """Return sum of n"""
    return sum(n)
   
def subtract(n):
    """Return result after subtraction"""
    return reduce(sub, n)
    
def multiply(n):
    """Return result of multiplication"""
    return math.prod(n)

def divide(n):
    """Return result after division"""
    return reduce(truediv, n)

def main_menu():
    """Display user options"""
    options = ['Add➕', 'Subtract➖', 'Multiply✖️', 'Divide➗', 'Quit🚫']
    print("\nMain Menu")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
        
def get_number():
    """Prompt user for numbers until program ends"""
    global last_result
    if last_result is not None:
        use_last = input(f"Do you want to use {last_result} "
                         "as your next number? (y/n) ").lower().strip()
        if use_last == 'y':
        #Allows continued calculation,
        #with answer from last arithmetic calculation
            user_number.append(last_result)
  
    print(f"\nEnter numbers (enter '{END_PROGRAM}' to see result)")
    while True:
        number = input("number: ").strip()
        if number == END_PROGRAM:
            break
        try: 
            user_number.append(int(number))
        except ValueError:
            print("Oops! Not a valid number ❗")

def main():
    global last_result
    print("Simple Calculator🔢")   
    while True:
        #clearing user_number so new operations can be carried out
        user_number.clear() 
        main_menu()
        choice = input(f"\nEnter an option from 1 to 5 "
                       f"(enter '{END_PROGRAM}' to quit)\n>>> ").strip()
        
        if choice == END_PROGRAM:
            print("Goodbye! 👋🏾")
            print("\nMADE BY HAASHIRAA. 👨🏾‍💻")
            break
        
        if choice == "1":
            get_number()
            last_result = add(user_number)
            print(f"\t= {last_result}")
            
        elif choice == "2":
            get_number()
            last_result = subtract(user_number)
            print(f"\t= {last_result}")
                
        elif choice == "3":
            get_number()
            last_result = multiply(user_number)
            print(f"\t= {last_result}")
                
        elif choice == "4":
            get_number()
            try:
                last_result = divide(user_number)
                print(f"\t= {last_result}")
            except ZeroDivisionError:
                print("\nYou can't divide by 0! 🙅🏾‍♂️")
        
        else:
            print("\nOption is out of range!")

if __name__ == "__main__":
    main()