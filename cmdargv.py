from sys import argv
print("Total argument present ",len(argv))
print("first argument is ",argv[0])
sum=0
for i in argv[1:]:
    #sum=sum+int(i)
    print(i)
print(sum)