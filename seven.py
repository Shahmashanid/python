#list
#collection of elements
#a=[], represents
#properties 
#list can have any elements of any size
#data=[12,12,33,'mohan',55[45,56]]
#list are ordered
a=[1,2,3,4]
b=[4,3,2,1]
print(a==b) #if they have same elements a and b are not same
            #if oder is same than same
#List are indexed
#index start from zero
a=[11,12,13,14,15,16,17,18,19]
print(a[0])#index
#[start,stop,step]
print(a[1:4])#4th index will not print stops @3rd index
print(a[0:9:2])
print(a[:6])#starts from 0 runs till end
print(a[3:])#stats from 3 and runs till end
print(a[::-1])#stats from 0 and runs till end in reverse
#in string
name='mohan das gandhi'
print(a[::-1]) #space is also considered as element
#positive index start from 0,1,2,3....
#negitive index start from ...-3,-2,-1 not from zero
#applitude
a='mohan'
(a[-5])==(a[0]) 
print(a)#yes
#list are mutable(we can change)
#str are inmutable
#to change
a=[11,12,13,14,15]
a[0]='mohan'
print(a)
#list are dynamic(add,remove)
a=[11,12,13,14]
a[0:2]=[31,22,33,34]#from zero to 1 chance ayyitt new number will come
print(a)
#list are nested
a=[1,2,[100,200],4,5]
print(a[2])#100,200
print(a[2][0])#100

#in build methods
#to add elements
#append()
#add an element to the end of the list
a=[11,22,33,44]
a.append(100)#only one value can be added at a time
print(a)
#extent()
#can add no of elements at a time
#can add listilekk list innee
#can add string to list
a=[11,22,33,44]
a.extend('hari')
print(a)
a=[11,22,33,44]
a.extend([55,77,'hari'])
print(a)

#insert()
#insert(index,value)
a=[11,22,33,44]
a.insert(0,'mohan')
print(a) #['mohan', 11, 22, 33, 44]
#value is not getting removed here
#to remove elements
#remove()
a=[11,12,13,14,15,11,11,11]
a.remove(11)
print(a) #only first 11 will be removed
#pop()
#remove last element
a=[11,12,13,14,15,17,19,131]
a.pop()
a.pop()
print(a)
#remove last element if i give one pop
#pop(index)
a=[11,12,13,14,15,17,19,131]
a.pop(0)
print(a)

#tuple
#collection of elements
#a=(2,3,4,'mohan',657,76,9)
#ordered
#indexed
#immutable
#duplicate numbers can be added

#iteration
#str,list,tuple,set,dict iteration can be done
a=[11,12,13,14,15]
b="mohan das"
c=(100,200,300,400,500)
for i in a:
    print(i)

a=456789
count=0
while a>0:
    count=count+1
    a=a//10
print(count)

a='mohan'
for i in range(0,len(a)):
    print(i,a[i])

fruits=['apple','mango','orange','grape','pineapple','watermelon']
for i in range(0,len(fruits)):
    print(i,fruits[i])

#find vowels and their position in a string
name=input("enter your name")
for i in range(len(name)):
    if name[i]=='a'or name[i]=='e'or name[i]=='i' or name[i]=='u':
        print(i,name[i])
#or
name=input("enter your name")
vowel='aeiou'
for i in range(len(name)):
    if name[i] in 'aeiou':
        print(i,name[i])

#in operation or membership operation
b=[11,12,13,14,'mohan']
if 'mohan' in b:
    print('yes')

#create a list of even numbers and odd numbers from first 100 numbers
num=[]
even=[]
odd=[]
for i in range(1,101):
    num.


