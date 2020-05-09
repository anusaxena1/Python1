
#Write a program to Add, Subtract, Multiply, and Divide 2 numbers
num1=20
num2=10
Add=num1+num2
Sub=num1-num2
Mul=num1*num2
Div=num1/num2
print ("Addition is",Add)
print ("Subtraction is",Sub)
print ("Multiplication is",Mul)
print ("Division is",Div)

#Basic Operator-Write a program to find the biggest of 3 numbers (Use If Condition)
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
num3=int(input("Enter 3rd number"))
if num1>num2 and num1>num3:
  print ("The biggest no is",num1)
elif num2>num1 and num2>num3:
  print ("The biggest no is",num2)
else:
  print("The biggest no is",num3)

#3.Write a program to find given number is odd or Even
num1=int(input("Enter the number"))
if num1%2==0 :
    print("The number",num1,"is even")
else :
    print("The number",num1,"is odd")

#Basic Operators
#4.Write a program to find the number is Prime or not.
num=int(input("Enter the number to check for prime"))
if num==1:
  print ("Number",num,"is not a prime number")
elif num>1:
  for i in range(2,num):
    if num%i==0:
      print ("Number",num," is not a prime number")
      break
  else:
    print ("Number",num,"is a prime number")





#5.Write a program to receive 5 command line arguments and print each argument separately. Example : >> python test.py arg1 arg2 arg3 arg4 arg5 a) From the above statement your program should receive arguments and print them each of them. b) Find the biggest of three numbers, where three numbers are passed as command line arguments.'''
#test.py
import sys
arg1,arg2,arg3,arg4,arg5=sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
print ("arg1=",arg1)
print ("arg2=",arg2)
print ("arg3=",arg3)
print ("arg4=",arg4)
print ("arg5=",arg5)

arg3,arg4,arg5=input("Enter 3 numbers")
if arg3>arg4 and arg3>arg5:
  print ("the biggest no is",arg3)
elif arg4>arg3 and arg4>arg5:
  print ("the biggest no is",arg4)
else:
  print("the biggest no is",arg5)





#Basic String operations
#6.Write a program to read string and print each character separately. 
#a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings. 
#b) Repeat the string 100 times using repeat operator * 
#c) Read strig 2 and concatenate with other string using + operator.
str1=input("Enter the string")#needs to give as "hello india" including the quotes
for character in str1:
  print character
str1=input("Enter the string")
str2=str1[1:-1]
print ("str2=",str2)
print ("str1=",str1)
print ("str1*100 times=",str1*100)
str3=str1+" hello India"
print ("str3 =",str3)





#Basic List operations
#7.Create a list with at least 10 elements in it 
  #print all elements 
  #perform slicing 
  #perform repetition with * operator 
  #Perform concatenation wiht other list.
str1=input("Enter the list1")
list1=list(str1)
print ("list1=",list1)
list2=list(input("Enter list2 elements"))
print ("list2=",list2)
print ("list1[1:3]=",list1[1:3])
print ("list2[3:-3]=",list2[3:-3])
print ("list1*2=",list1*2)
print ("list1+list2=",list1+list2)





#Basic tuple operations
#8.Create a tuple with at least 10 elements in it 
  #print all elements 
  #perform slicing 
  #perform repetition with * operator 
  #Perform concatenation wiht other list.
str1=input("Enter the tuple elements")
tuple1=tuple(str1)
print ("tuple1=",tuple1)
print ("tuple1[1:3]=",tuple1[1:3])
print ("tuple1[3:-3]=",tuple1[3:-3])
print ("tuple1*2=",tuple1*2)
print ("tuple1+(1,2,3,4,5)=",tuple1+(1,2,3,4,5))





#Python Numbers
#9.Write program to Add , subtract, multiply, divide 2 complex numbers.
import math
a=2+2j
b=3+3j
print ("Addition of two complex numbers :",a+b)
print ("Subtraction of two complex numbers :",a-b)
print ("Multiplication of two complex numbers :",a*b)
print ("Division of two complex numbers :",a/b)





