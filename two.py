#variable:
#why variable is used
#to store a value in memory at runtime
#how to declare- 
#variable= value
#variable cannot start with a number ,symbols 
#start with a letter or underscore
a=5
print(a)

a=10
a=15 #python is a line by line execution,if you give 2a's the last value will be printed out and if there is any error in first line 
     # then they will not execute the rest of the code
print(a)

a=10
print(id(a))
a=15 
print(id(a))#instead of changing the first a's value python creates a new memory allocation and assigns there a
            #but in c they will change the value itself

#*python is case sensitive language, a and A are different variables
age=15
Age=20
AGE=25
print(Age)

#swap 2 numbers
a=3
b=7
a,b = b,a
print(a)
print(b) #not to be used in interview

a=5
b=6
c=a
a=b
b=c
print(a)
print(b)

#swap with operations
a=5
b=7
a=a+b #12
b=a-b #12-7=5
a=a-b #12-5=7
print(a)
print(b)

#operations
a=5
a=a+10 #a=5+10
print(a)