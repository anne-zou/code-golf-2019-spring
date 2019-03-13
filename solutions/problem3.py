o=open("../answers/3.txt","a")
n=open("../inputs/3.txt","r")
for s in n:
    if s!="":
        t=s[0]
        f=t
        for i in range(1,len(s)):
            c=s[i]
            if c<s[i-1]:
                t=c
            else:
                t+=c
                if len(t)>len(f):
                    f=t
        o.write(f+"\n")
    o.write("")