#Assignment Operator
#10.Using assignment operators, perform following operations Addition, Substation, Multiplication, Division, Modulus, Exponent and Floor division operations
import math
a=3.2
b=4.6
add=a+b
sub=b-a
mul=a*b
div=b/a
mod=a%b
exp1=a**b
flordiv=b//a
print "addition is \n",add
print "subtraction is \n",sub
print "multiplication is \n",mul
print "division is \n",div
print "modulus is \n",mod
print "exponent is \n",exp1
print "floor division is \n",flordiv





#Bitwise Operator
#11.Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.
import math
a = 10            
b = 20             
c = a & b;       
print "Value of c (a&b) is ", c
c = a | b;         
print "Value of c (a|b) is ", c
c = a ^ b;        
print "Value of c (a^b) is ", c
c = ~a;           
print "Value of c (~a) is ", c
c = a << 2;       
print "Value of c (a<<2) is ", c
c = a >> 2;       
print "Value of c (a>>2) is ", c





#comparison operator
#12.Read 10 numbers from user and find the average of all. a) Use comparison operator to check how many numbers are less than average and print them b) Check how many numbers are more than average. c) How many are equal to average.
a,b,c,d,e,f,g,h,i,j=(input("Enter 10 numbers"))
avg=(a+b+c+d+e+f+g+h+i+j)/10
countBig=0
countSmall=0
countEqual=0
print "Average of the 10 nos is =",avg
print "Numbers smaller than the Average are below:"
if a<avg:
    print "a=",a
    countSmall+=1
elif a>avg:
    #print "a=",a, "is bigger than avg=",avg
    countBig+=1
else:
    #print "a=",a, "is equal to avg=",avg
    countEqual+=1
    
if b<avg:
    print "b=",b
    countSmall+=1
elif b>avg:
    #print "b=",b, "is bigger than avg=",avg
    countBig+=1
else:
    #print "b=",b, "is equal to avg=",avg
    countEqual+=1
    
if c<avg:
    print "c=",c
    countSmall+=1
elif c>avg:
    #print "c=",c, "is bigger than avg=",avg
    countBig+=1
else:
    #print "c=",c, "is equal to avg=",avg
    countEqual+=1
    
if d<avg:
    print "d=",d
    countSmall+=1
elif d>avg:
    #print "d=",d, "is bigger than avg=",avg
    countBig+=1
else:
    #print "d=",d, "is equal to avg=",avg
    countEqual+=1
    
if e<avg:
    print "e=",e
    countSmall+=1
elif e>avg:
    #print "e=",e, "is bigger than avg=",avg
    countBig+=1
else:
    #print "e=",e, "is equal to avg=",avg
    countEqual+=1
    
if f<avg:
    print "f=",f
    countSmall+=1
elif f>avg:
    #print "f=",f, "is bigger than avg=",avg
    countBig+=1
else:
    #print "f=",f, "is equal to avg=",avg
    countEqual+=1
    
if g<avg:
    print "g=",g
    countSmall+=1
elif g>avg:
    #print "g=",g, "is bigger than avg=",avg
    countBig+=1
else:
    #print "g=",g, "is equal to avg=",avg
    countEqual+=1
    
if h<avg:
    print "h=",h
    countSmall+=1
elif h>avg:
    #print "h=",h, "is bigger than avg=",avg
    countBig+=1
else:
    #print "h=",h, "is equal to avg=",avg
    countEqual+=1
    
if i<avg:
    print "i=",i
    countSmall+=1
elif i>avg:
    #print "i=",i, "is bigger than avg=",avg
    countBig+=1
else:
    #print "i=",i, "is equal to avg=",avg
    countEqual+=1
    
if j<avg:
    print "j=",j
    countSmall+=1
elif j>avg:
    #print "j=",j, "is bigger than avg=",avg
    countBig+=1
