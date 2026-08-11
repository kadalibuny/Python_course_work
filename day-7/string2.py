Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='         hello   world   '
s.strip()
'hello   world'
s.lstrip()
'hello   world   '
s.rstrip()
'         hello   world'
s.repalce('  ','')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.repalce('  ','')
AttributeError: 'str' object has no attribute 'repalce'. Did you mean: 'replace'?
s.repalce('   ','')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.repalce('   ','')
AttributeError: 'str' object has no attribute 'repalce'. Did you mean: 'replace'?
s.replace('   ','')
'helloworld'
s='java-python-flask-mysql-fastupi-c'
s.split('-',3)
['java', 'python', 'flask', 'mysql-fastupi-c']
s.plit('-')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.plit('-')
AttributeError: 'str' object has no attribute 'plit'. Did you mean: 'split'?
s.split('-')
['java', 'python', 'flask', 'mysql', 'fastupi', 'c']
s.split(' & ',2)
['java-python-flask-mysql-fastupi-c']
s.split('%',2)
['java-python-flask-mysql-fastupi-c']
s.rsplit('-',3)
['java-python-flask', 'mysql', 'fastupi', 'c']
l='''python
java
sql
c'''
l
'python\njava\nsql\nc'
l.splitlines()
['python', 'java', 'sql', 'c']
c=['python','java','sql','c']
"".join(c)
'pythonjavasqlc'
' '.join(c)
'python java sql c'
'0'.join(c)
'python0java0sql0c'
c={'python','java','sql','c'}
"".join(c)
'cpythonsqljava'
''.join((1,2,3))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    ''.join((1,2,3))
TypeError: sequence item 0: expected str instance, int found
''.join(('1','2','3'))
'123'
c.partition('.')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c.partition('.')
AttributeError: 'set' object has no attribute 'partition'
c.partition(',')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.partition(',')
AttributeError: 'set' object has no attribute 'partition'
a='string.py'
a.partition(',')
('string.py', '', '')
a.partition('.')
('string', '.', 'py')
a.rpartition('.')
('string', '.', 'py')
a='string.png'
a.startswith('str')
True
a.startswith('list')
False
a.endswith('.py')
False
a.endswith('py')
False
a.endswith('png')
True
'python'.islower()
True
'PYTHON#$$'.isupper()
True
"Good Boy".istitle()
True
>>> 'good boy'.istitle
<built-in method istitle of str object at 0x000002532A74A9B0>
>>> 'good boy'.istitle()
False
>>> 'estbab'.isalpha()
True
>>> '12mn34nm'.isalnum()
True
>>> '12342432345432'.isnum()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    '12342432345432'.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> '12342432345432'.isalnum()
True
>>> ' '.isspace()
True
>>> ''.isspace()
False
>>> 'print'.isidentifier()
True
>>> 'add'.isidentifier()
True
>>> 'q'.isidentifier()
True
>>> 'qwqewfwrv'.isidentifier()
True
>>> '112121223222346458909876543212345678'.isnumeric()
True
>>> '12w2ww'.isnumeric()
False
