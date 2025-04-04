Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #non bool type in logical operator
>>> 5 and 6
6
>>> -5 and 6
6
>>> 1.2 and 2.3
2.3
>>> 0.0 and 0.6
0.0
>>> 0 and 9
0
>>> 5+2j and 3+4j
(3+4j)
>>> 5+2j and 0+0j
0j
>>> 5+2j and 4+0j
(4+0j)
>>> '' and 'by'
''
>>> 'hi' or 'by'
'hi'
>>> #short circuit in IDLE
>>> 5 anc 6
SyntaxError: invalid syntax
>>> 5 anc 6
SyntaxError: invalid syntax
>>> 5and 6
6
>>> 
>>> 0 and 6
0
>>> 5 and 0
0
>>> 0 or 6
6
>>> 0 or 0
0
5 or 9 0
SyntaxError: invalid syntax





5 or 9
5


