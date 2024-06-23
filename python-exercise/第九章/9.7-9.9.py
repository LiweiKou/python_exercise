# 9.7管理员是⼀种特殊的⽤户。编写⼀个名为 Admin的类，让它继承你为练习 9.3 或练习 9.5 完成编写的 User 类。
# 添加⼀个名为 privileges 的属性，⽤来存储⼀个由字符串（如 "can addpost"、"can delete post"、"can ban user" 等）组成的列表。
# 编写⼀个名为 show_privileges() 的⽅法，显⽰管理员的权限。创建⼀个 Admin 实例，并调⽤这个⽅法。
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f'用户的姓名是{self.first_name} {self.last_name}')
    def greet_user(self):
        print(f'hello,{self.first_name} {self.last_name}!')

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can addpost", "can delete post", "can ban user"]
    def show_privileges(self):
        for privilege in self.privileges:
            print(f'{self.first_name}{self.last_name}有{privilege}的权利')
user = Admin('k', 'lw')
user.show_privileges()

# 9.8编写⼀个名为 Privileges 的类，它只有⼀个属性privileges，其中存储了练习 9.7 所述的字符串列表。
# 将⽅法show_privileges() 移到这个类中。在 Admin 类中，将⼀个Privileges 实例⽤作其属性。
# 创建⼀个 Admin 实例，并使⽤⽅法show_privileges() 来显⽰权限。
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f'用户的姓名是{self.first_name} {self.last_name}')
    def greet_user(self):
        print(f'hello,{self.first_name} {self.last_name}!')

class Privileges:
    def __init__(self):
        self.privileges = ["can addpost", "can delete post", "can ban user"]
    def show_privileges(self):
        for privilege in self.privileges:
            print(f'有{privilege}的权限')

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

user = Admin('k', 'lw')
user.privileges.show_privileges()

# 9.9在本节最后⼀个 electric_car.py 版本中，给Battery 类添加⼀个名为 upgrade_battery() 的⽅法。
# 这个⽅法检查电池容量，如果电池容量不是 65，就设置为 65。
# 创建⼀辆电池容量为默认值的电动汽⻋，调⽤⽅法 get_range()，然后对电池进⾏升级，并再次调⽤ get_range()。
# 你将看到这辆汽⻋的续航⾥程增加了
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
my_leaf = ElectricCar('比亚迪', '仰望U9', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()