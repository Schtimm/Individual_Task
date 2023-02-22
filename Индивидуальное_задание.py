from random import*
def Listbuild(a, cap):
    a=[]
    cap=int(cap)
    for i in range(cap):
        a.append(randint(5,1000))
    return a
b=[]
print(Listbuild(b, 20))
