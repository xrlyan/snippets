#!/usr/bin/env python
# coding=utf-8
# 测试utf-8编码
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def fibonacci():
    a = b = 1
    # yield则像是generator函数的返回结果
    yield a
    yield b
    while True:
        a, b = b, a+b
        # yield唯一所做的另一件事就是保存一个generator函数的状态，
        # generator就是一个特殊类型的迭代器（iterator）
        yield b

num = 0
fib = fibonacci()
while num < 100:
    # 和迭代器相似，我们可以通过使用next()来从generator中获取下一个值，也可以通过隐式地调用next()来忽略一些值
    num = next(fib)
    print num,
    # 1 1 2 3 5 8 13 21 34 55 89 144
