o=open("../answers/1.txt","a")
def p(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=2
for x in range(3,10**5):
    if p(x):
        if a+2==x:
            o.write(a,x)
        a=x
