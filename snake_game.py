import turtle
import time

def go_up():
    if head.dir != "down":
        head.dir = "up"
def go_down():
    if head.dir != "up":
        head.dir = "down"
# TODO نوشتن تابع برای جهت چپ و راست


def move():
    if head.dir == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.dir == "down":
        y = head.ycor()
        head.sety(y - 20)

    # TODO اضافه کردن حرکت به سمت چپ و راست






window = turtle.Screen()
window.title("Snake game")
window.bgcolor("blue")
window.setup(width=600, height=600)

head = turtle.Turtle()
head.shape("square")
head.penup()
head.dir = "none"

window.listen()
window.onkey(go_up,"Up")
window.onkey(go_down,"Down")
# TODO اضافه کردن کلید های چپ و راست
#       Left   Right

while True:
    window.update()
    move()
    time.sleep(0.1)
