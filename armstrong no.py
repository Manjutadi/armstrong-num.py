#armstrong  no
n=int(input())
cnt=0
temp=n
while n:
    r=n%10
    n=n//10
    cnt+=1
n=temp
#print(cnt)
arm=0
while n:
    r=n%10
    n=n//10
    arm=arm+pow(r,cnt)
if arm==temp:
    print("armstrong")
else:
    print("not an armstrong")
