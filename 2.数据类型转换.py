# 数据类型转换分为隐式转换和显示转换
# 隐式转换-----自动完成
# 显示转换-----使用数据类型完成

# 隐式转换：低精度向高精度转换可以忽略信息直接转换。
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

# 显示类型转换
num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str:", type(num_str))

print(num_int + num_str)  # 这里会告知不能直接隐式类型转换，需要用显式类型转换

x = int(1)  # x 输出结果为 1
y = int(2.8)  # y 输出结果为 2
z = int("3")  # z 输出结果为 3

x = float(1)  # x 输出结果为 1.0
y = float(2.8)  # y 输出结果为 2.8
z = float("3")  # z 输出结果为 3.0
w = float("4.2")  # w 输出结果为 4.2

x = str("s1")  # x 输出结果为 's1'
y = str(2)  # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

num_int = 123
num_str = "456"

print("num_int 数据类型为:", type(num_int))
print("类型转换前，num_str 数据类型为:", type(num_str))

num_str = int(num_str)  # 强制转换为整型
print("类型转换后，num_str 数据类型为:", type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:", num_sum)
print("sum 数据类型为:", type(num_sum))