else:
    #print "j=",j, "is equal to avg=",avg
    countEqual+=1    
print "the total count of nos bigger than average is ",countBig
print "the total count of nos smaller than average is=",countSmall
print("the total count of nos equal to the average is=",countEqual





#Decision making (IF .. Else structure)
#13.Write a program to find the biggest of 4 numbers. a) Read 4 numbers from user using Input statement. b) extend the above program to find the biggest of 5 numbers. ( PS : Use IF and IF & Else , If and ELIf, and Nested IF )
a,b,c,d=(input("Enter the numbers:"))
greatest=0
if (a>b)&(a>c)&(a>d):
    print("the greatest no of the first 4 is",a
    greatest=a
elif (b>a)&(b>c)&(b>d):
    print("the greatest no of the first 4 is",b
    greatest=b
elif (c>a)&(c>b)&(c>d):
    print("the greatest no of the first 4 is",c
    greatest=c
else:
    print("the greatest no of the first 4 is",d
    greatest=d
e=int(input("Enter 5th number"))

if(e>greatest):
    print(" The biggest of all 5 nos is",e





#Python List functions and Methods
'''14.Write a program to create two list A and B such that List A contains Employee Id, List B contains Employee name ( minimum 10 entries in each list ) and perform following operations 
a) Print all names on to screen 
b) Read the index from the user and print the corresponding name from both list. 
c) Print the names from 4th position to 9th position 
d) Print all names from 3rd position till end of the list 
e) Repeat list elements by specified number of times ( N- times, where N is entered by user) 
f) Concatenate two lists and print the output. 
g) Print element of list A and B side by side.( i.e. List-A First element , List-B First element )'''
listEId=[1,2,3,4,5,6,7,8,9,10]
listEName=['Rohit','Dhawan','Kohli','Rahane','Manish','Dhoni','Hardik','Chahal','Bhuvi','Bumrah']
print listEName
index=int(input("Enter the index to read from"))
print listEName[index]
print listEId[index]
print listEName[3:-1]
print listEName[2:]
ntime=int(input("enter the no of times you wish to repeat the list"))
print listEId*ntime
print listEName*ntime
concatList=listEId+listEName
print concatList
for element in range(len(listEId)):
  print "ListEid element",listEId[element],"listEName elements",listEName[element]





#Python List functions and Methods
'''15.Create a list of 5 names and check given name exist in the List.
a) Use membership operator ( IN ) to check the presence of an element. 
b) Perform above task without using membership operator. 
c) Print the elements of the list in reverse direction.'''

#a) Use membership operator ( IN ) to check the presence of an element. 
list1=['Ram','Ravi','Raj','Rakesh','Ravish']
#print list1
if ('Ravi') in list1:
  print("Ravi is present in the list"
else:
  print("Ravi is not present in the list"

#b) Perform above task without using membership operator. 
for i in list1:
  if (i=='Ravi'):
    print("Ravi is present in the list"
    break
else:
    print("Ravi is not present in the list"

#c) Print the elements of the list in reverse direction.
list1.reverse()
print("the elements of list1 in reverse direction are",list1





#Python Numbers
'''16.i) Check whether given number is prime or not.
ii) Generate all the prime numbers between 1 to N where N is given number.'''
num=int(input("Enter the number to check for prime"))
if num==1:
  print "Number",num,"is not a prime number"
elif num>1:
  for i in range(2,num):
    if num%i==0:
      print "Number",num," is not a prime number"
      break
  else:
    print "Number",num,"is a prime number"
upper=int(input("Enter the no till which you need to print the prime numbers"))
print "The prime numbers between the given range is"
for num in range(2,upper+1):
  if num>1:
    for i in range(2,num):
      if(num%i)==0:
        break
    else:
      print num





#Decision making (IF .. Else structure)
'''17.Write program to find the biggest and Smallest of N numbers. 
PS: Use the functions to find biggest and smallest numbers.'''
num=list(input("Enters numbers again"))#either enter as ['1','21','23']or 1,23,45,65
biggest=max(num)
smallest=min(num)
print "Maximum is",biggest
print "Minimum is",smallest





#Looping structures
'''18.Using loop structures print numbers from 1 to 100. and using the same loop print numbers from 100 to 1.( reverse printing) a) By using For loop b) By using while loop c) Let mystring ="Hello world" print each character of mystring in to separate line using appropriate loop structure.'''
print "Printing 1 to 100 using for loop"
list1=[]
for i in range(1,101):
  print i
  list1.append(i)
list1.reverse()
print "\nNumbers 1 to 100 in reverse order using the same for loop",list1

list2=[]
i=1
print "\nPrinting 1 to 100 using while loop"
while i<=100:
  print i
  list2.append(i)
  i+=1
list2.reverse()
print("\nNumbers 1 to 100 in reverse order using the same while loop",list2

mystring='Hello world'
print '\nPrinting each character of string Hello world in separate line'
for each in mystring:
  print each





#Looping Structures
'''19.Using loop structures print even numbers between 1 to 100. 
a) By using For loop , use continue/ break/ pass statement to skip odd numbers.
i) break the loop if the value is 50 
ii) Use continue for the values 10,20,30,40,50

b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
i) break the loop if the value is 90 
ii) Use continue for the values 60,70,80,90'''

#Using for loop structure to print even numbers between 1 to 100
print "The even numbers from 1 to 100 using for loop is below:" 
for i in range(1,101):
  if i%2==0:
    print i
print "\n\n"


#.a) By using For loop , use continue/ break/ pass statement to skip odd numbers.
print "The numbers from 1 to 100 skipping odd numbers using for loop is below:" 
for i in range (1,101):
  if i%2!=0:
    continue
  print i
print "\n\n"


#.i) break the loop if the value is 50 
print "Breaking the for loop i ==50"
for i in range(1,101):
    if i==50:
      break
    print i
print "\n\n"    


#.ii) Use continue for the values 10,20,30,40,50
print "using continue for the values 10,20,30,40,50"    
for i in range (1,101):
  if i==10 or i==20 or i==30 or i==40 or i==50:
    continue
  print i
print "\n"    



#Using while loop structure to print even numbers between 1 to 100
print "The even numbers from 1 to 100 using while loop is below:" 
i=1
while i<=100:
  if i%2==0:
    print i
  i+=1
print "\n\n"


#.a) By using while loop , use continue/ break/ pass statement to skip odd numbers.
print "The numbers from 1 to 100 skipping odd numbers using while loop is below:" 
i=1
while i<=100:
  if i%2!=0:
    i+=1
    continue
  print i
  i+=1
print "\n\n"


#.i) break the loop if the value is 50 
print "Breaking the for loop i ==50"
i=1
while i<=100:
  if i==50:
    break
  print i
  i=i+1    


#.ii) Use continue for the values 10,20,30,40,50
print "using continue for the values 10,20,30,40,50"    
i=1
while i<=100:
  if i==10 or i==20 or i==30 or i==40 or i==50:
    i=i+1
    continue
  print i
  i=i+1
print "\n"

  



#Looping Structures 20.Write a program to generate Fibonacci series of numbers. Starting numbers are 0 and 1, new number in the series is generated by adding previous two numbers in the series. Example : 0, 1, 1, 2, 3, 5, 8,13,21,..... a) Number of elements printed in the series should be N numbers, Where N is any +ve integer. b) Generate the series until the element in the series is less than Max number.'''
nterms=int(input("Enter the no of terms"))
a=0 
b=1
if nterms<=0:
  print("please enter positive number")
elif nterms==1:
  print("Fibonacci series:",a)
elif nterms==2:
  print a
  print b
else:
  print a
  print b
  while(nterms>2):
    numnext=a+b
    print numnext
    a=b
    b=numnext
    nterms=nterms-1