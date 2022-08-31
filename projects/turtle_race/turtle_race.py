import turtle
import time
import random

def canvas_setup(): 
    canvas = turtle.Screen()
    canvas.title = 'Turtle Races'
    WIDTH, HEIGHT = 500, 500
    canvas.screensize(WIDTH, HEIGHT)

def get_number_of_turtles():
    greeting = input('How many turtles are racing today? ')
canvas_setup()
time.sleep(5)
