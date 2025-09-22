import turtle

# Window and turtle initialization
window = turtle.Screen()
window.title("For Loops and Functions with Python Turtle")
t = turtle.Turtle()

# --- Function Definitions ---

def draw_polygon(sides, length):
    """
    Draws a regular polygon with the specified number of sides.
    
    Parameters:
    sides (int): The number of sides for the polygon.
    length (int): The length of each side.
    """
    angle = 360 / sides
    t.color("blue")
    t.pensize(2)
    print(f"Drawing a {sides}-sided polygon...")
    
    # For loop to repeat the drawing, using the 'i' variable
    for i in range(sides):
        t.forward(length)
        t.right(angle)

# --- Using the Function ---

# Move the turtle to the starting position
t.penup()
t.goto(-150, 50)
t.pendown()

# Call the function to draw a square
draw_polygon(4, 100)
t.penup()
t.goto(50, 50)
t.pendown()

# ----------------- Exercises to Complete -----------------

# Exercise 1: Easy
# TODO: Use a 'for' loop to draw a triangle with sides of 150.
# Hint: A triangle has 3 sides. What is the turning angle?

# Exercise 2: Medium
# TODO: Use a 'for' loop to draw 5 squares, each with a different color.
# Hint: Define a list of colors like `colors = ["red", "orange", "yellow", "green", "blue"]`.

# Exercise 3: Difficult
# TODO: Create a function called 'draw_flower' that uses a 'for' loop to draw a flower.
# You can make each petal a small circle or a simple shape.
# Hint: A circle can be drawn with `t.circle(radius)`.

# Keeps the window open
window.mainloop()
