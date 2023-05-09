numbers = []
for i in range(4):
    new_number = int(input('enter a number: '))
    numbers.append(new_number)
print()
x = int(input('enter a number: '))
# print(numbers.count(x))
n = 0
for c in numbers:
    if c == x:
        n += 1

print(n)

# ex1  :  
'''
'123456789'
فرض کنید رشته بالا را داریم
مجموع اعداد را از رشته بالا محاسبه و نمایش دهید
مجموع اعداد زوج را از رشته بالا محاسبه و نمایش دهید

'''