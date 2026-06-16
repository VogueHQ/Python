# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,21]}




'''no we can't update because
first thing, we cannot include list in the set
and also we cannot index set'''

'even if there is no list in set then we can only add and remove element in the set , we cannot update anything on the set'



'''s = {8, 7, 12, "Harry"}

s.add(99)        # add new item
s.remove(7)      # remove an item

print(s)  # {8, 12, 99, "Harry"}'''
'we can do this ⬆️'


'''s = {8, 7, 12, "Harry"}

s[0] = 100  # ❌ CRASH — TypeError
but cannot do this ⬆️'''
