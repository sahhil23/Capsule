num=int(input("entr a numbe"))
orig= num
rev=0
while num>0:
    rev=rev * 10+num%10
    num//=10
if rev==orig:
    print("pallindrom")
else:
    print("not pllndrm")