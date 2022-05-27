dic = {"Jane": "choco",
"Dave": "candy",
"Jenny": "jelly"
}

dic["Jane"] #key

print(dic["Jane"])

dic["Jane"] = "coffee" #value 값 변경 

print(dic["Jane"])


#함수에서 dictionary 쓰기 for key in dictionary

for key in dic: 
    print("{}:{}".format(key,dic[key]))

dic["Peter"] = "cheese" #추가 

print()
for key in dic:
    print("{}:{}".format(key,dic[key]))

del dic["Dave"] #제거 
print()
for key in dic:
    print("{}:{}".format(key,dic[key]))