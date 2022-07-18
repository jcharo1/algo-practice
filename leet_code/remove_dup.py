s = "abc" 
t = "ahbgdc"
diff=[]
for char in t:
    if char not in s:
        diff.append(char)

print(diff)



def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 0: return True
        s_index = 0
        for i, char in enumerate(t):
            if char == s[s_index]:
                if s_index == len(s)-1:
                    return True
                s_index+=1
        return False







s = "axc" 
t = "ahbgdc"

diff=[]
for char in t:
    if char not in s:
        diff.append(char)

print(diff)