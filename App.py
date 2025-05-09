import turtle

window = turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800 , height=600)
window.tracer(0) 


madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-375 , 0)


madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(370 , 0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.15
ball.dy = 0.15

score1 , score2 = 0 , 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Blue player : 0   Red player : 0" , align="center" , font=("Courier" , 24 , "normal"))

def madrab1Up():
    y = madrab1.ycor()
    y += 15 
    madrab1.sety(y)


def madrab1Down():
    y = madrab1.ycor()
    y -= 15 
    madrab1.sety(y)


def madrab2Up():
    y = madrab2.ycor()
    y += 15 
    madrab2.sety(y)


def madrab2Down():
    y = madrab2.ycor()
    y -= 15 
    madrab2.sety(y)


window.listen()
window.onkeypress(madrab1Up, "w")
window.onkeypress(madrab1Down, "s")


window.onkeypress(madrab2Up, "Up")
window.onkeypress(madrab2Down, "Down")


while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball .ycor() > 290:
        ball.sety(290)
        if  ball.dy == 0.15:
            ball.dy = -0.15
        else:
            ball.dy = 0.15


    if ball .ycor() < -290:
        ball.sety(-290)
        if  ball.dy == 0.15:
            ball.dy = -0.15
        else:
            ball.dy = 0.15
    


    if ball.xcor() > 390 :
        ball.goto(0,0)
        if  ball.dx == 0.15:
            ball.dx = -0.15
        else:
            ball.dx = 0.15
        score1 += 1
        score.clear()
        score.write(f"Blue player : {score1}   Red player : {score2}" , align="center" , font=("Courier" , 24 , "normal"))
    
    if ball.xcor() < -390 :
        ball.goto(0,0)
        if  ball.dx == 0.15:
            ball.dx = -0.15
        else:
            ball.dx = 0.15
        score2 += 1
        score.clear()
        score.write(f"Blue player : {score1}   Red player : {score2}" , align="center" , font=("Courier" , 24 , "normal"))

    


    if ball.xcor() < -365 and ball.xcor() > -375 and ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40:
        ball.setx(-365)
        if  ball.dx == 0.15:
            ball.dx = -0.15
        else:
            ball.dx = 0.15


     
    if ball.xcor() > 360 and ball.xcor() < 370 and ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40:
        ball.setx(360)
        if  ball.dx == 0.15:
            ball.dx = -0.15
        else:
            ball.dx = 0.15
    

