import turtle
import time
from random import choice

WIDTH, HEIGHT = 500, 500

def canvas_setup(): 
    canvas = turtle.Screen()
    canvas.title = 'Turtle Races'
    
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
        
def create_turtles(number): 
    COLORS = ['red', 'magenta', 'lime', 'blue', 'gold', 'brown', 'pink', 'black', 'honeydew', 'lavender']
    turtles = []
    spacingx = WIDTH // (number + 1)
    for i in range(number): 
        t = turtle.Turtle(shape='turtle')
        t.penup()
        t.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        t.pendown()
        t.left(90)
        t.color(choice(COLORS))
        turtles.append(i)
    #print (turtles)
    
canvas_setup()
create_turtles(get_number_of_turtles())
time.sleep(5)


