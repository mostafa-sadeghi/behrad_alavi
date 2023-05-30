# all_persons = []
# for i in range(2):
#     student_name = input("Enter a name: ")
#     student_dad_name = input("Enter dad`s name: ")
#     student_national_code = input("Enter national code: ")

#     person = {}
#     person['name'] = student_name
#     person['dad'] = student_dad_name
#     person['code'] = student_national_code
#     all_persons.append(person)


# print(all_persons)
# print(all_persons[0])
# print(all_persons[1])
# print(all_persons[1]['name'])


# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)


# numbers = [2, 5, 8, 9, 22, 456]
# total = 0
# for n in numbers:
#     total += n
# print(total)


# exrcise 1: 
'''
برنامه ای بنویسید که تعداد اعداد زوج موجود در لیست زیر را نمایش دهد
my_list = [4,3,67,89,44,23,456,2345,2000]
'''
# my_list = [4,3,67,89,44,23,456,2345,2000]
# count = 0

# for number in my_list:
#     if number % 2 == 0:
#         count += 1

# print("number of even is :", count)


# exercise 2:
'''
my_list = [4,3,67,89,44,23,456,2345,2000]
برنامه ای بنویسید که یک عدد از ورودی دریافت نماید و در لیست بالا جستجو کند
در صورتی که عدد در لیست وجود داشته باشد، شماره خانه یا ایندکس آن عدد را نمایش دهد
در غیر اینصورت "nothing" را نمایش دهد
'''
# my_list = [4,3,67,89,44,23,456,2345,2000]

# find = "no"
# number = int(input('Enter a number: '))
# for i in range(len(my_list)):
#     if my_list[i] == number:
#         print(i)
#         find = "yes"
# if find == "no":
#     print("nothing")



count = 0

# for i in range(3):
#     new_number = int(input('Enter a number: '))
#     if new_number == 1000:
#         count += 1

# print(f'number 1000 repeated {count} times.')

# i = 0
# while i < 3:
#     new_number = int(input('Enter a number: '))
#     if new_number == 1000:
#         count += 1
#     i += 1

# print(f'number 1000 repeated {count} times.')





# for i in range(3):
#     print("hi")

# i = 0
# while i < 3:
#     print("hi")
#     i += 1
# exercise 3:
'''
برنامه بالا یعنی برنامه پیدا کردن تعداد تکرار عدد 1000 را با استفاده از حلقه وایل بنویسید
'''