def fordit_szam(a,b):
    szam1=str(a)
    szam2=str(b)
    szam1=szam1[::-1]
    szam2=szam2[::-1]
    x=int(szam1)+int(szam2)
    x=str(x)
    x=x.strip("0")



    return x

print(fordit_szam(305,794))

