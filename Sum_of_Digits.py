i=int(input("Enter a Num "))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("Sum of digits=",sum)
