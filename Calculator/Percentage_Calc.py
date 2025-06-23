from time import sleep
from random import randint

#Percentage Calc
random_time = randint(1, 8)
def menu():
    while True:
        print(f"""
================================          
            WELCOME!
================================          
This is a percentage calculator.        
What would you like to do?
          
1 -> Apply % in a number 
2 -> Discount % of a number
3 -> Discover a %
4 -> Exit        
""")
        try:
            choices = int(input(f"What option do you want: "))
            if choices in [1, 2, 3, 4]:
                return choices  
            else:
                print(f"\nNumber invalid = [{choices}] try again!")
                sleep(2)
        except ValueError:
            print(f"\nError: Invalid option try only numbers")
            sleep(1)

def percentage_applied():
    while True:
        print(f"""
================================
     PERCENTAGE CALCULATOR
================================
Here you can find out how much -
it will cost if you apply a % to
a value.
""")    
        try:
            value = float(input(f"Define a value: "))

            percentage = float(input(f"Now define the (%): "))

            value_with_percentage = (percentage / 100) * value
        except ValueError:
            print(f"\nError: Invalid option try only numbers")
            sleep(1)
            continue
        sleep(1)
        print(f"""
================================
The value was defined like R${value:.2f} 
and percentage like {percentage:.2f}% and 
{percentage:.2f}% of R${value:.2f} is 
R${value_with_percentage + value:.2f}
================================""") 
        sleep(4)   
        option = returning()
        if option == 1:
            for i in range(random_time):
                print(f"Loading...")
                sleep(0.8)

        elif option == 2:
            print(f"Returning to main menu")
            for i in range(random_time):
                print(f"Loading...")
                sleep(0.5)         
            break
        else:
            print(f"Invalid number = [{option}]!")
            sleep(0.5)
                   
def percentage_discounted():
    while True:
        print(f"""
================================
     PERCENTAGE CALCULATOR
================================
Here you can find out how much -
it will cost if you have a dis -
count             
""")    
        try:
            value = float(input(f"Define a value: "))

            percentage = float(input(f"Now define the (%): "))

            value_discounted = value * (percentage / 100) 
        except ValueError:
            print(f"\nError: Invalid option try only numbers")
            sleep(1)
            continue
        sleep(1)
        print(f"""
================================
The value and percentage defined 
was -> R${value:.2f}, {percentage:.2f}%
therefore if R${value:.2f} have {percentage:.2f}%
of discount it will be discounted 
R${value_discounted:.2f} resulting {value - value_discounted:.2f}
================================""") 
        sleep(4)   
        option = returning()
        if option == 1:
            for i in range(random_time):
                print(f"Loading...")
                sleep(0.8)

        elif option == 2:
            print(f"Returning to main menu")
            for i in range(random_time):
                print(f"Loading...")
                sleep(0.5)         
            break
        else:
            print(f"Invalid number = [{option}]!")
            sleep(0.5)

def discover_percentage():
    while True:
        print(f"""
================================
     PERCENTAGE CALCULATOR
================================
Here you can find out which per-
centage of a discounted value             
""")    
        try:
            total_value = float(input(f"Define a total value: "))

            amount = float(input(f"Now define the amount discounted: "))

            percentage_calc = (amount / total_value) * 100
        except ValueError:
            print(f"\nError: Invalid option try only numbers")
            sleep(1)
            continue
        sleep(1)
        print(f"""
================================
The total value was defined like 
R${total_value:.2f} and the amou
nt discounted like R${amount:.2f}.
now the percentage of R${amount:.2f}
of discount is the {percentage_calc:.2f}%.
================================""") 
        sleep(4)   
        option = returning()
        if option == 1:
            for i in range(random_time):
                print(f"Loading...")
                sleep(0.8)

        elif option == 2:
            print(f"Returning to main menu")
            for i in range(random_time):
                print(f"Loading...")
                sleep(0.5)         
            break
        else:
            print(f"Invalid number = [{option}]!")
            sleep(0.5)
                   
def returning():
    while True:
        print(f"""
================================
       RETURNING OPTION!   
================================
Would you like to do it again or 
return to main menu?
              
1 - Do it again
2 - Return to main menu                                                                               
""")
        try:
         option = int(input(f"Choose the option: "))
         if option in [1, 2]:
            return option
         else:
             print(f"\nInvalid number = [{option}]")
             sleep(1)
        except ValueError:
            print(f"\nError: Invalid option try only numbers")
            sleep(1)

def main():
    while True:
        choices = menu()
        sleep(1)
        if choices == 1:
            percentage_applied()
        elif choices == 2:
            percentage_discounted()
        elif choices == 3:
            discover_percentage()
        elif choices == 4:
            print(f"\nOk, closing the program!")
            exit()
                
main()