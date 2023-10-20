# Function to check if two strings are anagrams of each other
def isAnagram(s, t):
    hmap = {}  # Initialize a dictionary to store character counts
    
    # If the lengths of the two strings are different, they can't be anagrams
    if len(s) != len(t):
        return False

    # Count the occurrences of each character in string 's'
    for letter in s:
        if letter not in hmap:
            hmap[letter] = 1
        else:
            hmap[letter] += 1

    # Check if string 't' has the same characters and counts as 's'
    for letter in t:
        if letter not in hmap:
            return False  # If a character in 't' is not in 's', they can't be anagrams
        else:
            hmap[letter] -= 1
            if hmap[letter] == 0:
                del hmap[letter]  # Remove characters with a count of zero

    return True  # If all characters match, the strings are anagrams

# Input: Read two strings from the user
s = input("Input first string: ")
t = input("Input second string: ")

# Call the isAnagram function to check if they are anagrams
res = isAnagram(s, t)

# Print the result
if res:
    print("The two strings are anagrams of each other.")
else:
    print("The two strings are not anagrams of each other.")

    
'''
Input:-
Input first string: "anagram"
Input second string: "nagaram"

Output:-
The two strings are anagram of each other.

Time Complexity: O(n)
 '''
