# 8.6编写⼀个名为 city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回⼀个格式类似于下⾯的字符串：
# "Santiago, Chile"
def city_country(name, country):
    city = f'{name}, {country}'
    return city.title()
# ⾄少使⽤三个城市⾄国家对调⽤这个函数，并打印它返回的值。
print(city_country('wuhan', 'china'))

# 8.7编写⼀个名为 make_album() 的函数，它创建⼀个描述⾳乐专辑的字典。
# 这个函数应接受歌⼿名和专辑名，并返回⼀个包含这两项信息的字典。
# 使⽤这个函数创建三个表⽰不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
def make_album(singer_name, album_name):
    album = {'singer_name': singer_name, 'album_name': album_name}
    return album
print(make_album('Jay', '睡前故事'))
print(make_album('Eminem', 'Houdini'))
print(make_album('Kdot', 'Not like us'))
'''
给 make_album() 函数添加⼀个默认值为 None 的可选形参，以便存
储专辑包含的歌曲数。如果调⽤这个函数时指定了歌曲数，就将这个
值添加到表⽰专辑的字典中。调⽤这个函数，并⾄少在⼀次调⽤中指
定专辑包含的歌曲数。
'''
def make_album(singer_name, album_name, song_number=None):
    if song_number:
        album = {'singer_name': singer_name, 'album_name': album_name, 'song_number': song_number}
    else:
        album = {'singer_name': singer_name, 'album_name': album_name}
    return album
print(make_album('Eminem', 'Houdini', 5))
print(make_album('Eminem', 'Houdini'))

# 8.8在为练习 8.7 编写的程序中，编写⼀个 while循环，让⽤户输⼊歌⼿名和专辑名。
# 获取这些信息后，使⽤它们来调⽤ make_album() 函数并将创建的字典打印出来。在这个 while 循环中，务必提供退出途径。
def make_album(singer_name, album_name, song_number=None):
    if song_number:
        album = {'singer_name': singer_name, 'album_name': album_name, 'song_number': song_number}
    else:
        album = {'singer_name': singer_name, 'album_name': album_name}
    return album
while True:
    print("\nPlease tell me your favorite album:")
    print("(enter 'q' at any time to quit)")
    s_name = input("who is the album singer:")
    if s_name == 'q':
        break
    a_name = input("what is the album name?")
    if a_name == 'q':
        break
    print(make_album(s_name, a_name))
