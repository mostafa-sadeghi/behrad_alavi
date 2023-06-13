from turtle import Screen, Turtle
from time import sleep
from random import randrange

main_surface = Screen()
main_surface.bgcolor('blue')
main_surface.setup(width=600, height=600)
main_surface.title('Snake Game')
main_surface.tracer(0)
# TODO  برای درست کردن صفحه نیز یک تابع ایجاد کنید
def make_turtle(turtle_shape, turtle_color):
    my_turtle = Turtle()
    my_turtle.shape(turtle_shape)
    my_turtle.color(turtle_color)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle

def move():
    if snake_head.direction == "up":
        yposition = snake_head.ycor()
        yposition += 20  # yposition = yposition + 20
        snake_head.sety(yposition)
    if snake_head.direction == "down":
        yposition = snake_head.ycor()
        yposition -= 20  # yposition = yposition + 20
        snake_head.sety(yposition)
    if snake_head.direction == "right":
        xposition = snake_head.xcor()
        xposition += 20  # yposition = yposition + 20
        snake_head.setx(xposition)
    if snake_head.direction == "left":
        xposition = snake_head.xcor()
        xposition -= 20  # yposition = yposition + 20
        snake_head.setx(xposition)
def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"
def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"
def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"
def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def change_food_position():
    x = randrange(-270, 270)
    y = randrange(-270, 270)
    food.goto(x,y)

snake_head = make_turtle("square", "black")
snake_head.goto(100, 100)
snake_head.direction = "stop"

food = make_turtle("circle", "red")
change_food_position()

main_surface.listen()
main_surface.onkey(go_up,"Up")
main_surface.onkey(go_down,"Down")
main_surface.onkey(go_left,"Left")
main_surface.onkey(go_right,"Right")


snake_body = []
running = True
while running:
    main_surface.update()

    if snake_head.distance(food) < 20:
        change_food_position()
        new_tail = make_turtle("square", "grey")
        snake_body.append(new_tail)

    for i in range(len(snake_body) - 1, 0, -1):
        prevx = snake_body[i-1].xcor()
        prevy = snake_body[i-1].ycor()
        snake_body[i].goto(prevx, prevy)

    if len(snake_body) >0 :
        head_x = snake_head.xcor()
        head_y = snake_head.ycor()
        snake_body[0].goto(head_x, head_y)

    move()
    sleep(0.2)
