import turtle
from random import randint

myPen = turtle.Turtle()
screen = turtle.Screen()
screen.tracer(0) 
myPen.speed(0)
myPen.hideturtle()

def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)    		  
    myPen.write(message, align="left", font=FONT)

def box(intDim):
    myPen.begin_fill()
    for _ in range(4):
        myPen.forward(intDim)
        myPen.left(90)
    myPen.end_fill()
    myPen.setheading(0)

palette = ["#FFFFFF", "#000000", "#00ff00", "#ff00ff", "#AAAAAA"]
maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def drawMaze(maze):
    boxSize = 15	
    myPen.penup()
    myPen.goto(-130, 130)
    myPen.setheading(0)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            myPen.color(palette[maze[i][j]])
            box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()	
        myPen.setheading(270) 
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180) 
        myPen.forward(boxSize * len(maze[i]))
        myPen.setheading(0)
        myPen.pendown()

def exploreMaze(maze, row, col):
    if maze[row][col] == 2:
        return True
    elif maze[row][col] == 0:
        maze[row][col] = 3
        myPen.clear()
        drawMaze(maze) 
        screen.update()        
        if row < len(maze) - 1:
            
            if exploreMaze(maze, row + 1, col):
                return True
        if row > 0:
            
            if exploreMaze(maze, row - 1, col):
                return True
        if col < len(maze[row]) - 1:
            
            if exploreMaze(maze, row, col + 1):
                return True
        if col > 0:
            
            if exploreMaze(maze, row, col - 1):
                return True
        
        maze[row][col] = 4    
        myPen.clear()
        drawMaze(maze) 
        screen.update()            
        print("Tracking")
  
drawMaze(maze) 
screen.update()

solved = exploreMaze(maze, 0, 1)
if solved:
    print("Maze Solved")
    text("Maze Solved", -100, -150, 20)
else:  
    print("Cannot Solve Maze")
    text("Cannot Solve Maze", -130, -150, 20)

screen.update()