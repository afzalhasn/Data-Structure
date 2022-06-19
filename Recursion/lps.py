def lps(X,i,j):
    if i>j:
        return 0
    if i == j:
        return 1
    if X[i] == X[j]:
        return 2 + lps(X,i+1,j-1)
    else:
        return max(lps(X,i,j-1), lps(X,i+1,j))
X = "GXTAYXB"
print ("Length of LPS is ", lps(X ,0, len(X)-1) )
