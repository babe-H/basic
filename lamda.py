# 콜백 함수 
from ast import Lambda


def call_10_times(func):
    for i in range(10):
     func(i)
   

def print_love(number):
    print("Je T'aime",number)

call_10_times(print_love)

# lambda function

call_10_times(lambda number: print("Je T'aime", number))

# filter function # map function

def  only_even(number):
    return number%2 == 0

a= list(range(100))
b= filter(only_even,a)  # filter function ( f(x)  ,  x ) 
print(list(b))

b= filter(lambda number: number%2 == 0, a)
print(list(b))

def times(number):
    return number*number

a= list(range(100))
print(list(map(lambda number: number*number, a)))


