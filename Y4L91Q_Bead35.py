
import matplotlib.pyplot as plt
import numpy as np
def db_in_lista(ls):
    x = np.array(ls)
    plt.hist(x)
    plt.show()
    db=0
    for i in range(len(ls)):
        elem = ls.count(i)
        if elem > db:
            db = elem
            s = i
    if db > len(ls)/2:
        s=str(s)
        db=str(db)
        return s+"("+db+"-szer/-szor szerepel a listában)"




print(db_in_lista([7,5,3,3,5,8,3,3,3,3,4]))