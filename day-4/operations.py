Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python operators
>>> '''
1.Art
2.Com
3.ass
4.rel
5.mem
6.ide
7.bit
'''
'\n1.Art\n2.Com\n3.ass\n4.rel\n5.mem\n6.ide\n7.bit\n'
>>>   a=10
  
SyntaxError: unexpected indent
>>> a=10
>>> b=5
>>> a+b
15
>>> a-b
5
>>> a*b
50
>>> a/2
5.0
>>> a//2
5
>>> 9.2/3
3.0666666666666664
>>> 9.2//2
4.0
>>> a=10
>>> b=4
>>> a<b
False
>>> a>b
True
>>> a<=b
False
>>> b=>a
SyntaxError: invalid syntax
>>> b>=a
False
>>> b==a
False
>>> a!=b
True
>>> a=8
>>> a+=2
>>> a
10
>>> a-=5
>>> a
5
>>> a**=6
>>> a
15625
>>> a-=625
>>> a
15000
>>> a/500
30.0
>>> a/=5
>>> a
3000.0
>>> a//=4
>>> a
750.0
>>> a+=1
>>> a
751.0
>>> int(a)
751
>>> a//=7
>>> a
107.0
>>> a
107.0
>>> type(a)
<class 'float'>
>>> int(a)
107
>>> type(a)
<class 'float'>
>>> email=true
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    email=true
NameError: name 'true' is not defined
>>> email= True
>>> password= Flase
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    password= Flase
NameError: name 'Flase' is not defined
>>> password= False
>>> email and password
False
>>> email or password
True
>>> not email
False
>>> not password
True
>>> ❤️
SyntaxError: invalid character '❤' (U+2764)
>>> print(❤)
SyntaxError: invalid character '❤' (U+2764)
>>> print("❤")
❤
>>> mnvrjkvm,mfjhvx 
KeyboardInterrupt
>>> l=[1,2,3,4]
>>> 1 in l
True
>>> 6in l
False
>>> 5in l
False
>>> 5 not in l
True
>>> l not in l
True
>>> lin l
SyntaxError: invalid syntax
>>> i in l
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    i in l
NameError: name 'i' is not defined
>>> 4in l
True
>>> t=('mango','papaya',"kiwi")
>>> mango in t
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    mango in t
NameError: name 'mango' is not defined
>>> 'mango' in t
True
>>> 'tamato' in t
False
>>> 'kiwi' not in t
False
>>> s={'sa','rey','ga','ma'}
>>> 'sa' in s
True
>>> 'rey' not in s
False
>>> 'pa' in s
False
>>> d={'name':'bunny','age':20}
>>> 'age' in d
True
>>> l=[1,2,3,4,5]
>>> m=[1,2,3,4,5]
>>> id(l)
2245738853824
>>> id(m)
2245738872640
>>> l is m
False
>>> m is l
False
>>> m is not l
True
>>> l is not m
True
>>> n=m
>>> id(m)
2245738872640
>>> id(n)
2245738872640
>>> #bitwise operators
>>> ~-23
22
>>> 11 & 12
8
>>> 11 | 12
15
>>> 2<<2
8
>>> 2>>2
0
>>> 2<<3
16
>>> 2<<10
2048
>>> 2<<8
512
>>> 2<<2
8
>>> 2>>8
0
>>> print(2<<2)
8
>>> ~12
-13
>>> ~-12
11
>>> ~232323
-232324
>>> ~-323232
323231
>>> 8>>2
2
>>> 8>>2
2
>>> 2<<2
8
>>> 