from tkinter import font
import turtle

window= turtle.Screen()
window.title("Pong by@LundriK")

window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#Score
score_a=0;
score_b=0

#paddleA
paddleA=turtle.Turtle()
paddleA.speed(1)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#paddleB
paddleB=turtle.Turtle()
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball_dx=2
ball_dy=-2

pen=turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0 ",align="center",font=("Courier",24,"normal"))



#Function
def up_paddle_A():
    y=paddleA.ycor()
    y+=20
    paddleA.sety(y)

def down_paddle_A():
    y=paddleA.ycor()
    y-=20
    paddleA.sety(y)

def up_paddle_B():
    y=paddleB.ycor()
    y+=20
    paddleB.sety(y)

def down_paddle_B():
    y=paddleB.ycor()
    y-=20
    paddleB.sety(y)

window.listen()
window.onkeypress(up_paddle_A,"w")
window.onkeypress(down_paddle_A,"s")
window.onkeypress(up_paddle_B,"Up")
window.onkeypress(down_paddle_B,"Down")



while True:
    window.update()

    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball_dy*=-1
    
    if ball.ycor()< -290:
        ball.sety(-290)
        ball_dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    
    if ball.xcor()< -390:
        ball.goto(0,0)
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    
    if (ball.xcor()> 340 and ball.xcor()<350) and (ball.ycor() < paddleB.ycor() +40 and ball.ycor() > paddleB.ycor() -40):
        ball.setx(340)
        ball_dx*=-1

    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor() < paddleA.ycor()+40 and ball.ycor() > paddleA.ycor() -40):
        ball.setx(340)
        ball_dx*=-1
