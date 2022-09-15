def isAnagram(s, t):
    # Initalize an empty dictionary
    hmap = {}
    # Return False if both strings are of different length
    if len(s) != len(t):
        return False

    # Iterate through the first string, adding each element to the dictionary and
    # increasing the value by one when the element is already in the dictionary
    for letter in s:
        if not letter in hmap:
            hmap[letter] = 1
        else:
            hmap[letter] += 1

        # Iterate through the second string, checking if the element of t is within the
        # dictonary and decreasing the value each time it is.
        # Once the value of a key reaches to 0, you delete the key from the hashmap.
    for letter in t:
        if not letter in hmap:
            return False
        else:
            hmap[letter] -= 1
            if hmap[letter] == 0:
                del hmap[letter]

    return True

s = input("Input first string: ")
t = input("Input second string: ")
res = isAnagram(s,t)
if res == True:
    print("The two strings are anagram of each other.")
else:
    print("The two strings are not anagram of each other.")

    
'''
Input:-
Input first string: "anagram"
Input second string: "nagaram"

Output:-
The two strings are anagram of each other.

Time Complexity: O(n)
 '''
