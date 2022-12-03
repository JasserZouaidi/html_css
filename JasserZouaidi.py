def remplir1 (f1) :
    r = ""
    while r.upper() != "N" :
        l = ""
        for i in range (4) :
            ch = ""
            for j in range (5) :
                ch += str(randint(0,1))
            l += ch + " "
        f1.write(l + "\n")
        r = input('Continuez (O/N) ?')
        while r.upper() not in {"O","N"} :
            r = input('Continuez (O/N) ?')
    f1.close



def one (x) :
    ch = str(x)
    r = 0
    for i in range (len(ch)) :
        if ch[i] == "1" :
            r += 1
    return r




def tri(t,n):
    for i in range(n):
        max = i
    for j in range(i+1,n):
        if one(t[max]) < one(t[j]):
            max = j
    if i != max :
        a = t[i]
        t[i] = t[max]
        t[max] = a

def remplir2 (f1,f2) :
    f1 = open('binaire.txt',"r")
    l = f1.readline()
    print(l)
    while l != "" :
        i = 0
        ch = ""
        t = array([int]*100)
        while l != "" :
            t[i] = l[0:5]
            l = l[6::]
            i += 1
        tri(t,i)
        for j in range (i) :
            ch += str(t[i]) + " "
        print(ch)
        f2.write(ch + "\n")
        l = f1.readline()
    f1.close()
    f2.close()

        
def afficher(f2) :
    f2 =open('res.txt',"r")
    ch = f2.readline()
    while ch != "" :
        print(ch)
        ch = f2.readline()
    f2.close()



#pp
from numpy import array
from random import randint
f1 = open('binaire.txt',"w")
remplir1(f1)
f2 =open('res.txt',"w")
remplir2(f1,f2)
afficher(f2)