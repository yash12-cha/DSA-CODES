s1 = input()
s2 = input()
temp = " "
# length of first string
l1 = len(s1)
# length of second string
l2 = len(s2)
# length of both strings should be equal
if (l1 != l2):
    print("Strings are not rotations of each other.")
else:
    temp = s1 + s1
    if (temp.count(s2)> 0):
        print("Strings are rotations of each other.")
    else:
        print("Strings are not rotations of each other.")
    
