# Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

# Python 支持各种数据结构的推导式：
# 列表(list)推导式
# 字典(dict)推导式
# 集合(set)推导式
# 元组(tuple)推导式

# 列表(list)推导式
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 字典(dict)推导式
list_demo = ['Google', 'Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
new_dict = {key: len(key) for key in list_demo}
print(new_dict)

# 集合推导式
set_new = {i**2 for i in (1, 2, 3)}
print(set_new)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 元组推导式（生成器表达式）
a = (x for x in range(1, 10))
print(tuple(a))       # 使用 tuple() 函数，可以直接将生成器对象转换成元组

