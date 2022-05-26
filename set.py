a= {8,3,'JENNY'}

b= [6,4,3,5,5,5,5,8]

c=set(b)

print(a)
print(c)
print(len(c))

logs = [
    ("Jane","Hi"),
    ("Dave","Hi"),
    ("Jane","Hi"),
    ("Chris","Hi"),
    ("David","Hi"),
    ("Jason","Hi"),
    ("Jane","Hi"),
    ("Naomi","Hi"),
    ("Jane","Hi"),
    ("Peter","Hi"),
    ("Jane","Hi"),
   
]

users = [user for (user,message) in logs]
print(users)
unique_users =set(users)
print(unique_users)
print(len(unique_users))

users = {user for (user,message) in logs}

print(users)

a= {1,2,3}
b={3,4,5}

print(a|b) # 합집합
print(a-b) # 차집합
print(a&b) # 교집합
print(a^b) # 대칭차집합 