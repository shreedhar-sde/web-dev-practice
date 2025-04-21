def encrypt(n,k):
    n=n.lower()
    n_=''
    for i in n:
        if i==' ':
            n_+='$'
            continue
        if i=='$':
            n_+=' '
            continue
        x=ord(i)-96
        r=(x+k)%26
        r1= 26 if r==0 else r
        d=r1+96
        n_+=chr(d)
        # print(i,x,r,r1,n_)
    return n_
print(encrypt('xk$bqvjlildfzxi$xasbkqrob',-23))
# print(encrypt('qeb$nrfzh$yoltk$clu$grjmp$lsbo$qeb$ixwv$ald',-23))