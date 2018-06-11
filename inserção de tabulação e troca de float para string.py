Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dic {}
SyntaxError: invalid syntax
>>> dic = {}
>>> keys in dic
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    keys in dic
NameError: name 'keys' is not defined
>>> key in dic
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    key in dic
NameError: name 'key' is not defined
>>> key in dic
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    key in dic
NameError: name 'key' is not defined
>>> key in dic
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    key in dic
NameError: name 'key' is not defined
>>> dic [teste] = 1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dic [teste] = 1
NameError: name 'teste' is not defined
>>> dic ["teste"] = 1
>>> 
>>> 
>>> 
>>> key in dic
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    key in dic
NameError: name 'key' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> key in dict
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    key in dict
NameError: name 'key' is not defined
>>> key in dict dic
SyntaxError: invalid syntax
>>> key in dic
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    key in dic
NameError: name 'key' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 1 in dic
False
>>> 
>>> 
>>> 
>>> key in dic
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    key in dic
NameError: name 'key' is not defined
>>> 
>>> 
>>> 
>>> teste in dic
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    teste in dic
NameError: name 'teste' is not defined
>>> dic
{'teste': 1}
>>> 
>>> 
>>> 
>>> "teste" in dic
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dic
{'teste': 1}
>>> def dobro (x):
	return x*2

>>> dobro (2)
4
>>> def
SyntaxError: invalid syntax
>>> dobro
<function dobro at 0x0000024469B8EBF8>
>>> dobro ()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dobro ()
TypeError: dobro() missing 1 required positional argument: 'x'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lisr (dobro)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    lisr (dobro)
NameError: name 'lisr' is not defined
>>> list (dobro)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list (dobro)
TypeError: 'function' object is not iterable
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def bom_dia()
SyntaxError: invalid syntax
>>> def bom_dia(): print ("Bom dia, humanoide!")

>>> 
>>> 
>>> 
>>> bom_dia()
Bom dia, humanoide!
>>> 
>>> 
>>> 
>>> bom_dia("idiota")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    bom_dia("idiota")
TypeError: bom_dia() takes 0 positional arguments but 1 was given
>>> bom_dia(nome = "idiota"):
	
SyntaxError: invalid syntax
>>> def bom_dia(nome = "idiota"):
	print ("Bom dia, %s" % nome)

	
>>> 
>>> 
>>> bom_dia
<function bom_dia at 0x0000024469B8EEA0>
>>> bom_dia ()
Bom dia, idiota
>>> bom_dia ("otário")
Bom dia, otário
>>> import
SyntaxError: invalid syntax
>>> import calendar
>>> 
>>> 
>>> calendar
<module 'calendar' from 'D:\\Program Files\\Python36\\lib\\calendar.py'>
>>> 
>>> 
>>> calendar.prmonth(2000,3)
     March 2000
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
>>> calendar.prmonth(2017,12)
   December 2017
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
>>> calendar.prcall (2017)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    calendar.prcall (2017)
AttributeError: module 'calendar' has no attribute 'prcall'
>>> calendar.prcal (2017)
                                  2017

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5             1  2  3  4  5
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
23 24 25 26 27 28 29      27 28                     27 28 29 30 31
30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31

>>> calendar.monthcalendar (2017,12)
[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]
>>> from calendar import monthcalendar
>>> 
>>> 
>>> 
>>> monthcalendar ()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    monthcalendar ()
TypeError: monthdayscalendar() missing 2 required positional arguments: 'year' and 'month'
>>> monthcalendar
<bound method Calendar.monthdayscalendar of <calendar.TextCalendar object at 0x0000024469BBDF98>>
>>> for semana in monthcalendar (2017,12):
	print semana
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(semana)?
>>> for semana in monthcalendar (2017,12):
	print (semana)

	
