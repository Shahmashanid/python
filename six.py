#control statment
#1.loop
#1a. while loop
#used for conditional based
#condition is always true or false
#if the condition is true it loops until gets false
#syntax= while condition:
            #code to be executed
i=1
while i<10:
    print(i)
    i=i+1

i=1
while i<=100:
    print(i)
    i=i+1
print("mohan")

#sum of first 10 numbers
i = 1
sum = 0
while i <= 10:
    sum=sum+i 
    i=i+1
print(sum)

#print even sum and odd sum  from first 100 numbers
i=1
esum=0
osum=0
while i<=100:
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
print(esum)
print(osum)

#1b. for loop
#iteration based
#syntex= for i in range():
 #range is an object
 #range(start,stop,step)step=how to print number

i=1
while i<=10:
    print(i)
    i+=1 #=1 act as step

for i in range(1,101,3):
    print(i)


for i in range(10,0,-1):
    print(i)

#find sum of 100 numbers
sum=0
for i in range(101):
    sum=sum+i
    print(sum)

#sum of digit in a number
num=8509
sum=0
while num>0:
    a=num%10 
    num=num//10
    sum=sum+a
print(sum)

#reverse of a number
num=786
rev=0
while num>0:
    a=num%10 
    num=num//10
    rev=rev*10+a
print(rev)

#factorial of a number
num=int(input('enter number-'))
fact=1
while num>0:  
    fact=fact*num
    num=num-1
print(fact) 

