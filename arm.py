num=int(input())
sum=0
t=num
while t>0:
  digit=t%10
  sum+=digit**3
  t//=10
if num==sum:
  print("yes")
else:
  print("no")
