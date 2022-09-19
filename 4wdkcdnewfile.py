import random
x=50
t=[x]
y=random.randint(1,100)

print(x)
print(y)

if x in range(1,26):
 print("1w")
elif x in range(26,51):
 print("2w")
elif x in range(51,76):
 print("3w")
elif x in range(76,101):
 print("4w")
 
if y in range(1,26):
 y1=random.randint(1,6)
elif y in range(26,51):
 y1=random.randint(1,6)
 y2=random.randint(1,6)
elif y in range(51,76):
 y1=random.randint(1,6)
 y2=random.randint(1,6)
 y3=random.randint(1,6)
elif y in range(76,101):
 y1=random.randint(1,6)
 y2=random.randint(1,6)
 y3=random.randint(1,6)
 y4=random.randint(1,6)