#2. comparision operators:==,!=,>,<,>=,<=
#to compare value
#this is in boolean form, if  condition is true will give true and if  condition is false will give false

#a.equal to ==
a=7
b=9
print(a==b)#false
a=7
b=7
print(a==b)

#b.not equal to !=
a=7
b=7
print(a!=b)

#c.greater than >
a=7
b=9
print(a>b)

#d.less than <
a=1
b=9
print(a<b)

#e.greater than or equal to >=
a=9
b=10
print(a>=b)
a=2
b=2
print(a>=b)

#f.less than or equal to <=
a=3
b=4
print(a<=b)

#conditional statements:
#conditinal is either true or false
#if true executes, if not give else 

#if 
age=15
if age>=18:
    print("eligible ")
else:
    print("not eligible")

#check if a number odd or even
num=95
if num%2==0:
    print('even')
else:
    print('odd')

#check if a number is multiple of 5
num=55
if num%5==0:
    print('multiple of 5')
else:
    print('not a multiple of 5')

#check if a number is largest of 2 number
a=5
b=7
if a>b:
    print('a is larger')
else:
    print('b is larger')

#elif (multiple condition)
#elif means or not 
#which means if the condition is false then only elseif works
mark=40
if mark > 70:
    print('B+')
elif mark > 60:
    print('B')
elif mark > 40:
    print('c+')
elif mark > 30:
    print('c')
else:
    print('FAIL')

#check if a number is positive, negitive or zero
num=-567
if num>0:
    print('positive')
elif num<0:
    print('negitive')
else:
    print('zero')


#3. logical operators: and,or,not
#to connect multiple conditions
#a. and
# true and true = true
# true and false = false
# false and true = false
# false and false = false
a=7 
b=5
if a>5 and b==5:
    print('yes')


#b. or (if one condition is true then the or will give true)
# true or true = true
# true or false = true
# false or true = true
# false or false = false
a=7 
b=5
if (a>1 or b==3) and (a==6 or b==5):
    print('yes')
else:
    print('not')

#c.not=
# != and not= are not same 
# this is used to make true condition to false and false to true
a= 10
print(not a ==10)

#largest of 3 numbers
a=10
b=11
c=-100
if a>b and a>c:
    print('a is larger')
elif b>a and b>c:
    print('b is larger')
else:
    print('c is larger')

#check if a number is multiple of 3 and 5
num=95
if num%3==0 and num%5==0:
    print('mulfiple of 3 and 5')
else:
    print('not a multiple of 3 and 5')
 
    

