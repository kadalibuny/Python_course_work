Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import keyword
>>> print(len(keyword.kwlist))
35
>>> print(keywors.kwlist)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(keywors.kwlist)
NameError: name 'keywors' is not defined. Did you mean: 'keyword'?
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a=10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b=b,a
>>> a
10
>>> b=20
>>> b
20
>>> a,b=b,a
>>> a
20
>>> b
10
