def f(x):
    return x+5

numList = [1,2,3,4,5,6,7,8,9]

print(list(map(f,numList)))

# 내장함수 map을 사용하지 않는다면 

temList = []

for i in numList:
    temList.append(f(i))

print(temList)

# 프로그래머 김플 