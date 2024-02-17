import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Rainbow Animation")
screen.bgcolor("black")

# Create a turtle
rainbow = turtle.Turtle()
rainbow.speed(0)  # Set the fastest drawing speed

# Define colors of the rainbow
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Function to draw the rainbow
def draw_rainbow():
    size = 20
    for color in colors:
        rainbow.color(color)
        rainbow.width(15)  # Set line thickness
        rainbow.penup()
        rainbow.goto(0, -size)
        rainbow.pendown()
        rainbow.circle(size)
        size += 35  # Increase size for more circles

# Hide the turtle
rainbow.hideturtle()

# Function to animate the rainbow
def animate():
    rainbow.clear()
    draw_rainbow()
    screen.update()
    screen.ontimer(animate, 200)  # Even slower animation with a delay of 200 milliseconds

# Start the animation
animate()

# Close the window when clicked
screen.exitonclick()
