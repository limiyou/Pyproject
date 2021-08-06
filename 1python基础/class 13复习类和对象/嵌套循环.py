cases=[
    ["yuze",18,"男"],
    ["junjun",17,"女"],
    ["yingying",19,"女"]
]
#转化成字典["name","age“，"gender"]
keys=["name","age","gender"]
li=[]
for case in cases:
    d={}
    for idx,column in enumerate(case):
        d[keys[idx]]=column
    li.append(d)
print(li)
        


list=["this",'is','a','list']
for index,item in enumerate(list):
    print(index,item)