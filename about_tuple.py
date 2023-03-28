numbers = (1, 2, 3, 4, 5, 6)
print(type(numbers))
# تاپل دقیقا شبیه به لیست است اما:
# امکان اضافه کردن و حذف کردن و تغییر دادن در تاپل وجود ندارد
numbers[0] = 2000  # خطا


numbers = [1, 2, 3, 4, 5, 6]
print(type(numbers))
numbers.append(60)
numbers[0] = 1000
print(numbers)


# جلسه بعدی در مورد دیکشنری + ترتل
