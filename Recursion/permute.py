def permute(s):
    if len(s) == 1:
        return s
    output=[]
    for i,let in enumerate(s):
        for p in permute(s[:i]+s[i+1:]):
            output.append(let+p)
    return(output)
print(permute("abc"))
