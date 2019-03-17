import random
import math
import collections
from datetime import date

# Create two list of unequal size

l1 = random.sample(range(1,200),10)
print(l1)

l2 = random.sample(range(1,200),15)
print(l2)

# Print len of each list
print("Len of first")
print(len(l1))

print("Len of second")
print(len(l2))

# Combine two list in single list

print("combine list")
l_combine = l1 + l2
print(l_combine)

# create new list which is twice in combined list (X2 --> e.g. 1--> 2)

l_combine_twice = []

for l in l_combine :
    l_combine_twice.append(l * 2)

print('all twice elements')
print (l_combine_twice)

# sort in asc
print('sort list in list asc')

l_combine_twice.sort()
print(l_combine_twice)

# sort in desc
print('sort list in desc')

l_combine_twice.sort(reverse = True)
print(l_combine_twice)

# max value
print("Max")
print(max(l_combine_twice))

# min value
print("Min")
print(min(l_combine_twice))

# select # 4, 5, 6, 7
print("4 elements")
for l_print in range(3,7):
    print(l_combine_twice[l_print])

print(l_combine_twice[3:7])

# select last 3 list from list
print("last 3 elements")
for l_print in range(-3,0):
    print(l_combine_twice[l_print])

# Create a new list with cube of existing value

print('Cube list')
listcube = [i**3 for i in l_combine_twice]
print(listcube)

# Create new list with square root of existing values (import math)

print('squert list')
listsquer = [math.sqrt(i) for i in l_combine_twice]
print(listsquer)

# Crreate a new list which adds 1 and then squers the sum
print("add 1 and then squers the sum")
listadd1andsquer = [(i + 1) ** 2 for i in l_combine_twice]
print(listadd1andsquer)

# check exists in
print("exists check of 21")
print(21 in l_combine_twice)

# Gen two dicnoery

dict1 = {'one' : 1, 'two' : 2,'three' : 3, 'four' : 4,'five' : 5, 'six' : 6}
dict2 = {'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10}

# Print Key for dict 1
print(dict1.keys())

# print value for dict 2
print(dict2.values())

# combine dicts
dict1.update(dict2)

# sort dict value list asc
list1 = dict1.values()
print('orginal list')
print(list1)

print("sorted list")
#list1.sort()
#print(list1)

for i , j in dict1.items() :
    print(i, j)

print("---------- sting list output--------")
# Create a list with 10 strings

str_list = ['a','z','c','d','f','g','h','i','j','k']

# Loop trough every element of the list using index number

for i in range(len(str_list)) :
    print(i, str_list[i])

# print a tuple of (index, string)
# another_tuple = tuple(str_list)

# save the tuple to another list
new_list = []

for i in range(len(str_list)) :
    new_list.append([i, str_list[i]])

# print(new_list)

another_tuple = tuple(new_list)

print(another_tuple)

another_list = list(another_tuple)

#print(another_list)

# Sort the new list of tuples in asc order of sting values

def takeSecond(elem):
    return elem[1]

another_list.sort(key = takeSecond)

print(another_list)

# Create a final list providing index numbers of ordered tuples

final_list = []

for i in range(len(another_list)) :
    final_list.append(another_list[i][0])

print(final_list)


print("----- one line -------")

#new_list.sort(key = lambda x : x[1])

#print(new_list)

nee_fin =[i[0] for i in sorted(enumerate(str_list),key = lambda x : x[1])]
print(nee_fin)

print("----- While loop-------")

# create a tuple of 10 int element

lw = random.sample(range(1,200),10)
wt = tuple(lw)
print(wt)
nlist = []

# Run a while loop to capture all element of the tuple and multiply by 2
i = 0
while i < len(wt) :
    nlist.append(wt[i] * 2)
    i+=1

#print(nlist)

print(nlist)
# Save the new value to different list


# OS commmands
import os

print("-------- OS --------")
print("File list")
print(os.listdir('/Users/mohnishbilimoria/documents/'))

print("Size of file")
print(os.stat('/Users/mohnishbilimoria/documents/Feb-10.py').st_size)

print("ext of file")
print(os.path.splitext('/Users/mohnishbilimoria/documents/Feb-10.py')[1])

print("----------File operations---------------")

# Select a folder with maximum files in it

filelist = []
for file in os.listdir('/Users/mohnishbilimoria/documents/') :
        if os.path.isfile(os.path.join('/Users/mohnishbilimoria/documents/', file)):
            filelist.append(file)

print(filelist)

dict_files = dict()

# check for os.path.join
for file in range(len(filelist)) :
    dict_files[filelist[file]] = ((os.stat('/Users/mohnishbilimoria/documents/' + filelist[file]).st_size))/1024**2

print(dict_files)

# Create a directory with filename as keys and file size as values

print("------- Functions -----------")

# Create function which accepts a number and returns its square value

def squervalue(input):
    return input**2

# Create a function which accepts 2 strings and check if they are qul in length
def checklen(str1, str2):
    return len(str1) == len(str2)

print(squervalue(2))
print(checklen('a','c'))

print("------------ assigmnet----------")

def divisby7(input) :
    if(input % 7 == 0) :
        return input

#print(divisby7(49))

def getage(yob, mob, dob):
    dobe = date(yob,mob,dob)
    today = date.today()
    return (today.year - dobe.year)
print("age is")
print(getage(1980,12,30))

# Find element comm in 2 list

def listcommon(list1, list2) :
    #resutlist = []
    for i in list1:
        if(i in list2):
            print (i)

(listcommon([1,2],[1,3]))

# find elements in list 1 only
def findinlist(num):
    listm = random.sample(range(1,200),10)
    if(num in listm):
        print("Found!!")
    else:
        print("NotFound")

findinlist(3)
# find if string is pelindrom

def reverse(str):
    return str[::-1]

def pelindrom(str):
    rev = reverse(str)

    if(str == rev):
        return True
    return False

#print(pelindrom('abc'))

# retain only pelindrom word from list

def pelindromlist(inlist):
    result = []
    for i in range(len(inlist)) :
        if(pelindrom(inlist[i])):
            result.append(inlist[i])
    
    return result

print(pelindromlist(['aba','abc']))

# Create 2 list of diif size with random function, reatin only uquioe values from both list

def uniquevalues(list1, list2):
    result = []
    for i in list1:
        if(i not in list2):
            result.append(i)
    
    return result

print(uniquevalues(random.sample(range(1,200),10),random.sample(range(1,200),15)))


# fibnnaci serise functin
def fibonacci(inputnum):
    n1 = 0
    n2 = 1
    nth = 1

    if(inputnum == 1):
        print(n1)
    else:
        print(n1)
        while nth < inputnum:
            
            print(" ")
            nth = n1 + n2

            n1 = n2
            n2 = nth
            print(n1)

fibonacci(10)


# create password genarter with lenght x

import string
import random

def randompassword(sizeofpass):
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(sizeofpass, sizeofpass + 4)
  return ''.join(random.choice(chars) for x in range(size))

print(randompassword(8))
# Create 2 list with random of unequal size create dictiry where element of list 2 will be key and bool output of whether present in list 1 will be value

def dictlist(list1,list2):
    dict_resu = dict()

    for l in list2:
        if(l in list1):
            dict_resu[l] = True
        else:
            dict_resu[l] = False
    
    return dict_resu

print(dictlist(random.sample(range(1,200),10),random.sample(range(1,200),15)))


# write function to find percetage of common uniqu letters between 2 strings

def commonstring(str1, str2):
    a = list(set(str1) & set(str2))
    print(a)
    print((len(a) / max(len(str1),len(str2)))*100)

commonstring('abc','cde')