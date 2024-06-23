# 9.1创建⼀个名为 Restaurant 的类，为其__init__() ⽅法设置两个属性：restaurant_name 和cuisine_type。
# 创建⼀个名为 describe_restaurant() 的⽅法和⼀个名为 open_restaurant() 的⽅法，
# 其中前者打印前述两项信息，⽽后者打印⼀条消息，指出餐馆正在营业。
# 根据这个类创建⼀个名为 restaurant 的实例，分别打印其两个属性，再调⽤前述两个⽅法。
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name}')
        print(f'Cuisine_type is {self.cuisine_type}')

    def open_restaurant(self):
        print('餐馆正在营业。')


restaurant = Restaurant('湖锦酒楼', '湖北菜')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9.2根据为练习 9.1 编写的类创建三个实例，并对每个实例调⽤ describe_restaurant() ⽅法。
restaurant1 = Restaurant('湖锦酒楼', '湖北菜')
restaurant2 = Restaurant('潮汕牛肉火锅', '广东火锅')
restaurant3 = Restaurant('西湖酒楼', '淮扬菜')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9.3创建⼀个名为 User 的类，其中包含属性first_name 和 last_name，还有⽤户简介中通常会有的其他⼏个属性。
# 在类 User 中定义⼀个名为 describe_user() 的⽅法，⽤于打印⽤户信息摘要。
# 再定义⼀个名为 greet_user() 的⽅法，⽤于向⽤户发出个性化的问候。
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f'用户的姓名是{self.first_name} {self.last_name}')
    def greet_user(self):
        print(f'hello,{self.first_name} {self.last_name}!')
user = User('寇', '力维')
user.greet_user()

# 9.4在为练习 9.1 编写的程序中，添加⼀个名为number_served 的属性，并将其默认值设置为 0。
# 添加⼀个名为 increment_number_served() 的⽅法，⽤来让就餐⼈数递增。
#调⽤这个⽅法并向它传递⼀个这样的值：你认为这家餐馆每天可能接待的就餐⼈数。
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name}')
        print(f'Cuisine_type is {self.cuisine_type}')

    def open_restaurant(self):
        print('餐馆正在营业。')
    # 添加⼀个名为 set_number_served() 的⽅法，⽤来设置就餐⼈数。调⽤这个⽅法并向它传递新的就餐⼈数，然后再次打印这个值。
    def set_number_served(self, number_served):
        self.number_served = number_served
        return self.number_served
    #添加⼀个名为 increment_number_served() 的⽅法，⽤来让就餐⼈数递增。
    #调⽤这个⽅法并向它传递⼀个这样的值：你认为这家餐馆每天可能接待的就餐⼈数。
    def increment_number_served(self, number):
        self.number_served += number

# 根据这个类创建⼀个名为 restaurant 的实例。打印有多少⼈在这家餐馆就餐过，然后修改这个值并再次打印。
restaurant = Restaurant('湖锦酒楼', '湖北菜')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
print(restaurant.set_number_served(20))
restaurant.increment_number_served(5)
print(restaurant.number_served)

# 在为练习 9.3 编写的 User 类中，添加⼀个名为 login_attempts 的属性。
# 编写⼀个名为increment_login_attempts() 的⽅法，⽤来将属性login_attempts 的值加 1。
# 再编写⼀个名为reset_login_attempts() 的⽅法，⽤来将属性login_attempts 的值重置为 0。
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print(f'用户的姓名是{self.first_name} {self.last_name}')
    def greet_user(self):
        print(f'hello,{self.first_name} {self.last_name}!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
# 根据 User 类创建⼀个实例，再调⽤increment_login_attempts() ⽅法多次。
# 打印属性login_attempts 的值，确认它正确地递增了。
# 然后，调⽤⽅法reset_login_attempts()，并再次打印属性 login_attempts的值，确认它被重置为 0
user = User('x', 'sj')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

# 冰激凌⼩店是⼀种特殊的餐馆。编写⼀个名为IceCreamStand 的类，让它继承你为练习 9.1 或练习 9.4 编写的Restaurant 类。
# 这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。添加⼀个名为 flavors 的属性，⽤于存储⼀个由各种⼝味的冰激凌组成的列表。
# 编写⼀个显⽰这些冰激凌⼝味的⽅法。创建⼀个 IceCreamStand 实例，并调⽤这个⽅法。
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name}')
        print(f'Cuisine_type is {self.cuisine_type}')

    def open_restaurant(self):
        print('餐馆正在营业。')
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['1', '2', '3']
    def ice_flavors(self):
        print(f'该餐馆有{self.flavors}口味的冰激凌')
icecream = IceCreamStand('DQ', '冰激凌')
icecream.ice_flavors()
