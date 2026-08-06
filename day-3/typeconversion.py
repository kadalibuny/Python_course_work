Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> float(a)
10.0
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> b=10.3434
>>> int(b)
10
>>> srt(b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    srt(b)
NameError: name 'srt' is not defined
>>> str (b)
'10.3434'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> s1='bunny'
>>> int(s1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int(s1)
ValueError: invalid literal for int() with base 10: 'bunny'
>>> float(s1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float(s1)
ValueError: could not convert string to float: 'bunny'
>>> list(s1)
['b', 'u', 'n', 'n', 'y']
>>> tuple()s1(
	
SyntaxError: invalid syntax
>>> tuple(s1)
('b', 'u', 'n', 'n', 'y')
>>> set(s1)
{'u', 'b', 'y', 'n'}
>>> dict(s1)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict(s1)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> a1=[1,2,3,4,5]
>>> int(a1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(a1)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(a)
10.0
>>> float(a1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(a1)
TypeError: float() argument must be a string or a number, not 'list'
>>> str(a1)
'[1, 2, 3, 4, 5]'
>>> set(a1)
{1, 2, 3, 4, 5}
>>> dict(a1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(a1)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> q1=(1,2,3,4,5)
>>> int(q1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(q1)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> float(q1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(q1)
TypeError: float() argument must be a string or a number, not 'tuple'
>>> str(q1)
'(1, 2, 3, 4, 5)'
>>> dict(q1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(q1)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> s1={1,2,3,4,5}
>>> int(s1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(s1)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> list(s1)
[1, 2, 3, 4, 5]
>>> dict(s1)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(s1)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> d1={'name':'bunny','age':20}
>>> int(d1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(d1)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> float(d1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float(d1)
TypeError: float() argument must be a string or a number, not 'dict'
>>> str(d1)
"{'name': 'bunny', 'age': 20}"
>>> tuple(d1)
('name', 'age')
>>> list(d1)
['name', 'age']
>>> z=2+7j
>>> int(z)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(z)
TypeError: can't convert complex to int
>>> float(z)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    float(z)
TypeError: can't convert complex to float
>>> str(z)
'(2+7j)'
>>> bool(z)
True
>>> 