# 数据类型会自己推导，不需要像C++那样声明
# python中有6种数据类型 Number数字 String字符串 List列表 Tuple元组 Set集合 Directionary字典

# ------------------不可变数据------------------
# 1.Number Python3 支持 int、float、bool、complex（复数）

int_a = 10
print(int_a, type(int_a))

float_a = 10.2
print(float_a, type(float_a))

bool_a = False
print(bool_a, type(bool_a))


# 输入
a = input("按下 enter 键退出，其他任意键显示...\n")
print(a)
