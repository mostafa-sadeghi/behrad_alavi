i = 0
t = 0

while i < 3:
    n = int(input('enter a number: '))
    if n % 2 != 0:
        t = t + n
    i = i + 1

print(t)

for i in range(3):
    n = int(input('enter a number: '))
    if n % 2 != 0:
        t = t + n
print(t)

# exercise : با کمک حلقه فور و وایل برنامه ای بنویسید که اعداد موجود در لیست زیر را با هم جمع نماید
numbers = [1,2,3,4,5,6]