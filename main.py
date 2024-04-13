# Python: Declaring a Variable without assigning it a Value

my_variable = None

print(my_variable) # 👉️ None

print(type(my_variable)) # 👉️ <class 'NoneType'>

my_variable = None

if my_variable is None:
    print('It is None')
else:
    print('It is NOT None')