#list
a=[1,2,3,4,5]
#print(a)
print(a[3])
print(a[-1])
print(a[0:4:2])
a=[1,23,1,45,567,7888888,'giri']
a.append('prasad')
print(a)
a.extend([33,4,55,676,88])
print(a)
print(a.count(1))
a.remove(45)
print(a)
a.pop(3)
print(a)
a=[22,344,566,]
a.insert(2,"kkk")
print(a)
a=[22,44,6778,899,000]
print(a.index(6778))
for a in [22,33,445,"jaggu"]:
    print(a)
a=[22,344,5]
print(len(a))
# tuple
a=()
print(type(a))
a=(1,2,44,556,7788,8998,)
print(a[-1])
print(a[0:3:2])
print(min(a))
print(max(a))
print(sum(a))
print(len(a))
#concatenation
a1=(1,3,4)
a2=(3,4,6)
print(a1+a2)
#repetation
a=(1,2,44,556,7788,8998,)
print(a*10)
#iteration
for i in a:
    print(i)
#membership operators
a=(1,2,44,556,7788,8998,)
print(1 in a)
print(2 not in a)
#identity operators
a1=(1,3,4)
a2=(1,3,4)
print(a1 is a2)
print(a1 is not a2)
# string
a= "sravanthi krish"
print(a.lower())
print(a.upper())
a="  giri prasad  "
print(a.endswith('prasad'))
print(a.startswith("giri"))
print(a.replace("prasad","anju"))
print(a.index("giri"))
print(a.find("anju"))
print(a.count('a'))
print(a.removeprefix('giri'))
print(a.removesuffix("prasad"))
print(a.split())
print(a.strip())
print(a.rstrip())
print(a.lstrip())
print(len(a))
v=a.lstrip()
print(len(v))
v=a.rstrip()
print(len(v))
#dictionary
a={}
print(type(a))
a={1:'abc',22:'giri','prasad':1}
print(a[22])
print(a.get(1))
print(a.keys())
print(a.values())
print(a.items())
a.update({222:334})
print(a)
for i,j in a.items():
    print(i,j)
del a[1]
print(a)
a["italy"]='roman'
print(a)
print(len(a))
#set