[0, 0, 0, 0, 1, 2, 3]
[4, 5, 6, 7, 8, 9, 10]
[11, 12, 13, 14, 15, 16, 17]
[18, 19, 20, 21, 22, 23, 24]
[25, 26, 27, 28, 29, 30, 31]
>>> from string import join
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    from string import join
ImportError: cannot import name 'join'
>>> from str import join
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    from str import join
ModuleNotFoundError: No module named 'str'
>>> str.join ()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    str.join ()
TypeError: descriptor 'join' of 'str' object needs an argument
>>> str.join (".",("a","b","c"))
'a.b.c'
>>> str.join (("a","b","c"))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    str.join (("a","b","c"))
TypeError: descriptor 'join' requires a 'str' object but received a 'tuple'
>>> str.join ("a","b","c")
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    str.join ("a","b","c")
TypeError: join() takes exactly one argument (2 given)
>>> str.join (["a","b","c"])
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    str.join (["a","b","c"])
TypeError: descriptor 'join' requires a 'str' object but received a 'list'
>>> str.join ("",["a","b","c"])
'abc'
>>> str.join (" ",["a","b","c"])
'a b c'
>>> str.join ("+",["a","b","c"])
'a+b+c'
>>> str.join (" + ",["a","b","c"])
'a + b + c'
>>> s = monthcalendar (2017,12) [0]
>>> s
[0, 0, 0, 0, 1, 2, 3]
>>> 
>>> 
>>> 
>>> map (str,s)
<map object at 0x0000024469BBDFD0>
>>> s
[0, 0, 0, 0, 1, 2, 3]
>>> map (string,s)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    map (string,s)
NameError: name 'string' is not defined
>>> map (string,s)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    map (string,s)
NameError: name 'string' is not defined
>>> map (str, s)
<map object at 0x0000024469DE7E80>
>>> map (chr, s)
<map object at 0x0000024469BBDFD0>
>>> list (map (str, s))
['0', '0', '0', '0', '1', '2', '3']
>>> 
>>> 
>>> 
>>> join (list (map (str, s)), "\t")
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    join (list (map (str, s)), "\t")
NameError: name 'join' is not defined
>>> str.join (list (map (str, s)), "\t")
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    str.join (list (map (str, s)), "\t")
TypeError: descriptor 'join' requires a 'str' object but received a 'list'
>>> str.join (list (map (chr, s)), "\t")
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    str.join (list (map (chr, s)), "\t")
TypeError: descriptor 'join' requires a 'str' object but received a 'list'
>>> 
>>> 
>>> 
>>> 
>>> tab = "\t"
>>> 
>>> 
>>> 
>>> tab.join (s)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    tab.join (s)
TypeError: sequence item 0: expected str instance, int found
>>> s
[0, 0, 0, 0, 1, 2, 3]
>>> str.join (list (map (chr, s))

	  
KeyboardInterrupt
>>> str.join (list (map (chr, s)))
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    str.join (list (map (chr, s)))
TypeError: descriptor 'join' requires a 'str' object but received a 'list'
>>> str.join (map (chr, s))
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    str.join (map (chr, s))
TypeError: descriptor 'join' requires a 'str' object but received a 'map'
>>> str.join (map (chr, s))
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    str.join (map (chr, s))
TypeError: descriptor 'join' requires a 'str' object but received a 'map'
>>> s
[0, 0, 0, 0, 1, 2, 3]
>>> str (s)
'[0, 0, 0, 0, 1, 2, 3]'
>>> str.join (str (s))
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    str.join (str (s))
TypeError: join() takes exactly one argument (0 given)
>>> str.join (str (s),"\t"))
SyntaxError: invalid syntax
>>> str.join (str s,"\t")
SyntaxError: invalid syntax
>>> str.join (str s,)
SyntaxError: invalid syntax
>>> str.join (str s)
SyntaxError: invalid syntax
>>> str.join (str (s))
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    str.join (str (s))
TypeError: join() takes exactly one argument (0 given)
>>> str.join (str (s),1))
SyntaxError: invalid syntax
>>> str.join (str (s),1)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    str.join (str (s),1)
TypeError: can only join an iterable
>>> str.join (str (s),"1")
'1'
>>> s
[0, 0, 0, 0, 1, 2, 3]
>>> str.join (str (s),"5")
'5'
>>> str.join ("1",str (s))
'[101,1 101,1 101,1 101,1 111,1 121,1 131]'
>>> str.join ("\t",str (s))
'[\t0\t,\t \t0\t,\t \t0\t,\t \t0\t,\t \t1\t,\t \t2\t,\t \t3\t]'
>>> str.join (\t,str (s))
SyntaxError: unexpected character after line continuation character
>>> str.join ('\t',str (s))
'[\t0\t,\t \t0\t,\t \t0\t,\t \t0\t,\t \t1\t,\t \t2\t,\t \t3\t]'
>>> str.join ("1",'\t',str (s))
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    str.join ("1",'\t',str (s))
TypeError: join() takes exactly one argument (2 given)
>>> str.join (s,str (s))
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    str.join (s,str (s))
TypeError: descriptor 'join' requires a 'str' object but received a 'list'
>>> str.join (1,str (s))
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    str.join (1,str (s))
TypeError: descriptor 'join' requires a 'str' object but received a 'int'
>>> string s
SyntaxError: invalid syntax
>>> string (s)
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    string (s)
NameError: name 'string' is not defined
>>> str (s)
'[0, 0, 0, 0, 1, 2, 3]'
>>> s
[0, 0, 0, 0, 1, 2, 3]
>>> str.join (1,str (s))
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    str.join (1,str (s))
TypeError: descriptor 'join' requires a 'str' object but received a 'int'
>>> str.join ('\t',str (s))
'[\t0\t,\t \t0\t,\t \t0\t,\t \t0\t,\t \t1\t,\t \t2\t,\t \t3\t]'
>>> return str.join ('\t',str (s))
SyntaxError: 'return' outside function
>>> map (str, (s))
<map object at 0x0000024469DE7518>
>>> list (map (str, (s)))
['0', '0', '0', '0', '1', '2', '3']
>>> str.join ("\t",list (map (str, (s))))
'0\t0\t0\t0\t1\t2\t3'
>>> print (str.join ("\t",list (map (str, (s)))))
0	0	0	0	1	2	3
>>> print (str.join ("\t",list (map (str, (s)))))
0	0	0	0	1	2	3
>>> 
>>> 
>>> 
>>> 
>>> monthcalendar (2017,12)
[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]
>>> for semana in monthcalendar (2017,12):
	print (str.join ("\t",list (map (str, (semana)))))

	
