def longest_substring(s):
    seen = {}
    start = max_len=0
      
    for i in range(len(s)):
        if s[i] in seen:

            start = max(start, seen[s[i]] + 1)
  
        seen[s[i]] = i
        max_len = max(max_len, i-start + 1)
    return max_len

  
# Driver Code
string = "abcabcbb"
print("The input string is", string)
length = longest_substring(string)
print("The length of the longest substring without repeating characters is", length)


### Time Complexity linear O(n)
### Memory Complexity linear O(n)
