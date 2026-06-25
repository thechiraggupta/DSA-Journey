n=list(map(int,input("Enter the number:").split()))

pos=0

for i in range(len(n)):
    if n[i]!=0:
        n[pos]=n[i]
        pos+=1

for i in range(pos, len(n)):
    n[i]=0

print(n)