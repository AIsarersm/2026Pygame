import time  # 內置模塊
import math  # 內置模塊
import random  # 內置模塊
import pygame  # 導入第三方模塊
import pythonModule  # 導入本地模塊


def greet():
    print("    Hello, Python!")


def add(a, b):
    """計算兩個數的和"""
    return a + b


def power(base, exponent=2):
    """計算base的exponent次方，默認是平方"""
    return base ** exponent


if __name__ == '__main__':  # 程序一般入口
    # 程序會從這里可以運行
    # 調用power函數
    the_base = 5
    power_num = 3
    result_1 = power(the_base, power_num)
    print(f"5^3的結果是{result_1}")

    # 使用內置模塊的功能
    print(f"現在的時間是{time.time()}")

    # 使用本地模塊定義的功能
    pythonModule.my_hello()



