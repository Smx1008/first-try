p=["buff","buff","nerf"]
i=["sword","shield"]
t=[12,27,4,7,9]

def menu(p,i,t):
 m=[]
 m.append("1.Frequence")
 m.append("2.Items")
 m.append("3.Team")
 print("   M E N U")
 print("-------------")
 print("")
 for item in m:
  print(item)
  print("")
 cho=""
 while cho !="1"and cho!="2"and cho!="3"and cho!="quit":
  cho=input("enter your desired section(1,2,3):")
  print("")  
  if cho=="1":
   print(m[0])
   print("-------------") 
   print("")
   print("1.1")
   print("-------------")
   for item in p:
    print("  ",item)
    print("")
  elif cho=="2":
   print(m[1])
   print("-------------")
   print("")
   print("2.1")
   print("-------------")
   for item in i:
    print("  ",item)
    print("")  
  elif cho=="3":
   print(m[2])
   print("-------------")
   print("")
   print("3.1")
   print("-------------")
   for item in t:
    print("  ",item)
    print("")
  elif cho=="quit":
   print("menu closed")
  
menu(p,i,t)