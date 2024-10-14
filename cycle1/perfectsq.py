n=int(input("Enter the no.of elements:"))
sum1=0
for i in range(1,n):
    if(n%i ==0):
        sum1=sum1+i
if(sum1 ==n):
    print("the number is perfect number")
else:
    print("the number is not a perfect number")