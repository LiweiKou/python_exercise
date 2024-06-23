# 10.1在⽂本编辑器中新建⼀个⽂件，写⼏句话来总结⼀下你⾄此学到的 Python 知识，其中每⼀⾏都以“In Python you can”打头。
# 将这个⽂件命名为 learning_python.txt，并存储到为完成本章练习⽽编写的程序所在的⽬录中。
# 编写⼀个程序，读取这个⽂件，并将你所写的内容打印两次：第⼀次打印时读取整个⽂件；
# 第⼆次打印时先将所有⾏都存储在⼀个列表中，再遍历列表中的各⾏。
from pathlib import Path
path = Path('小米学习/word.txt')
contents = path.read_text()
print(contents.rstrip())
for line in contents.splitlines():
    print(line)

# 10.2可使⽤ replace() ⽅法将字符串中的特定单词替换为另⼀个单词。
# 下⾯是⼀个简单的⽰例，演⽰了如何将句⼦中的 'dog' 替换为 'cat'：
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# 读取你刚创建的⽂件 learning_python.txt 中的每⼀⾏，将其中的 Python
# 都替换为另⼀门语⾔的名称，如 C。将修改后的各⾏都打印到屏幕上。
for line in contents.splitlines():
    print(line.lower().replace('python', 'C'))

# 10.4编写⼀个程序，提⽰⽤户输⼊其名字。在⽤户做出响应后，将其名字写⼊⽂件 guest.txt。
from pathlib import Path
name = input('请输入您的姓名：')
path = Path('小米学习/guest.txt')
path.write_text(name)

# 10.5编写⼀个 while 循环，提⽰⽤户输⼊其名字。收集⽤户输⼊的所有名字，将其写⼊ guest_book.txt，并确保这个⽂件中的每条记录都独占⼀⾏
from pathlib import Path
names = ''
while True:
    print('你可以随时输入q退出')
    name = input('请输入您的姓名：')
    if name == 'q':
        break
    else:
        names += (name + '\n')
path = Path('小米学习/guest_book.txt')
path.write_text(names)
