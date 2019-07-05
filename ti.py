a,b=map(int,input().split())
for number in range(a+1,b):
  if number>1:
    for i in range(2,number):
      if(number%i)==0:
        break
    else:
     print(number,end=" ")
