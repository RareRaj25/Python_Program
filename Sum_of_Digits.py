i=int(input("Enter a Num "))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
if(sum%2==0):
    
    print("Sum of digits is even",sum)
else:
    print("Sum of digits is odd",sum)
            
    

