def numRabbits(answers):
    """
    Calculate the minimum number of rabbits in the forest based on their answers.
    """
    answer_counts = {}
    total_rabbits = 0

    for answer in answers:
        if answer in answer_counts:
            answer_counts[answer] += 1
        else:
            answer_counts[answer] = 1

        # When the count reaches answer + 1, it forms a complete group
        if answer_counts[answer] == answer + 1:
            total_rabbits += answer + 1
            answer_counts[answer] = 0  # Reset the count for this answer

    # Add remaining rabbits that didn't form a complete group
    for answer, count in answer_counts.items():
        if count > 0:
            total_rabbits += answer + 1

    return total_rabbits

answers = [1,1,2]
ans = numRabbits(answers)


'''
Time complexity:

-> Counting Answers: Iterating through the answers list of length n to count occurrences takes O(n) time.
-> Processing Counts: Iterating through the keys in the answer_counts dictionary, which can have at most n unique keys, also takes O(n) time.
-> Overall: Both steps are linear in the size of the input, so the total time complexity is O(n).

Space complexity:

-> Dictionary Storage: The answer_counts dictionary stores counts for each unique answer. In the worst case, where all answers are unique, it will have n entries, leading to O(n) space usage.
-> Additional Variables: Other variables like total_rabbits and loop variables use constant space.
-> Overall: The dominant space usage comes from the dictionary, resulting in O(n) space complexity.
'''