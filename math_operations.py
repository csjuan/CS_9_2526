# Created by: 
# Group: 
# Date: 
# Topic, problem, theme: 

#Defining the function (is the process)
def math_operation_addition(num1,num2):
    """
    Displays the addition of two numbers

    Args:
        num1 (int): first number
        num2 (int): second number
    
    Returns:
        addition (int): 
      """
    addition_result = num1 + num2

    return addition_result

def math_operation_subtraction(num1,num2):
    """
    Displays the subtraction of two numbers

    Args:
        num1 (int): first number
        num2 (int): second number
    
    Returns:
        addition (int): 
      """
    subtraction_result = num1 - num2

    return subtraction_result

# Main program
# The user enters the information, calls the function and display the results

print("=== Results ===")
print()

# Get information from user
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# Calling the functions
addition_final_result = math_operation_addition(num1,num2)
subtraction_final_result = math_operation_subtraction(num1,num2)

print(f"\nthe addition= {addition_final_result}")
print(f"\nthe subtraction= {subtraction_final_result}")

