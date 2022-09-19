import random
x=50
p=random.randint(1,3)

if p==1:
 x=(x+5)
 print("your unit got 5 lvl points!")
elif p==2:
 x=(x+10)
 print("your unit got 10 lvl points!")
else:
 x=(x-5)
 print("your unit lost 5 lvl points")

t=[x] 
d=["yes","no"]

def test(t):
 y=random.randint(1,100)
 print("facing enemy with",y,"lvl points")
 if t[0]>y:
  print("win")
  print(t)
  z=random.randint(1,10)
  if z>5:
   c=""
   while c!=d[0] and c!=d[1]:
    c=input("do u want to collect?: ")
    if c==d[0]:
     t.append(y)
     print("collected!")
     print(t)
    elif c==d[1]:
     print("not collected...")
  else:
   print("there is nothing left to collect...")
 else:
  print("lose")
  del t[0]
  print("your first unit got demolished!")
  if len(t)>=1:
   print(t)
  if len(t)==0:
   print("no units left, game over!")

print(x)               
while len(t)>=1:
 test(t)
