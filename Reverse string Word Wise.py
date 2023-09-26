def reverseWords(s):
    i = len(s) - 1 # Initialize i to the last index of the input string
    ans = "" # Initialize an empty string to store the reversed words
    # Iterate through the input string from the end to the beginning
    while i >= 0:
       # Skip over any leading spaces by decrementing i
        while i >= 0 and s[i] == ' ':
            i -= 1
        # Set j to the current value of i, which is the end index of the current word
        j = i
        # Break the loop when leading spaces are encountered
        if i < 0:
            break
        # Decrement i until a space character is encountered, which is the start index of the current word
        while i >= 0 and s[i] != ' ':
            i -= 1
        # If ans is empty, add the current word to it; otherwise, add a space followed by the current word
        if len(ans) == 0:
            ans += s[i + 1:j + 1]
        else:
            ans += " " + s[i + 1:j + 1]

    return ans
s = input("Input String: ")
res = reverseWords(s)
print("Output: ",res)

'''
Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(n), where n is the length of the input string.
'''
