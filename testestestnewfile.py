import random
x=50
y=("")
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
 
print("your unit is now lvl",x)

t=[x] 
d=["yes","no"]

def dice_list(level):
 dice_list =  []
 if level in range(1,26):
  dice_list.append(random.randint(1,6))
 elif level in range(26,51):
  dice_list.append(random.randint(1,6))
  dice_list.append(random.randint(1,6))
 elif level in range(51,76):
  dice_list.append(random.randint(1,6))
  dice_list.append(random.randint(1,6))
  dice_list.append(random.randint(1,6))
 elif level in range(76,101):
  dice_list.append(random.randint(1,6))
  dice_list.append(random.randint(1,6))
  dice_list.append(random.randint(1,6))
  dice_list.append(random.randint(1,6))      
 return dice_list

x_list =  dice_list(t[0])
y_list =  dice_list(y)

def test(t):
 y=random.randint(1,100)
 print("facing enemy with",y,"lvl points")
 print("unit lvl",t[0],"vs","enemy unit lvl",y)
 x_list =  dice_list(t[0])
 y_list =  dice_list(y)
 print("")
 print("-------------")
 print("lvl",t[0])
 print("")

 print('X LIST')
 for item in x_list:
   print(str(item))

 print("-------------")
 print("lvl",y)
 print("")

 print('Y LIST')
 for item in y_list:
 	print(str(item))
	
 print("-------------")
 print("")
 print("X list",sum(x_list))
 print("Y list",sum(y_list))
 print("")
 if sum(x_list)>sum(y_list):
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
     go=""
     while go!=d[0] and go!=d[1]:
      go=input("keep going?:")
      if go==d[1] :
       print("")
       print("menu")
       input("quit menu:")
    elif c==d[1]:
     print("not collected...")
     go=""
     while go!=d[0] and go!=d[1]:
      go=input("keep going?:")
      if go==d[1] :
       print("")
       print("menu")
       input("quit menu:")
  else:
   print("there is nothing left to collect...")
   go=""
   while go!=d[0] and go!=d[1]:
    go=input("keep going?:")
    if go==d[1] :
     print("")
     print("menu")
     input("quit menu:")
 else:
  print("lose")
  del t[0]
  print("your first unit got demolished!")
  if len(t)>=1:
   print(t)
   go=""
   while go!=d[0] and go!=d[1]:
    go=input("keep going?:")
    if go==d[1] :
     print("")
     print("menu")
     input("quit menu:")
  if len(t)==0:
   print("no units left, game over!")

go=""
while go!=d[0] and go!=d[1]:
 go=input("are you ready?:")
 if go==d[1] :
  print("")
  print("menu")
  input("quit menu:")       
while len(t)>=1:
 print("")
 test(t)