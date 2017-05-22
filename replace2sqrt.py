def re2sqrt(s):
    j = s.find("^(1/2)")
    while j != -1:
        j -= 1
        while '0'<=s[j]<='9':
            j=j-1
        s = s[:j+1]+'sqrt('+s[j+1:]
        s = s.replace("^(1/2)",")",1)
        j = s.find("^(1/2)")
    return s