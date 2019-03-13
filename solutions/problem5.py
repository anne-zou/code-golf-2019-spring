n=open("../inputs/5.txt","r")
o=open("../answers/5.txt","a")
for w in n:
    for i in reversed(range(1,len(w)+1)):
        o.write(w[:i]+"\n")
    for i in range(2, len(w)+1):
        o.write(w[:i]+"\n")