Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

s='sowmya'
a='tummala'
a+b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a+b
NameError: name 'b' is not defined
s+a
'sowmyatummala'
a+s
'tummalasowmya'
a + s
'tummalasowmya'
b='num'
b*12
'numnumnumnumnumnumnumnumnumnumnumnum'
b='num.,'
b*019
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
b*19.2
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b*19.2
TypeError: can't multiply sequence by non-int of type 'float'
b*19
'num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,num.,'
names['sai krishan','prasad','bunny']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    names['sai krishan','prasad','bunny']
NameError: name 'names' is not defined
names=['sai krishan','prasad','bunny']
names
['sai krishan', 'prasad', 'bunny']
names(5:11)
SyntaxError: invalid syntax
names(5 : 11)
SyntaxError: invalid syntax
names([5 : 11]
      
SyntaxError: invalid syntax
names([5:11]
      
SyntaxError: invalid syntax
names[5:11]
      
[]
names [5]
      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names [5]
IndexError: list index out of range
names[2]
      
'bunny'
names[2:5]
      
['bunny']
names[10:12]
      
[]
bunny in names
      
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    bunny in names
NameError: name 'bunny' is not defined
'binny' in names
      
False
'sai' in names
      
False
'sai krishna' in names
      
False
len(names)
      
3
names3)
      
SyntaxError: unmatched ')'
names(3)
      
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    names(3)
TypeError: 'list' object is not callable
sort()names
      
SyntaxError: invalid syntax
sort(names)
      
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sort(names)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(names)
      
['bunny', 'prasad', 'sai krishan']
max(names)
      
'sai krishan'
min(names)
      
'bunny'
s-'codegnan'
      
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s-'codegnan'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
s='codegnan'
      
.
s.upper()
      
'CODEGNAN'
s.lower()
      
'codegnan'
s.swapcase
      
<built-in method swapcase of str object at 0x0000017694944530>
s.title()
      
'Codegnan'
s.center(20.)
      
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s.center(20.)
TypeError: 'float' object cannot be interpreted as an integer
s.center(10,'-')
      
'-codegnan-'
s.ijust(20,'-')
      
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s.ijust(20,'-')
AttributeError: 'str' object has no attribute 'ijust'. Did you mean: 'ljust'?
s.Ijust(20,'-')
      
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.Ijust(20,'-')
AttributeError: 'str' object has no attribute 'Ijust'. Did you mean: 'ljust'?
s.1just(20,'-')
      
SyntaxError: invalid imaginary literal
s.find('bunny')
      
-1
s.fid('codegnan')
      
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.fid('codegnan')
AttributeError: 'str' object has no attribute 'fid'. Did you mean: 'find'?
s.find('codegnan')
      
0
s.find(n)
      
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s.find(n)
NameError: name 'n' is not defined
s.rfind('n')
      
7
s.find('n')
      
5
s.count()''n
      
SyntaxError: invalid syntax
s.count('n')
      
2
s
      
'codegnan'
s
      
'codegnan'
e
      
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    e
NameError: name 'e' is not defined
s.replace('codegnan','butternan')
...       
'butternan'
>>> s.marktrans('aeiou','#%$_@')
...       
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.marktrans('aeiou','#%$_@')
AttributeError: 'str' object has no attribute 'marktrans'. Did you mean: 'maketrans'?
>>> s.maketrans('aeiou','#%$_@')
...       
{97: 35, 101: 37, 105: 36, 111: 95, 117: 64}
>>> s.translate(s.maketrans('aeiou','#%$_@'))
...       
'c_d%gn#n'
>>> text='hello @@@'
...       
>>> text.encode
...       
<built-in method encode of str object at 0x0000017694946CF0>
>>> text
...       
'hello @@@'
>>> text.encode()
...       
b'hello @@@'
>>> text.decode()
...       
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
