// men bu men Sarvarman Xalmetov
f=open("omadlatto.txt","w")
a=1;
b=2;
for c in range(b,30):
   if ((c==a) or (c==b)):continue
   for d in range(c,31):
    if ((d==a) or (d==b) or (d==c)):continue
    for e in range(d,32):
     if ((e==a) or (e==b) or (e==c) or (e==d)):continue
     for i in range(e,33):
      if ((i==a) or (i==b) or (i==c) or (i==d) or (i==e)):continue
      for j in range(i,34):
       if ((j==a) or (j==b) or (j==c) or (j==d) or (j==e) or (j==i)):continue
       for k in range(j,35):
        if ((k==a) or (k==b) or (k==c) or (k==d) or (k==e) or (k==i) or (k==j)):continue
        for m in range(k,36):
         if ((m==a) or (m==b) or (m==c) or (m==d) or (m==e) or (m==i) or (m==j)or (m==k)):continue
         for n in range(m,37):
          if ((n==a) or (n==b) or (n==c) or (n==d) or (n==e) or (n==i) or (n==j)or (n==k) or (n==m)):continue
          f.write("| ")
          f.write(str(a))  
          f.write(" ")
          f.write(str(b))
          f.write(" ")
          f.write(str(c))
          f.write(" ")
          f.write(str(d))
          f.write(" ")
          f.write(str(e))
          f.write(" ")
          f.write(str(i))
          f.write(" ")
          f.write(str(j))
          f.write(" ")
          f.write(str(k))
          f.write(" ")
          f.write(str(m))
          f.write(" ")
          f.write(str(n))
          f.write(" |")
          f.write("\n")
f.close
