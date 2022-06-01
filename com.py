# 내포 ( comprehension )
# 반복 가능한 것 -> 반복 가능한 것 
# list , dictionary , set , generator

Orgin = [0,1,2,3,4,5,6,7,8 ]
New = []

for i in Orgin:
    if i%2 == 1:
        New.append(i)

# 결과로 리스트 => 리스트 내포 

print (New)


# 결과로 리스트 => 리스트 내포 

New = [i for i in Orgin if i % 2 == 1] #결과 요소의 표현식  #반복문   #조건문 

print(New)  

New = ( i for i in Orgin if i % 2 == 1 )

print("********************Generator :")

print(New)
print(list(New))
print(type(New))

New = { i for i in Orgin if i % 2 == 1 } # set

print(New)

New = {str(i)*3 : i for i in Orgin if i % 2 == 1 }  # dictionary

print(New)  