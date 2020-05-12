import tsp
def koordinates(n):
    ls = []
    if n == 1:
        x = input("Adjon meg egy koordinátát','-vel elválasztva:")
        print("1")
    if n == 2:
        for i in range(n):
            x = input("Adjon meg egy koordinátát','-vel elválasztva:")
        print("1,2")
    if n == 3:
            a = input("Adjon meg egy koordinátát','-vel elválasztva:")
            ax ,ay = a.split(",")
            ax = int(ax)
            ay = int(ay)
            b = input("Adjon meg egy koordinátát','-vel elválasztva:")
            bx,by = b.split(",")
            bx = int(bx)
            by = int(by)
            c = input("Adjon meg egy koordinátát','-vel elválasztva:")
            cx, cy = c.split(",")
            cx = int(cx)
            cy= int(cy)
            s1 = min(abs(ax - bx),abs(ay - by))
            s2 = min(abs(ax-cx),abs(ay-cy))
            s3 = min(abs(bx-cx),abs(by-cy))
            ls = [s1,s2,s3]
            if max(ls) ==  s1:
                print("1,3,2")
            if max(ls) == s2:
                print("1,2,3")
            if max(ls) == s3:
                print("2,1,3")
    else:
        for i in range(n):
            x = input("Adjon meg egy koordinátát','-vel elválasztva:")
            z,y = x.split(",")
            z=int(z)
            y=int(y)
            ls.append((z,y))
        t = tsp.tsp(tuple(ls))
        t = t[1]
        for i in t:
            print(i+1,end=",")

n = int(input("Adj meg a koordináta számát(0 és 40 között): "))
koordinates(n)