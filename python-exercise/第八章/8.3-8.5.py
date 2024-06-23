# 8.3编写⼀个名为 make_shirt() 的函数，它接受⼀个尺码以及要印到 T 恤上的字样。这个函数应该打印⼀个句⼦，简要地说明 T 恤的尺码和字样。
def make_shirt(size, words):
    print(f'T恤的尺码为：{size}，T恤上的文字是：{words}')
# 先使⽤位置实参调⽤这个函数来制作⼀件 T 恤，再使⽤关键字实参来调⽤这个函数。
make_shirt('L', 'I ll be the best')

# 8.4修改 make_shirt() 函数，使其在默认情况下制作⼀件印有“I love Python”字样的⼤号 T 恤。
# 调⽤这个函数分别制作⼀件印有默认字样的⼤号 T 恤，⼀件印有默认字样的中号 T 恤，以及⼀件印有其他字样的 T 恤（尺码⽆关紧要）。
def make_shirt(size, words='I love Python'):
    print(f'T恤的尺码为：{size}，T恤上的文字是：{words}')
make_shirt('l')
make_shirt('m')
make_shirt('s', 'valorant')

# 8.5编写⼀个名为 describe_city() 的函数，它接受⼀座城市的名字以及该城市所属的国家。这个函数应该打印⼀个像下⾯这样简单的句⼦。
# Reykjavik is in Iceland.给⽤于存储国家的形参指定默认值。为三座不同的城市调⽤这个函数，其中⾄少有⼀座城市不属于默认的国家
def describe_city(name, country='china'):
    print(f'{name} is in {country}')
describe_city('wuhan')