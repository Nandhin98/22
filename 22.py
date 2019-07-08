 def gcd(n,k):
     if (n>k):
         small=k
     else:
         small=n
     for i in range(1,small+1):
         if((n%i==0)and(k%i==0)):
             hcf=i
     return hcf
   n,k=map(int,input().split())
  print(gcd(n,k))
