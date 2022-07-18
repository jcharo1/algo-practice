


s = "foo"
t = "bar"
def isomorphic(s,t):
    s_t_dict= {}
    t_s_dict = {}
    d=zip(s,t)
    print()
    for s1,t1 in d:
        s_t_dict[s1]=t1
        t_s_dict[t1] =s1
        print("s1")
    print(len(d))
    d=zip(s,t)
    for s1,t1 in d:
        print("s1")
        print((s_t_dict.get(s1)))
        print((t_s_dict.get(t1)))
        if (s_t_dict.get(s1)) != (t1) or (t_s_dict.get(t1)) != s1:
            return False
    return True
print(isomorphic(s,t))   



