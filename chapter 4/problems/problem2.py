# write a program to accept marks of 6 students and display them in a sorted manner.


print("ENTER YOUR  MARKS\n")

Marks = []

f1 = int(input("ENTER YOUR MARKS: "))
Marks.append(f1)
f2 = int(input("ENTER YOUR MARKS: "))
Marks.append(f2)
f3 = int(input("ENTER YOUR MARKS: "))
Marks.append(f3)
f4 = int(input("ENTER YOUR MARKS: "))
Marks.append(f4)
f5 = int(input("ENTER YOUR MARKS: "))
Marks.append(f5)
f6 = int(input("ENTER YOUR MARKS: "))
Marks.append(f6)


print("\nHERE IS THE ALL MARKS IN SORTED MANNER\n")
Marks.sort()

print(Marks) 

print("\nThanks..!!!")


