Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10,b=12.3,c='codegnan'
SyntaxError: cannot assign to literal
>>> a,b,c=10,12.3,'codegnan'
>>> a
10
>>> b
12.3
>>> c
'codegnan'
>>> print('a=',a,'b=',b,'c=',c)
a= 10 b= 12.3 c= codegnan
>>>  print('a=',a,'b=',b,'c=',c,sep='')
 
SyntaxError: unexpected indent
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=10b=12.3c=codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='',end='\n\n\n')
a=10b=12.3c=codegnan


>>> print('a=',a,'b=',b,'c=',c,sep='.')
a=.10.b=.12.3.c=.codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='',end=@)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print('a=',a,'b=',b,'c=',c,sep='',end='@')
a=10b=12.3c=codegnan@
>>> print(f'a={a} b={b} c={c} ')
a=10 b=12.3 c=codegnan 
>>> print('a=%d b=%f c=%s')
a=%d b=%f c=%s
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.300000 c=codegnan
>>> print("a{} b={} c={}".format(a,b,c))
a10 b=12.3 c=codegnan
>>> print("a{} b={} c={}".format(b,a,c))
a12.3 b=10 c=codegnan
>>> print("a{0} b={1} c={2}".format(b,a,c))
a12.3 b=10 c=codegnan
>>> print("a={0} b={1} c={2}".format(b,a,c))
a=12.3 b=10 c=codegnan
>>> 