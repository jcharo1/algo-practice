# Code design 
In this problem I decided to implent a Trie or Prefix Tree due to its structure that store a dynamic set of strings.

    
# Time Efficiency 
worst case run time complexity for a trie is a combination of `m`, the length of the longest key, and `n` the total number of keys in the trie. Therefore creating a runtime of `O(m*n)`
the time complexity of searching, inserting or deleting from a trie depends on the total length of the word `a` and the total number of words `n` making a runtime of `O(a*n)

# Space Complexity
Space complexity of this problem `O(n)`