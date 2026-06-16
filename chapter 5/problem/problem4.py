# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s. add('20') # length of s after these operations?


# 20 == 20.0  ,  so this both are same then this will consider as a single value
# so the lenght of this set should be 2

print(len(s))

