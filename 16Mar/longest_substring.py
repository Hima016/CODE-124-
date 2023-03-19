def longest_common_substring(word1, word2):
    m = len(word1)
    n = len(word2)
    # Create a 2D array to store the lengths of the common substrings
    # dp[i][j] represents the length of the longest common suffix of word1[0:i] and word2[0:j]
    dp = [[0] * (n+1) for _ in range(m+1)]
    # Initialize the base case: empty strings have no common suffix
    max_len = 0
    # Fill in the 2D array using dynamic programming
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0
    return max_len
m=input()
n=input()
print(longest_common_substring(m,n))