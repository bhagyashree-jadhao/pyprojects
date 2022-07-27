
#1.sum of n term
'''m=int(input("Enter the number"))
n=int(input("Enter the number"))
sum=0
while n>=m:

    sum=sum+n
    n-=1
print(f"sum of {n} to {m} is ={sum}")'''
#o/p
#Enter the number10
#Enter the number20
#sum of 9 to 10 is =165

#2. sum of digit
'''num=eval(input("Enter the any number"))
sum=0

while num >0:
    mod=num%10
    sum=sum+mod
    num=num//10
print(sum)'''
#o/p
#Enter the any number35462
#20
#
#3. Reverse of number
'''n=int(input("Enter the number"))
rev=0
while n>0:
    mod=n%10
    rev=rev*10+mod
    n//=10
print(rev)'''
#o/p
# Enter the number56743
#34765
#4.sum of all even number in given range
'''num1=int(input("Enter the strat value"))
num2=int(input("Enter the end value"))
even_sum=0
odd_sum=0
while num1<num2:
    if num1%2==0:
        even_sum=even_sum+num1
    else:
        odd_sum=odd_sum+num1
    num1+=1
print(f"Even number sum is : {even_sum}")
print(f"Odd nummber sum is :{odd_sum}")'''
#o/p
#Enter the strat value1
#Enter the end value10
#Even number sum is : 20
#Odd nummber sum is :25
#5.Multiplication table
'''n=int(input("Enter the number"))
i=1
while i<11:
    print(n,'*',i,'=',n*i)
    i+=1'''
'''
Enter the numner6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60
'''
#print Armstrong number in range
'''num1=int(input("Enter the strat number"))
num2=int(input("Enter the end value"))
for num in range(num1,num2):
    sum=0
    temp=num
    while temp>0:
        mod=temp%10
        sum=sum+mod*mod*mod
        temp//=10

    if num==sum:
        print(f"{num}is armstrong")
    else:
        continue
'''
'''#Output
Enter the strat number100
Enter the end value999
153is armstrong
370is armstrong
371is armstrong
407is armstrong
'''
#7check number is Palindrom number
'''num1=int(input("Enter the  number"))
sum=0
num=num1
while num1>0:
    mod=num1%10
    sum=sum*10+mod
    num1//=10
if num==sum:
    print("Given number {}is palindreom".format(num))
else:
    print("{}number is not palindrom".format(num))'''
#to check prime number
'''num1=int(input("Enter  strating range:"))
num2=int(input("Enter the last number"))
print("Prime numbers:", end=' ')
if num1>=2:
    for n in range(num1,num2):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n,end=' ')
else:
    print("Plese enter valid number and first number should greter than 2")'''
from test import power
from test import cube
cube(2)


