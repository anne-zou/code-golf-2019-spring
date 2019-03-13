o=open("../answers/2.txt","a")
n=open("../inputs/2.txt","r")
for p in n:
    a,b=p.split(" ")
    a=str(bin(a[2:]))
    b=str(bin(a[2:]))
    o.write(sum(x!=y for x,y in zip((32-len(a))*"0"+a,(32-len(b))*"0"+b))+"\n")