0	0	0	0	1	2	3
4	5	6	7	8	9	10
11	12	13	14	15	16	17
18	19	20	21	22	23	24
25	26	27	28	29	30	31
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for semana in monthcalendar (2017,12):
	
	print (str.join ("\t",list (map (str, (semana)))))

	
0	0	0	0	1	2	3
4	5	6	7	8	9	10
11	12	13	14	15	16	17
18	19	20	21	22	23	24
25	26	27	28	29	30	31
>>> for semana in monthcalendar (2017,12):
	
	print (str.join ("\t",list (map (str, (semana)))))
	break

0	0	0	0	1	2	3
>>> for semana in monthcalendar (2017,12):
	print ("Seg""\t""Ter""\t""Qua""\t""Qui""\t""Sex""\t""Sab""\t""Dom")
	print (str.join ("\t",list (map (str, (semana)))))

	
Seg	Ter	Qua	Qui	Sex	Sab	Dom
0	0	0	0	1	2	3
Seg	Ter	Qua	Qui	Sex	Sab	Dom
4	5	6	7	8	9	10
Seg	Ter	Qua	Qui	Sex	Sab	Dom
11	12	13	14	15	16	17
Seg	Ter	Qua	Qui	Sex	Sab	Dom
18	19	20	21	22	23	24
Seg	Ter	Qua	Qui	Sex	Sab	Dom
25	26	27	28	29	30	31
>>> c=calendar.TextCalendar (calendar.SUNDAY)
>>> c
<calendar.TextCalendar object at 0x0000024469DE7518>
>>> list (c)
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    list (c)
TypeError: 'TextCalendar' object is not iterable
>>> str=c.formatmounth (2017,12)
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    str=c.formatmounth (2017,12)
AttributeError: 'TextCalendar' object has no attribute 'formatmounth'
>>> str=c.formatmonth (2017,12)
>>> 
>>> 
>>> 
>>> print (str)
   December 2017
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

>>> 
>>> 
>>> calendar.day_name
<calendar._localized_day object at 0x0000024469BBDDA0>
>>> calendar.day_name ()
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    calendar.day_name ()
TypeError: '_localized_day' object is not callable
>>> calendar.day_name (SUNDAY)
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    calendar.day_name (SUNDAY)
NameError: name 'SUNDAY' is not defined
>>> day=calendar.day_name
>>> 
>>> 
>>> day
<calendar._localized_day object at 0x0000024469BBDDA0>
>>> print (day)
<calendar._localized_day object at 0x0000024469BBDDA0>
>>> calendar.SUNDAY
6
>>> calendar.6
SyntaxError: invalid syntax
>>> calendar.day_name
<calendar._localized_day object at 0x0000024469BBDDA0>
>>> print (calendar.day_name)
<calendar._localized_day object at 0x0000024469BBDDA0>
>>> str=c.formatyear (2017)
>>> str
'                                  2017\n\n      January                   February                   March\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4\n 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11\n15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18\n22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25\n29 30 31                  26 27 28                  26 27 28 29 30 31\n\n       April                      May                       June\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n                   1          1  2  3  4  5  6                   1  2  3\n 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10\n 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17\n16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24\n23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30\n30\n\n        July                     August                  September\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n                   1             1  2  3  4  5                      1  2\n 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9\n 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16\n16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23\n23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30\n30 31\n\n      October                   November                  December\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n 1  2  3  4  5  6  7                1  2  3  4                      1  2\n 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9\n15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16\n22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23\n29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30\n                                                    31\n'
>>> print (str)
                                  2017

      January                   February                   March
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11
15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18
22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25
29 30 31                  26 27 28                  26 27 28 29 30 31

       April                      May                       June
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                   1          1  2  3  4  5  6                   1  2  3
 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30
