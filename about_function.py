# import turtle

# def draw(n):
#     for i in range(n):
#         pen.forward(100)
#         pen.left(360/n)


# stage = turtle.Screen()
# pen = turtle.Pen()

# draw(6)


# stage.exitonclick()


# یک تابع بنویسید که یک لیست به عنوان پارامتر بگیرد و
# اعداد زوج لیست را با هم جمع کند و نمایش دهد

def my_func(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total = total + n

    return total


numbers = [1,2,3,4,5,6,7,8,9]

result = my_func(numbers)
print(result)
