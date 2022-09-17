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


def findPattern(s, p):
    n = len(s)
    m = len(p)

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
            return True
    return False

s = input("Input Text: ")
p = input("Input Pattern: ")
res = findPattern(s,p)
if res == True:
    print("Pattern found in the text.")
else:
    print("Pattern not found in the text.")
    
'''
Input:-
Input Text: THIS IS A TEST TEXT
Input Pattern: TEXT

Output:- 
Pattern found in the text.

Time Complexity:-
O(N), where ‘N’ is the length of the string ‘S’.
Actually, the total time complexity will be O(N+M), where ‘M’ is the length of the string ‘P’, so we can simply say O(N) as ‘N’ will always be larger than 'M'.
'''
