#string
# means sequence of series/ collection of character
#it can be of alphabet,number,symbols
#represented in quots(',",''')
#if i give inside the quots even number it detect as string


name = "mohan"
print(name)
print(type(name))

data = "mohan's resume"
qt= '''gandhi once said that "say no to violence"'''
print(qt)

#escape sequance(to give propertices inside the string)
#\ is considered as quots here 
#instered of giving quots we can as use \ here

data = 'mohan\'s resume' # \' means '
print(data)

qt= "gandhi once said that \"say no to violence\"" # \" means "
print(qt)

qt= "gandhi once said \n that \"say no to violence\"" #\n means next line
print(qt)

qt= "gandhi on\tce said \n that \"say no to violence\"" #\t = tab space
print(qt)

qt= "gandhi\b once said \n that \"say no to violence\"" #\b = back space
print(qt)

qt= "gandhi\b once said \n that \"say no to violence\"" #\b = back space
print(qt)
qt= "gandhi\b once said \\n that \"say no to violence\"" #if i give \\ then it is read as string mean\n
print(qt)

#raw string
#give r infront of the content
qt= r"gandhi\b once said \n that \"say no to violence\""
print(qt) #use raw string to remove all the escape string without deleting 

#input function 
print()#print is used to give output to user
a= input("enter a number=")# a= input to give input in terminal
b= input("aenter a number=")#input() functions result wii be string
print(a+b)
#a=15 and b=33 ans=1533 not adding after giving a+b 
#what happens is string concantination where 2 num joins 
a= "mohan"
b="das"
print(a+' '+b)#give space

# a= "mohan"
# b=54
# print(a+b)#can only concatenate string to string not int to string

#type conversion/casting
#a. implicite(int or string is recognised by python itself)
#b. explicite(changing string to int,float ect...we are changing)
a="11"#its in string
b="10"
print(float(a)+int(b))#from str converted to float and int

a= float(input("enter a number="))#if i give float(input(.....) while a+b adding up not concatinate
b= int(input("enter a number="))
print(a+b)

#string format
#to convert different data into string
#f is used before content to convert to string
name= "mohan"
age= 29
married_status=False
rating=8.8
result=f'my name is {name}, my age is {age}, my married status is {married_status}, and rating is {rating}'
print(result)



