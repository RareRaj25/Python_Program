i=int(input("Enter a num "))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse=",rev)