30

        July                     August                  September
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                   1             1  2  3  4  5                      1  2
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
30 31

      October                   November                  December
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7                1  2  3  4                      1  2
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9
15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16
22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23
29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30
                                                    31

>>> print (c.formatyear (2017))
                                  2017

      January                   February                   March
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11
15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18
22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25
29 30 31                  26 27 28                  26 27 28 29 30 31

       April                      May                       June
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                   1          1  2  3  4  5  6                   1  2  3
 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30
30

        July                     August                  September
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                   1             1  2  3  4  5                      1  2
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
30 31

      October                   November                  December
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7                1  2  3  4                      1  2
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9
15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16
22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23
29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30
                                                    31

>>> 
>>> 
>>> print (c.formamonth (2017))
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    print (c.formamonth (2017))
AttributeError: 'TextCalendar' object has no attribute 'formamonth'
>>> print (c.formatmonth (2017))
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    print (c.formatmonth (2017))
TypeError: formatmonth() missing 1 required positional argument: 'themonth'
>>> print (c.formatmonth (2017,12))
   December 2017
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

>>> print (c.formatmonth (2017,12))
   December 2017
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

>>> print (str.join ("\t",list (map (str, (s)))))
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    print (str.join ("\t",list (map (str, (s)))))
TypeError: 'str' object is not callable
>>> s
[0, 0, 0, 0, 1, 2, 3]
>>> str.join ('\t',str (s))
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    str.join ('\t',str (s))
TypeError: 'str' object is not callable
>>> for semana in monthcalendar (2017,12):
	print ("Seg""\t""Ter""\t""Qua""\t""Qui""\t""Sex""\t""Sab""\t""Dom")
	print (str.join ("\t",list (map (str, (semana)))))

	
Seg	Ter	Qua	Qui	Sex	Sab	Dom
Traceback (most recent call last):
  File "<pyshell#241>", line 3, in <module>
    print (str.join ("\t",list (map (str, (semana)))))
TypeError: 'str' object is not callable
>>> semana
[0, 0, 0, 0, 1, 2, 3]
>>> str
'                                  2017\n\n      January                   February                   March\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4\n 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11\n15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18\n22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25\n29 30 31                  26 27 28                  26 27 28 29 30 31\n\n       April                      May                       June\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n                   1          1  2  3  4  5  6                   1  2  3\n 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10\n 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17\n16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24\n23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30\n30\n\n        July                     August                  September\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n                   1             1  2  3  4  5                      1  2\n 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9\n 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16\n16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23\n23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30\n30 31\n\n      October                   November                  December\nSu Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa\n 1  2  3  4  5  6  7                1  2  3  4                      1  2\n 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9\n15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16\n22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23\n29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30\n                                                    31\n'
>>> del str
>>> str
<class 'str'>
>>> 
>>> 
>>> 
>>> for semana in monthcalendar (2017,12):
	print ("Seg""\t""Ter""\t""Qua""\t""Qui""\t""Sex""\t""Sab""\t""Dom")
	print (str.join ("\t",list (map (str, (semana)))))

	
Seg	Ter	Qua	Qui	Sex	Sab	Dom
0	0	0	0	1	2	3
Seg	Ter	Qua	Qui	Sex	Sab	Dom
4	5	6	7	8	9	10
Seg	Ter	Qua	Qui	Sex	Sab	Dom
11	12	13	14	15	16	17
Seg	Ter	Qua	Qui	Sex	Sab	Dom
18	19	20	21	22	23	24
Seg	Ter	Qua	Qui	Sex	Sab	Dom
25	26	27	28	29	30	31
>>> print (str.join ("\t",list (map (str, (semana)))))
25	26	27	28	29	30	31
>>> monthcalendar (2017,12)
[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]

>>> semana = monthcalendar (2017,12)
>>> semana
[[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]
>>> print (str.join ("\t",list (map (str, (semana)))))
[0, 0, 0, 0, 1, 2, 3]	[4, 5, 6, 7, 8, 9, 10]	[11, 12, 13, 14, 15, 16, 17]	[18, 19, 20, 21, 22, 23, 24]	[25, 26, 27, 28, 29, 30, 31]
>>> for semana in monthcalendar (2017,12):
	print (str.join ("\t",list (map (str, (semana)))))

	
0	0	0	0	1	2	3
4	5	6	7	8	9	10
11	12	13	14	15	16	17
18	19	20	21	22	23	24
25	26	27	28	29	30	31

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
