
### Introduction 简介
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. 
Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in ***fewer*** lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale.[28]

Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.[29]


### 工具

idle
pycharm
pip
http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows

### list 有序列表
	python list 可以用来进行数组，链表，队列，堆栈操作
	.append() push_back
	.pop()
	.extend() 连接两个列表
	.insert() 在指定位置插入

### tuple 元组
	与list类似，有序，但不可修改(immutable)
	'tuple' object does not support item assignment

### Object-Oriented
	python 支持面向对象，但与java/c++不同的是
	1. python 不需要variable defination,
	2. __ == private 
	3. __xxx__ 特殊变量
	4 _xx ??
	python 支持inheretance like java single inheretance

### Some features: Generators 

```python
L = [x * x for x in range(10)] generate all at one time
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
g

```

### 对比：
速度：
https://benchmarksgame.alioth.debian.org/u64q/python.html
http://benchmarksgame.alioth.debian.org/u64q/java.html

