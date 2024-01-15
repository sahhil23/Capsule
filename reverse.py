x= int(input("enter a number:"))
rev=0
while x > 0:
    rev= rev * 10 + x % 10
    x //=10
print(f"reverse  is{rev}")  