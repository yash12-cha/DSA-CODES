def getLps(p):
    l = 0
    index = 1
    m = len(p)
    lps = [0] * m

    while index < m:

        if p[index] == p[l]:
            l += 1
            lps[index] = l
            index += 1
        else:

            if l == 0:
                lps[index] = 0
                index += 1
            else:
                # Skipping characters.
                l = lps[l - 1]

    return lps


def zAlgorithm(s, p):
    n = len(s)
    m = len(p)
    c = 0
    lps = getLps(p)

    # We will use these indices to traverse in s and p.
    index1 = 0
    index2 = 0

    while index1 < n:

        if s[index1] == p[index2]:

            index1 += 1
            index2 += 1


        else:

            if index2 == 0:
                index1 += 1
            else:
                # Skipping the characters.
                index2 = lps[index2 - 1]
        if index2 == m:
            c += 1
            index2 = lps[index2 - 1]
    return c

s = input("Input Text: ")
p = input("Input Pattern: ")
res = zAlgorithm(s,p)
print("The number of occurrences of pattern in given text is: ",res)

'''
Input:-
Input Text: zzzzyz
Input Pattern: zz

Output:-
The number of occurrences of pattern in given text is:  3
'''
