import turtle
import time
import random

def canvas_setup(): 
    canvas = turtle.Screen()
    canvas.title = 'Turtle Races'
    WIDTH, HEIGHT = 500, 500
    canvas.screensize(WIDTH, HEIGHT)

def get_number_of_turtles():
    while True: 
        greeting = input('How many turtles are racing today? (2 - 10)\n')
        if greeting.isdigit(): 
            num_of_turtles = int(greeting)
        else: 
            print("That's not a number. Try Again\n")
            continue
        
        if 2 <= num_of_turtles <= 10: 
            return num_of_turtles
        else: 
            print('Number should be between 2 and 10. Try Again\n')
            continue
#canvas_setup()
#time.sleep(5)
get_number_of_turtles()

