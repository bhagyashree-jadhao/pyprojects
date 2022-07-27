def add(a,b,c):
    sum=a+b+c
    print(sum)
'''add(10,20,30)#positional argument
def sub(a,b=20):#Default adgument
    print("values if aand b are : ",a,b)
sub(10,50)
def mult(a,b):
    print("Mult of two no is :" ,a*b)
mult(a=4,b=7)#Keyword argument
def add1(*m):
    sum=0
    for i in m:
        sum=sum+i
    print(f"Addition of all element in  tuple {m} = {sum}")

add1(10,20,30,40)
def even(*m):
    for i in m:
        if i%2==0:
            print(i)

even(11,22,33,55,66,77,88,99,100,120)
l=(11,22,33,55,66,77,88,99,100,120)
s=list(filter(lambda a:a%2==0,l))
print(s)
s1=list(filter(lambda  x: x if x%2==0 else False,l))
print(s1)
s2=list(map(lambda x:x*2,l))
print(s2)
str1="AEUIOaeiou"
str2=input(("Enter the string"))
#return vowels
l=list(filter(lambda x : x if x in str1 else False, str2))
print(l)
#remove duplicates char or number in list
l2=[]
list1=[10,20,11,10,11,30]
dup=(list(filter(lambda x : l2.append(x) if x not in l2 else False,list1)))
print(dup)
l2=[]
def dupl(*list1):

    for i in list1:
        if i not in l2:
            l2.append(i)
    print(l2)
x=(10,20,40,30,20,10,40)
remove=list(filter(dupl,x))
print(remove)
list1=[10,20,11,10,11,30]
list1.insert(3,70)
print(list1)
s='welcome to python'
s4=''
i=0
while i<len(s):
    if s[i] not in s4:
        s4=s4+s[i]
print(s4)'''
