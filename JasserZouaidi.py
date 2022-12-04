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
    f1.close()

def one (ch) :
    r = 0
    for i in range (5) :
        if ch[i] == "1" :
            r += 1
    return r

def tri(t,n):
    for i in range(n):
        m = i
        for j in range(i+1,n):
            if one(t[m]) < one(t[j]):
                m = j
        if i != m :
            a = t[i]
            t[i] = t[m]
            t[m] = a

def remplir2  (f1,f2) :
    f1 = open('binaire.txt',"r")
    l = f1.readline()
    while l != "" :
        ch = ""
        t = array([int]*4)
        for i in range (4) :
            t[i] = l[:5]
            l = l[6:]
        tri(t,4)
        for i in range (4) :
            ch += t[i] + " "
        f2.write(ch + "\n")
        l = f1.readline()
    f1.close()
    f2.close()

        
def afficher(f2) :
    f2 = open('res.txt',"r")
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
f2 = open('res.txt',"w")
remplir2(f1,f2)
afficher(f2)
