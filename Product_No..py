i=int(input("Enter a Num "))
prod=1
while(i>0):
    prod=prod*(i%10)
    i=i//10
print("Product of digits=",prod)
