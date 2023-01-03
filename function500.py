def plus_minus(a, b, c):
    c = a + b + c
    d = a - b - c
    return c, d

def tree():
    print('''
    ---1---
    --121--
    -12321-
    1234321''')
    
def addition(a,b):
    return a+b
print(addition(1,2))

def addition3(a,b,c):
    return a+b+c
print(addition3(1,2,3))

def square(a):
    return a**2
print(square(16)) #>>256

def square_list(A):
    square_list = [int(i**2) for i in A]
    return square_list
print(square_list([1,2,3,4,5])) #>>> [1, 4, 9, 16, 25]

def sum_square_list(listA):
    square_list = [int(i**2) for i in listA]
    sum_sqlist = sum(square_list)
    return sum_sqlist
print(sum_square_list([1,2,3,4,5])) #>>> 55

def sum_int(listA):
    sumlist = sum(listA)
    return sumlist
print(sum_int([1,2,3,4,5])) #>>> 15

def concat_2string(str1, str2):
    return str1 + str2
print(concat_2string('Goo','gle')) #>>> Google

def concat_3string(str1,str2,str3):
     return str1 + str2 + str3
 
def del_word(str1, str2):
    return str1.replace(str2,'')

print(del_word('onetwothree','two')) #>>>onethree

def repeat_word(str1, k):
    word = str1 + "-"
    word_k = word*k
    return word_k[:-1]
print(repeat_word('one',3))

def sum_len(listA):
    suml = [len(i) for i in listA if type(i) == str]
    suml = sum(suml)
    return suml
print(sum_len(['food','drink','snack',1,2,3]))


