i= int(input("enter a number:"))
a = len(str(i))
#print(a)
#b = len(i)
orig=i
sum=0
while i > 0:
   sum +=(i % 10) ** a
   i //=10
if sum==orig:
   print("amstrong number")
else:
   print("not amstrng nmber")