i=int(input("Enter a num "))
orig=i
sum=0

while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Number is Armstong")
else:
    print("Number is not armstrong")
