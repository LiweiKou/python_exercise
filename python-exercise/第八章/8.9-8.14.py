# 8.9创建⼀个列表，其中包含⼀系列简短的⽂本消息。将这个列表传递给⼀个名为 show_messages() 的函数，
# 这个函数会打印列表中的每条⽂本消息。
messages = ['klw', 'hust', 'xiaomi']
def show_messages(list_name):
    for value in list_name:
        print(value)
show_messages(messages)

# 8.10在为练习 8.9 编写的程序中，编写⼀个名为send_messages() 的函数，将每条消息都打印出来并移到⼀个名为sent_messages 的列表中。
# 调⽤ send_messages() 函数，再将两个列表都打印出来，确认把消息移到了正确的列表中。
sent_messages = []
def send_messages(list_name):
    while list_name:
        message = list_name.pop()
        print(f'{message}被移到sent_messages中')
        sent_messages.append(message)
send_messages(messages)
print(sent_messages)

# 8.11修改为练习 8.10 编写的程序，在调⽤函数send_messages() 时，向它传递消息列表的副本。
# 调⽤send_messages() 函数后，将两个列表都打印出来，确认原始列表保留了所有的消息
send_messages(messages[:])
print(sent_messages)
print(messages)

# 8.12编写⼀个函数，它接受顾客要在三明治中添加的⼀系列⾷材。这个函数只有⼀个形参（它收集函数调⽤中提供的所有⾷材），
# 并打印⼀条消息，对顾客点的三明治进⾏概述。调⽤这个函数三次，每次都提供不同数量的实参。
def add_food(*food_types):
    for food_type in food_types:
        print(f'顾客点的三明治需要{food_type}')
add_food('a', 'b', 'c')
add_food('b')

# 8.13复制前⾯的程序 user_profile.py，在其中调⽤build_profile() 来创建有关你的简介。
# 在调⽤这个函数时，指定你的名和姓，以及三个⽤来描述你的键值对。
def build_profile(first, last, **user_info):
   user_info['first_name'] = first
   user_info['last_name'] = last
   return user_info
user_profile = build_profile('x', 'sj',
location='china',
field='math')
print(user_profile)

# 8.14编写⼀个函数，将⼀辆汽⻋的信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 在调⽤这个函数时，提供必不可少的信息，以及两个名值对，如颜⾊和选装配件。这个函数必须能够像下⾯这样调⽤：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
def make_car(manufacturer, model, **car_messages):
    car_messages['manufacturer_name'] = manufacturer
    car_messages['model_name'] = model
    return car_messages
car_message = make_car('一汽', 'audi', color='black', tow_package=True)
print(car_message)