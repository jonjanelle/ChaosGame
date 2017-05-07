'''
Chaos game

1) place three starting posts
2) stamp turtle at random position
3) choose starting post at random, move to midpoint of current position and post, and stamp
4) repeat step 3 a few thousand times                                                              

Note: Stamp by moving forward 1 unit.
'''

import turtle, random

def main():
    window = turtle.Screen()
    
    pen = turtle.Turtle()
    pen.tracer(-1,delay=None)
    pen.color("black")
    pen.hideturtle()
    pen.shape("circle")
    pen.pensize(1)
    pen.speed(0)
    pen.penup()
    
    p1 = (-150,0)
    pen.setpos(p1[0],p1[1])
    pen.stamp()
    
    p2 = (150,0)
    pen.setpos(p2[0],p2[1])
    pen.stamp()
    
    p3 = (0, 150)
    pen.setpos(p3[0],p3[1])
    pen.stamp()

    
    newX = 0
    newY = 0
    
    for i in range(10000):
        pen.penup()
        #get current pen position
        px = pen.position()[0]
        py = pen.position()[1]
        
        #pick one of the three random points
        point = random.randint(1,3)
        
        #calculate new destination to place a point
        if point == 1:
            newX = (px + p1[0])/2
            newY = (py + p1[1])/2
        elif point == 2:
            newX = (px + p2[0])/2
            newY = (py + p2[1])/2
        elif point == 3:
            newX = (px + p3[0])/2
            newY = (py + p3[1])/2
        
        
        pen.setpos(newX,newY)
        pen.pendown()
        pen.forward(1)
        
    
    window.exitonclick()
    window.mainloop()
    


if __name__ == "__main__":
    main()





