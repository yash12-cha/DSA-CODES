s1 = input()
s2 = input()
res = input()
# length of first string
l1 = len(s1)
# length of second string
l2 = len(s2)
# length of result string
lr = len(res) 
# length of result string should be equal to sum of two strings
if ((l1 + l2) != lr):
    print("Not a valid shuffle of given string.")
else:
    i = 0
    j = 0
    k = 0
    while (k < lr):
        if (i < l1 and s1[i] == res[k]):
            i = i + 1
        elif (j < l2 and s2[j] == res[k]):
            j = j + 1
        else:
            break
        k = k + 1
    if ( i < l1 or j < l2):
        print("Not a valid shuffle of given string.")
    else:
        print("Valid shuffle of given string.")
    
