# string = '*' * 10
# string_2 = '@' * 10
# out = string + string_2
# print(out)

shopping_list = []
print(type(shopping_list))

shopping_list = ['egg', 'banana', 'apple', 1]
print("shopping list", shopping_list)


print("first item:", shopping_list[0])
print("last item:", shopping_list[-1])

shopping_list.append("potato")
shopping_list.append("mashroom")

print("shopping list after adding items", shopping_list)

product = input('enter a product name: ')
shopping_list.append(product)

print("list items after adding new input:", shopping_list)

# exercise : یک لیست بساز که 5 اسمی که از ورودی گرفتی را در آن اضافه کنی
# از لیست ساخته شده اولین اسم و آخرین اسم و همینطور دو اسم اول را پرینت نمائید.

# exercise :
# chars = ['a', 'b', 'c', 'd', 'e']

# از لیست بالا همه ی کاراکتر ها را کنار هم نمایش دهید یا پرینت کنید
# از لیست بالا همه ی کاراکتر ها را با یک فاصله کنار هم نمایش دهید یا پرینت کنید
