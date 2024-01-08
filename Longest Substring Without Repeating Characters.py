def lengthOfLongestSubstring(s):
    # Initialize variables
    max_length = 0

    i = 0
    j = 0
    char_count = {}
    ans = ""

    # Iterate through the string
    while j < len(s):
        # Update the count of the current character in the map
        if s[j] in char_count:
            char_count[s[j]] += 1
        else:
            char_count[s[j]] = 1

        # Check if the number of distinct characters is greater than window size
        if len(char_count) > (j - i + 1):
            j += 1
        # Check if the number of distinct characters is equal to window size
        elif len(char_count) == (j - i + 1):
            # Update the maximum length and substring if needed
            if j - i + 1 > max_length:
                max_length = j - i + 1
                ans = s[i:j+1]
            j += 1
        # Check if the number of distinct characters is smaller than window size
        else:
            # Move the left pointer to reduce the number of distinct characters
            while len(char_count) < j - i + 1:
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i += 1
            j += 1

    # Return the final result
    return ans,max_length
string = input("Input String: ")
s,res = lengthOfLongestSubstring(string)
print("Longest substring without repeating characters: ",s,res)
