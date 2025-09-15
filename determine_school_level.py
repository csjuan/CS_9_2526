# Created by:
# Group:
# Date:
# Topic, problem, theme:

#Definiing the function (is the process)
def determine_school_level(age):
    """
    Determines the appropriate school level based on age
    
    Args:
        age (int): The student's age
    
    Returns:
        str: The appropriate school level
    """
    if 5 <= age <= 10:
        return "Elementary"
    elif 11 <= age <= 13:
        return "Middle School"
    elif 14 <= age <= 18:
        return "High School"
    elif age >= 19:
        return "College"
    else:
        return "Pre-school or not yet school age"

# Main program
# The user enters the information, calls the function and display the results

print("=== School Level Determiner ===")
print("This program will tell you what school level you should be in!")
print()

# Get age from user
age = int(input("Please enter your age: "))

# Determine and display school level
school_level = determine_school_level(age)

print(f"\nAt age {age}, you should be in: {school_level}")


# Add some encouraging messages
# This section is alternative but adds information to the user.
# This section is added by advanced students.

if school_level == "Elementary":
    print("Time to learn the basics and have fun!")
elif school_level == "Middle School":
    print("Get ready for new challenges and adventures!")
elif school_level == "High School":
    print("Focus on your future goals and college prep!")
elif school_level == "College":
    print("Time to specialize and prepare for your career!")
else:
    print("Enjoy playing and getting ready for school!")
