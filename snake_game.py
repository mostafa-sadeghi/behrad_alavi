from turtle import Turtle, Screen
import time
from random import randint


def make_turtle_object(color, shape):
    turtle_object = Turtle()
    turtle_object.speed("fastest")
    turtle_object.color(color)
    turtle_object.shape(shape)
    turtle_object.penup()
    return turtle_object


def change_food_position():
    food_x_pos = randint(-250, 250)
    food_y_pos = randint(-250, 250)
    food.setpos(food_x_pos, food_y_pos)


def go_up():
    if head.dir != "down":
        head.dir = "up"


def go_down():
    if head.dir != "up":
        head.dir = "down"


def go_left():
    if head.dir != "right":
        head.dir = "left"


def go_right():
    if head.dir != "left":
        head.dir = "right"


def move():
    if head.dir == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.dir == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.dir == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.dir == "right":
        x = head.xcor()
        head.setx(x + 20)


window = Screen()
window.title("Snake game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)
head = make_turtle_object("black", "square")
head.dir = "none"


food = make_turtle_object("red", "circle")
change_food_position()


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")

snake_body = []
score = 0

score_pen = make_turtle_object("grey", "square")
score_pen.hideturtle()
score_pen.setposition(0,260)
score_pen.write(f'Score: {score}', align="center", font=("Arial", 24))
while True:
    window.update()
    if head.distance(food) < 20:
        change_food_position()
        tail = make_turtle_object("grey", "square")
        snake_body.append(tail)

    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()

        snake_body[i].goto(x, y)
    if len(snake_body) > 0:
        xhead = head.xcor()
        yhead = head.ycor()
        snake_body[0].goto(xhead, yhead)

    if head.xcor() > 290: # todo اضافه کردن خروج از سایر جهت ها
        head.goto(0,0)
        head.dir = "none"
        for body in snake_body:
            body.hideturtle()
        snake_body.clear()
        # TODO قرار دادن کدهای ریست در یک تابع
    # TODO اضافه کردن امتیاز
    move()
    time.sleep(0.1)
