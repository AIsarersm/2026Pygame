# 數據類型
# 1. int - 整數
a1 = 1
a2 = 100
a3 = -120

# 2. float - 浮點數
b1 = 2.0
b2 = 3.14
b3 = -0.01

# 3. bool - 布爾/布林值
c1 = True
c2 = False

# 4. str - 字符串
d1 = "Hello"
d2 = "I am a person"
d3 = 'a'
# f-string
name = "Eric"
age = 18
d4 = f"My name is {name}. my age is {age}"
# 4.1 字符串格式化
hour = 1
min = 2
second = 3
print(f"4.1 原本的輸出 - time is {hour}:{min}:{second}")  # 普通輸出
print(f"4.1 格式化後的輸出 - time is {hour:02d}:{min:02d}:{second:02d}")  # 普通輸出

# 5. list - 列表
# 5.1 初初化:
b_list = []

# 5.2 添加元素(從元素最後加入)
b_list.append(1)
b_list.append(2.1)
b_list.append(True)
b_list.append("hello")
print(f"5.2: e1列表有以下內容:{b_list}")

# 5.3 通過索引查詢內容，從0開始
print(f"5.3: e1的第二個元素是:{b_list[1]}")
# 5.3.1 索引可以是負數，代表從尾開始數，-1代表最後一個元素
print(f"5.3.1: e1的最後一個元素是:{b_list[-1]}")

# 5.4 可變性
b_list[0] = 'a'
print(f"5.4: 新的e1列表有以下內容:{b_list}")

# 5.5 插入到指定位置:
b_list.insert(2, "qq")
print(f"5.5: insert後新的e1列表有以下內容:{b_list}")

# 5.6 刪除指定索引的元素:
b_list.pop(1)
print(f"5.6: pop(1)後新的e1列表有以下內容:{b_list}")
# 5.6.1 不加參數時，默認是刪除索引最後的元素
b_list.pop()
print(f"5.6.1: pop()後新的e1列表有以下內容:{b_list}")

# 5.7 刪除指定值的元素
b_list.remove("a")
print(f"5.7: remove()後新的e1列表有以下內容:{b_list}")

# 5.8 獲取列表元素個數
print(f"5.8: 現時的元素個數為:{len(b_list)}")

# 6 元組tuple()
c_tuple = (100, 200)

# 6.1 通過索引查詢內容，從0開始
print(f"6.1: c_tuple的第一位是{c_tuple[0]}")

# 6.2 解包賦值
x, y = c_tuple
print(f"x和y分別是{x},{y}")

# 7 if-elif-else條件判斷
# 7.1 單一條件判斷
score = 85
print("7.1 單一條件判斷:")
if score >= 90:
    print("    Perfect")
elif 80 <= score < 90:
    print("    Good")  # 输出：良好
elif 60 <= score < 80:
    print("    Pass")
else:
    print("    Fail")

# 7.2 多條件判斷
age = 25
is_vip = True
print("7.2 多條件判斷:")
if age >= 18 and is_vip:    # 需同时满足
    print("    VIP")
elif age >= 18 or is_vip:   # 满足其一
    print("    Basic")
else:
    print("    No")

# 8. for循環遍歷列表
# 8.1 直接遍歷
my_list = ["a", 1, 1.2, 7, "q"]
print("8.1 直接遍歷結果為: ")
for single_obj in my_list:  # 順著一個一個地遍歷
    print(f"    my_list中有{single_obj}")

# 8.2 索引遍歷:
num_of_list = len(my_list)
print("8.2 索引遍歷結果為: ")
for i in range(num_of_list):
    print(f"    my_list中第{i+1}個元素是{my_list[i]}")

# 9. while循環基本用法
# 9.1 循環體內變量更新使條件表達式結果為True
count = 0
print("9.1 循環體內變量更新使條件表達式結果為True:")
while count < 3:
    print(f"    當前計數值為{count}")
    count += 1

# 9.2 配合if語句和break退出循環
num = 0
print("9.2 配合if語句和break退出循環:")
while num < 5:
    if num == 2:
        break
    print(f"    當時數值為{num}")
    num += 1

# 10. 函數的定義和使用
# 10.1 定義無參數、無返回值的函數
print("10. 函數的定義和使用")
def greet():
    print("    Hello, Python!")

# 10.1 定義帶參數和返回值的函數
def add(a, b):
    """計算兩個數的和"""
    return a + b

# 10.2 定義帶參數(有默認值)和返回值的函數
def power(base, exponent=2):
    """計算base的exponent次方，默認是平方"""
    return base ** exponent

# 10.3 調用greet()函數
greet()
# 10.4 調用add()函數
num1 = 2
num2 = 3
result = add(num1, num2)
print(f"    num1+num2的結果是{result}")
# 10.5 調用power()函數
the_base = 5
power_num = 3
result_1 = power(the_base, power_num)
print(f"    5^3結果是{result_1}")


