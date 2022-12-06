#Project 2: drawing the United States Flag
#By Jennifer Dopkins and Matthew Langendorfer
#import the time and turtle module
import turtle
import time

# create a screen
scr = turtle.getscreen()
scr.title("United States of America Flag")
scr.bgcolor("white")

#Set the turtle object and speed of the turtle
t = turtle.Turtle()
t.speed(50)
t.penup()


# starting points of the flag
x1 = -250
y1 = 120

#function to draw flag
def draw_flag():
    A = 250
    B = 475
    height = int(A)
    width = int(B)
    draw_flag()

# red and white stripes (total 13 stripes in flag)
stripe_ht = 250/13
stripe_wdt = 475
#star size
star_size = 12

    
#function to draw rectangle 
def draw_rectangle(x, y, height, length, color):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()

#function to draw stars
def draw_star(x, y, color, size):
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range(0,5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()
        

# function to create stripes of flag
def draw_stripes():
    x = x1
    y = y1
    # draw 6 red and 7 white strips
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_rectangle(x, y, stripe_ht, stripe_wdt, color)
            # decrease value of y by stripe_height
            y = y - stripe_ht

    # create last red stripe
    draw_rectangle(x, y, stripe_ht, stripe_wdt, 'red')
    y = y - stripe_ht


# function to create navy color square
def draw_square():
    square_ht = (7/13) * 250
    square_wdt = (0.76) * 250
    draw_rectangle(x1, y1, square_ht, square_wdt, 'navy')

#defining a function for drawing a 6 row star
def stars1():
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 112
    # create 5 rows of stars
    for row in range(0,5) :
        x = -234
        # create 6 stars in each row
        for star in range (0,6) :
            draw_star(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines


def stars_five():
    dist_of_stars = 30
    dist_bet_lines = stripe_ht + 6
    y = 100
    # create 4 rows of stars
    for row in range(0,4) :
        x = -217
        # create 5 stars in each row
        for star in range (0,5) :
            draw_star(x, y, 'white', star_size)
            x = x + dist_of_stars
        y = y - dist_bet_lines
        
#main function        
def main():
   time.sleep(2)
   draw_stripes()
   draw_square()
   stars1()
   stars_five()
   t.hideturtle()
   scr.mainloop()

if __name__ == "__main__":
    main()
    
    