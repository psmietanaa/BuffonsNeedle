# Piotr Smietana
# CS1210
# Homework 8
# A Python program that approximates pi using Buffon's Needle.

import random
import math
import turtle

def getTurtle(d):
    # Set up turtle using monteDraw.py from lecture
    turtle.setworldcoordinates(-12, -12, 12, 12)
    turtle.setup()
    t = turtle.Turtle()
    wn = t.getscreen()
    wn.title("Buffon's Needle")
    t.hideturtle()
    # Limit the number of screen updates
    # Draw every 10th update, but never fewer than 10
    tr = max(10, d/10) 
    wn.tracer(tr,0)
    return t

def drawBoard(t):
    # Draw thin square
    t.up()
    t.goto(-11,-11)
    t.down()
    t.pensize(3)
    t.goto(-11,11)
    t.goto(11,11)
    t.goto(11,-11)
    t.goto(-11,-11)
    t.up()
    # Draw orange lines
    t.up()
    x = -11
    y = -9
    t.goto(x,y)
    t.pensize(1)
    t.color("orange")
    t.down()
    # Using for loop to draw orange lines
    for I in range(10):
        if I % 2 == 0:
            t.down()
            x = x + 22
            t.goto(x,y)
            t.up()
            y = y + 2
            t.goto(x,y)
        else:
            t.down()
            x = x - 22
            t.goto(x,y)
            t.up()
            y = y + 2
            t.goto(x,y)

def buffonSimulation(d,t):
    # Setting up variables
    hits = 0
    # Do math
    theta = random.randint(0,180)
    yCenter = random.uniform(-10,10)
    yBottom = yCenter - (math.sin(math.radians(theta)) / 2)
    yTop = yCenter + (math.sin(math.radians(theta)) / 2)
    xCenter = random.uniform(-10,10)
    xBottom = xCenter - (math.cos(math.radians(theta)) / 2)
    xTop = xCenter + (math.cos(math.radians(theta)) / 2) 
    # Simualtion    
    for I in range(0,d):
        # Check if needle's top or bottom crossed one of the 4 lines
        # If yes draw a red needle
        if yBottom % 2 == 1 or yTop % 2 == 1:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()
        elif yBottom < -9 and yTop > -9:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()       
        elif yBottom < -7 and yTop > -7:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()            
        elif yBottom < -5 and yTop > -5:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()       
        elif yBottom < -3 and yTop > -3:
            hits = hits + 1   
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()    
        elif yBottom < -1 and yTop > -1:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()            
        elif yBottom < 1 and yTop > 1:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()            
        elif yBottom < 3 and yTop > 3:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()            
        elif yBottom < 5 and yTop > 5:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()            
        elif yBottom < 7 and yTop > 7:
            hits = hits + 1
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()            
        elif yBottom < 9 and yTop > 9:
            hits = hits + 1   
            t.up()
            t.color("red")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()            
        else:
            # Draw blue needle
            t.up()
            t.color("blue")
            t.goto(xBottom,yBottom)
            t.down()
            t.goto(xTop,yTop)
            t.up()         
        # Pick new values for simulation
        theta = random.randint(0,180)
        yCenter = random.uniform(-10,10)
        yBottom = yCenter - (math.sin(math.radians(theta)) / 2)
        yTop = yCenter + (math.sin(math.radians(theta)) / 2)
        xCenter = random.uniform(-10,10)
        xBottom = xCenter - (math.cos(math.radians(theta)) / 2)
        xTop = xCenter + (math.cos(math.radians(theta)) / 2) 
    return hits

def printText(pi,d,t):
    t.up
    t.color("black")
    t.goto(0,-11)
    message = "n = " + str(d) + ". Approximation for pi = " + str(pi)
    t.write(message, False, 'center', ('Arial', 16, 'bold'))

def main(): 
    # Take input from user how many needles to drop
    d = int(turtle.textinput('Monty Carlo', 'How many needles do you want to drop: '))
    # Set up turtle
    t = getTurtle(d)
    # Draw board
    drawBoard(t)
    # Simulation
    h = buffonSimulation(d,t)
    # Calculate pi
    if h == 0 :
        pi = 0
    else:
        pi = d / h
    # Print text
    printText(pi,d,t)
    # Turtle done
    turtle.done()
    
main()