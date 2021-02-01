Input:-

import random

n = int(input('Enter a Number'))
l=[]
s=0
while len(l)<n-1:
    k = random.randint(1,n)
    if k not in l:
        s+=k
        l.append(k)
        print("random no: ",k)
print('missing no. is: ', n*(n+1)//2 - s)


Output:-

Enter a Number5
random no:  2
random no:  3
random no:  1
random no:  5
missing no. is:  4