a = 31
t = type(a)      #class 'int'
print(t)      #prints <class 'int'>

b = 3.14
t = type(b)      #class 'float'
print(t)      #prints <class 'float'>

c = "Shreyang"
t = type(c)      #class 'str'
print(t)      #prints <class 'str'>

d = "3.14"
t = type(d)      #class 'str'
print(t)       #prints <class 'str'>
#double quotes are used to define a string, even if the string contains numbers, it is still of type 'str' and not 'float'

a = "3.14"
b = float(a)
t = type(b)     #class 'float'
print(t)     #prints <class 'float'>
