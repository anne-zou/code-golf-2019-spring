o=open("../answers/2.txt","a")
n=open("../inputs/2.txt","r")
for p in n:
    a,b=p.split(" ")
    a=str(bin(int(a[2:])))
    b=str(bin(int(a[2:])))
    o.write(str(sum(x!=y for x,y in zip((32-len(a))*"0"+a,(32-len(b))*"0"+b)))+"\n")