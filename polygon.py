import turtle
import random

# Define a list of acceptable colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black", "rainbow"]

def draw_polygon(sides, length, color):
    # Create a turtle object
    polygon = turtle.Turtle()
    
    # Set the fill color
    polygon.fillcolor(color)
    
    # Start filling
    polygon.begin_fill()
    
    for _ in range(sides):
        polygon.forward(length)
        polygon.left(360 / sides)
    
    # End filling
    polygon.end_fill()

# Main loop
while True:
    sides = int(input("Enter the number of sides (1-99): "))
    if 1 <= sides <= 99:
        length = int(input("Enter the length of each side in pixels: "))
        color_choice = input("Enter a color choice or 'rainbow' for random colors: ").lower()
        
        if color_choice == 'rainbow':
            # Generate a random color for each side
            for _ in range(sides):
                random_color = random.choice(colors)
                draw_polygon(1, length, random_color)
        elif color_choice in colors:
            draw_polygon(sides, length, color_choice)
        else:
            print("Invalid color choice. Please choose from the acceptable colors.")
    
    another_polygon = input("Do you want to draw another polygon? (yes/no): ").lower()
    if another_polygon != 'yes':
        break

# Close the Turtle graphics window
turtle.done()
