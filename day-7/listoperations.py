Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2.34,'str',True,[1,2,3],(1,2,3),{1,2,3},{1:2,2:3},2+5j]
1
1
l
[1, 2.34, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3}, (2+5j)]
m=[11,11,22,33,33,22,]
m
[11, 11, 22, 33, 33, 22]
a=[1,2,3]
b=[4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
b+a
[4, 5, 6, 1, 2, 3]
a*2
[1, 2, 3, 1, 2, 3]
b*4
[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
a[2]
3
a[4]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[4]
IndexError: list index out of range
a[0]
1
b[3]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b[3]
IndexError: list index out of range
b[2]
6
a[-1]
3
b[-2]
5
b[-3]
4
a[1:2]
[2]
a=[1,2,3,4,5,6]
a[1:2]
[2]
a[2:6]
[3, 4, 5, 6]
a[:]
[1, 2, 3, 4, 5, 6]
a[::]
[1, 2, 3, 4, 5, 6]
a[2::6]
[3]
a[1::5]
[2]
a=[10,20,30,40,20,10,22,44,88]
max(a)
88
min(a)
10
sorted(a)
[10, 10, 20, 20, 22, 30, 40, 44, 88]
a
[10, 20, 30, 40, 20, 10, 22, 44, 88]
len(a)
9
len(a)
9
a
[10, 20, 30, 40, 20, 10, 22, 44, 88]
a.ppend(1)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.ppend(1)
AttributeError: 'list' object has no attribute 'ppend'. Did you mean: 'append'?
a.append(a)
a
[10, 20, 30, 40, 20, 10, 22, 44, 88, [...]]
a.remove(a)
a
[10, 20, 30, 40, 20, 10, 22, 44, 88]
a.append(23)
a
[10, 20, 30, 40, 20, 10, 22, 44, 88, 23]
sorted(a)
[10, 10, 20, 20, 22, 23, 30, 40, 44, 88]
a.insert(2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.insert(2)
TypeError: insert expected 2 arguments, got 1
a.insert(2,1)
a
[10, 20, 1, 30, 40, 20, 10, 22, 44, 88, 23]
a.append(100)
a
[10, 20, 1, 30, 40, 20, 10, 22, 44, 88, 23, 100]
a.pop()
100
a.pop()
23
a.pop(5)
20
a
[10, 20, 1, 30, 40, 10, 22, 44, 88]
a.extend(1,1,2)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.extend(1,1,2)
TypeError: list.extend() takes exactly one argument (3 given)
a.extend([1,1,1])
a
[10, 20, 1, 30, 40, 10, 22, 44, 88, 1, 1, 1]
a.count(1)
4
a.remove(1)
a
[10, 20, 30, 40, 10, 22, 44, 88, 1, 1, 1]
a.del([8::])
SyntaxError: invalid syntax
a.clear()
a
[]
a=[1,2,3,5]
a.append(12)
a
[1, 2, 3, 5, 12]
del a[1]
del[1:2]
SyntaxError: invalid syntax
del a[1:2]
a
[1, 5, 12]
del a[1:3]
a
[1]
a=[1,2,3]
a=b
>>> b
[4, 5, 6]
>>> b.append(20)
>>> a
[4, 5, 6, 20]
>>> b
[4, 5, 6, 20]
>>> c=a.copy()
>>> c
[4, 5, 6, 20]
>>> c.append(50)
>>> c
[4, 5, 6, 20, 50]
>>> a
[4, 5, 6, 20]
>>> any([1,'',False,[],{},(),set()])
True
>>> any([0,'',False,[],{},(),set()])
False
>>> all([1,'',False,[],{},(),set()])
False
>>> all([0,'',False,[],{},(),set()])
False
>>> a.reverse()
>>> a
[20, 6, 5, 4]
>>> a
[20, 6, 5, 4]
>>> a.sort()
>>> a
[4, 5, 6, 20]
