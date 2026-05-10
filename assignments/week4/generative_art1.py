### Basic Turtle cheatsheet

# import turtle
from turtle import *
import random

# initial setup: canvas size
width = 1000
height = 700
setup(width, height)

# turn off animation, comment it out to see the drawing process
tracer(0, 0)
# set background color
bgcolor('white') # You can either use color names
# change the color of the lines
color('#000') # Or Hex Code
penup()

#foxtails
count = 0

for i in range(9):

    getatail = [1, 2]
    nooryes = random.choice(getatail)
    newangle = i * 20
    int(newangle)

    if nooryes == 1:

        count  += 1

        setheading(25 + newangle)

        goto(0, -120)
        pendown()
        forward(197.99)
        right(45)
        forward(102.49)
        right(120)
        forward(102.49)
        goto(0, -120)
        penup()

    else:
        goto(0, -120)
        penup()

print(f"Total tails drawn: {count}")


#foxbody
fillcolor("white")
begin_fill()

goto(-20,-20)
pendown()
goto(-40,-40)
goto(-60,-120)
goto(-40,-140)
goto(40,-140)
goto(60,-120)
goto(40,-40)
goto(20,-20)
goto(-20,-20)
end_fill()
penup()

# foxhead

goto(0,-40)
pendown()

fillcolor("white")
begin_fill()

goto(-40,0)
goto(-40,80)
goto(0,40)
goto(0,40)
goto(40,80)
goto(40,0)
goto(0,-40)

end_fill()
penup()

#foxnose

goto(-8,-20)
pendown()

fillcolor("black")
begin_fill()

goto(8,-20)
goto(0,-30)
goto(-8,-20)
end_fill()
penup()

# foxeyes

goto(-10,-10)
pendown()
goto(-22,5)
penup()

goto(10, -10)
pendown()
goto(22,5)
penup()

#foxstirn

# change the color of the lines

if count == 9:
    fillcolor('#A61A00')

elif count > 4:
    fillcolor('#E3721B')

elif count == 0:
    fillcolor('#D4D2D2')

else:
    fillcolor('#FADBAC')

begin_fill()
goto(0, 3)
pendown()
goto(-10, 19)
goto(0, 38)
goto(10, 19)
goto(0, 3)
end_fill()
penup()

fillcolor('white')
begin_fill()
goto(0, 10)
pendown()
goto(-5, 19)
goto(0, 30)
goto(5, 19)
goto(0, 10)
end_fill()
penup()


# move to the center
penup()
goto(0,0)
pendown()

#snowflakes
num_snowflakes = 100

for s in range(num_snowflakes):
    # Fox is roughly at (0, 0), so we spread them from -400 to 400
    x = random.randint(-490, 490)
    y = random.randint(-390, 390)

    # Avoid drawing snowflakes directly on the fox's face
    if -280 < x < 280 and -150 < y < 200:
        continue

    penup()
    goto(x, y)
    pendown()
    pencolor("lightgrey")

    # actually drawing snowflakes
    snowflake_size = random.randint(5, 15)
    for arm in range(6):
        forward(snowflake_size)
        backward(snowflake_size)
        right(60)

# Reset color
pencolor("black")

# quite with click
exitonclick()