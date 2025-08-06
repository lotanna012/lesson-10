num=int(input("enter a 3 digit number :"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=digit**3
    temp=temp//10
if num==sum:
        print("\n" ,sum, "is  an armstrong number" )
else:
        print("\n" ,sum, "is not  an armstrong number" )

