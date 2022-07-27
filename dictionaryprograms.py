from first import  d

for k,v in  d.items():
   # print(k,v)
    if isinstance(v,list):
        #print(v)
        for j in v:
            print(j)
            if isinstance(j,dict):

               for l ,m in j.items():
                   print(l,m)
'''d={
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
for i in d.values():
    #print(i)
    if isinstance(i,list):
        for j in i:
            #print(j)
            if isinstance(j,dict):
                for k in j:
                    print(k)'''
