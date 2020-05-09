#Dictionary and Date & Time
'''41.Using calendar module perform following operations. 
a)print the 2016 calendar with space between months as 10 character.
b) How many leap days between the years 1980 to 2025. 
c) Check given year is leap year or not. 
d) print calendar of any specified month of the year 2016.'''
import calendar
print "calendar for year 2016 with space between months as 10 character is", calendar.calendar(2016,c=10)
print "Leap days between the years 1980 to 2025 are",calendar.leapdays(1980,2025),"days"
enterYear=int(input("enter the year to see if leap or not"))
if calendar.isleap(enterYear)==True:
  print "year",enterYear,"is a leap year"
else:
  print "year",enterYear,"is not a leap year"
enterMonth2016=int(input("Enter the month no of 2016 year to print it"))
print calendar.month(2016,enterMonth2016,w=2,l=1)





#Functions
'''42.Write a program to generate a Fibonacci series using a function called fib(n), a) where N is user specified argument specifies number of elements in the series.'''
def fib(nterms):
  "This generates a fibonacci series"
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
# Now you can call fib function
n=int(input("Enter the no of terms"))
fib(n)





#Functions
'''43.Write a program to search given element from the list. Use your own function to search an element from list. Note: Function should receive variable length arguments and search each of these arguments present in the list.'''
def find(n):
  "This finds element from the list"
  list1=input("Enter list elements")
  list1=list(list1)
  list1.sort()
  found=0
  for each in list1:
    if n==each:
      print "element",n,"is present in the list"
      found=1
      break
  if found==0:
    print "element",n,"is not presnt in the list"
number=input("enter element to check in the list")
find(number)





#Functions
'''44.Write a program with lambda function to perform following. 
a) Perform all the operations of basic calculator ( add, sub, multiply, divide, modulus, floor division ).'''

add=lambda arg1,arg2:arg1+arg2
sub=lambda arg1,arg2:arg1-arg2
mul=lambda arg1,arg2:arg1*arg2
div=lambda arg1,arg2:arg1/arg2
mod=lambda arg1,arg2:arg1%arg2
fdiv=lambda arg1,arg2:arg1//arg2


# Now call all the functions
print "Value as Sum:",add(30,20)
print "Value as Sub:",sub(20,10)
print "Value as Mul:",mul(20,10)
print "Value as Div:",div(20.0,12.0)
print "Value as Mod:",mod(20,10)
print "Value as Fdiv:",fdiv(20,3)





#Functions
'''45.Write a program to check given string is Palindrome or not. ( Use function Concepts and Required keyword, Default parameter concepts) That is reverse the given string and check whether it is same as original string, if so then it is palindrome. Example : String = "Malayalam" reverse string = "Malayalam" hence given string is palindrome.'''
def PalindromeCheckRequiredParam(myStr):
  'this checks for the palindrokme string'
  #myStr="Hello buddy"
  myStr=myStr.lower()
  myStr1=myStr[::-1]
  if myStr==myStr1:
    print "The given string",myStr,"is palindrome"
  else:
    print "The given string",myStr,"is not palindrome"
  return
#myStr=input("Enter the string")
PalindromeCheckRequiredParam("hello world")
PalindromeCheckRequiredParam("POP")

def PalindromeCheckDefaultParam(myStr="Malayalam"):
  'this checks for the palindrokme string'
  #myStr="Hello buddy"
  myStr=myStr.lower()
  myStr1=myStr[::-1]
  if myStr==myStr1:
    print "The given string",myStr,"is palindrome"
  else:
    print "The given string",myStr,"is not palindrome"
  return
#myStr=input("Enter the string")
PalindromeCheckDefaultParam("duud")
PalindromeCheckDefaultParam()







#Functions
'''46.Write a function to find the biggest of 4 numbers. 
a) All numbers are passed as arguments separately ( Required argument) 
b) use default values for arguments ( Default arguments)'''
def BiggestRequiredArg(a,b,c,d):
  'this checks for biggest of 4 nos'
  if a>b and a>c and a>d:
    print "a is the biggest"
  elif b>a and b>c and b>d:
    print "b is the biggest"
  elif c>a and c>b and c>d:
    print "c is the biggest"
  else:
    print "d is the biggest"
  return
BiggestRequiredArg(2,3,4,1)

def BiggestDefaultArg(a,b,c,d=8):
  'this checks for biggest of 4 nos'
  if a>b and a>c and a>d:
    print "a is the biggest"
  elif b>a and b>c and b>d:
    print "b is the biggest"
  elif c>a and c>b and c>d:
    print "c is the biggest"
  else:
    print "d is the biggest"
  return
BiggestDefaultArg(a=2,c=3,b=4)





#Functions
'''47.Write function to extend the tuple with elements of list. Pass list and Tuple as parameter to the function.'''
def Extnd(tup1,list1):
  'This extends the tuple with elements of list'
  tup1=list(tup1)
  result=tup1+list1
  print result
tupp=(1,2,3,4)
listt=[11,22,33,44]
Extnd(tupp,listt)





'''48.Create a Calculator with the following functions. 
a) Addition/subtraction/multiplication and division of two numbers ( Note: Create separate function for each operation ) 
b) Find square root of a given number.( Use keyword arguments in your function) 
c) Create a list of sub strings from a given string, such that sub strings are created with given character. That is, string = "Pack: My: Box: With: Good: Food" Create sub strings with the delimiter character ":" such that the following sub strings are created. substrlist=[Pack, My, Box, With, Good, Food] Note : Function should take at least 2 parameters ( Main string and delimiter character) return value from function will be list of substring.'''
import math
def Addition(a,b):
  'This adds the two nos'
  sum=a+b
  print "sum is",sum
def Subtraction(a,b):
  'This finds the difference of two nos'
  sub=a-b
  print "Subtraction is",sub
def Multiply(a,b):
  'This multiplies two nos'
  mul=a*b
  print "multiplication is",mul
def Division(a,b):
  'This divides the nos'
  div=a/b
  print "Division is",div
def Sqrt(num):
  'This finds the square root of a number'
  print "SQrt is ",math.sqrt(num)
Addition(3,5)
Subtraction(9,3)
Multiply(3,5)
Division(4,2)
Sqrt(9)
Sqrt(num=81)

def subStr(str,delcharctr):
  'This creates sub string from given string with the delimiter character :'
  subStr= str.split(delcharctr,6)
  print "Original String is",str
  return subStr
str="Pack:My:Box:With:Good:Food"
delcharctr=':'
subStr= subStr(str,delcharctr)
print "Substring from string is",subStr





#File I/O Operations
'''49.Write a program to perform following file operations 
a) Open the file in read mode and read all its contents on to STDOUT. 
b) Open the file in write mode and enter 5 new lines of strings in to the new file. 
c) Open file in Append mode and add 5 lines of text into it.'''
fo = open("firstFile.txt","r")
print "Read String is : ",fo.read()
fo.close()

fo=open("firstFile2.txt","w")
fo.writelines("so we have come to the end now\ni dont think this is\nyes very true\n still to go\n this is final now")
fo.close()


fo=open("firstFile2.txt","a")
fo.writelines("finally\nso we have come to the end now\n again and again\nsorry to keep you waiting\nFINAL ONE!!!!")
fo.close()





#File I/O Operations
'''50. Write a program to open the existing file in read mode and perform following tasks,
      a) Read 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
        b) Reset the file pointer after reading 100 Character from file ( Use Seek function to reset)
        c) Open the file in read mode and start printing the contents from 5th line onwards.'''
fo=open("file1.txt","r")
position=0
while(True):
    a=fo.read(10)
    if not a:
        break
    else:
        print a
        position+=10
        print "position=",position

fo=open("file1.txt","r")
position=0
while(position<100):
    a=fo.read(10)
    if not a:
        break
    else:
        print a
        position+=10
        print "position=",position        
fo.seek(0,0)
print fo.read(10)

fo=open("file1.txt","r")
for i in range(5):
    fo.readline()
for line in fo:	
	print "line=",line
fo.close()





'''51. In a given directory search all text files for the pattern "Treasure". 
a) Find how many text file has the pattern.
b) Count how many times pattern repeats in each file
Note : Create at least 4 text file in a directory and keep the pattern in at least 2 files.
       Repeat the pattern in the file many times.'''

import glob
totalCount = 0
for eachfile in glob.glob("*.txt"):
    myfile = open(eachfile, "r")
    list1 = myfile.read().split()
    if "Treasure" in list1:
        print "File name:",eachfile,"\nCount of letter Treasure in this file:", list1.count("Treasure")
        totalCount += list1.count("Treasure")
    else:
        print "File name:",eachfile,"\nCount of letter Treasure in this file:", 0
    myfile.close()        
print "Total counts of letter Treasure in all the files:", totalCount





'''52.Open existing text file and reverse its contents. i.e
a) print the last line as first line and first line as last line ( Reverse the lines of the file )
b) print characters of file from last character of file till the first character of the file.(Reverse entire contents of  file )

strlist=list()
for lines in reversed(open("file.txt").readlines()):
    print lines.rstrip()
    strlist.append(lines.rstrip())
    
    
for string in strlist:
    print string[::-1]
    
    
    
    
    
'''53. Open the file is read & write mode and apply following  functions
         a) All 13 functions mentioned in Tutorial File object table.'''
fo = open("file.txt", "r+")
print "Name of the file: ", fo.name
# Close opend file
fo.close()


fo = open("file.txt", "r")
print "Name of the file: ", fo.name
fo.flush()
fo.close()

fo = open("file.txt", "r+")
print "Name of the file: ", fo.name
fid = fo.fileno()
print "File Descriptor: ", fid
fo.close()

fo = open("file.txt", "r+")
print "Name of the file:", fo.name
ret = fo.isatty()
print "Return value : ", ret
fo.close()

fo = open("file.txt", "r+")
print "Name of the file: ", fo.name
for index in range(1):
   line = fo.next()
   print "Line No %d - %s" % (index, line)
fo.close()

fo = open("file.txt", "r+")
print "Name of the file: ", fo.name
line = fo.read(100)
print "Read Line: %s" % (line)
fo.close()

fo = open("file.txt", "r+")
print "Name of the file: ", fo.name
line = fo.readline()
print "Read Line: %s" % (line)
line = fo.readline(5)
print "Read Line: %s" % (line)
fo.close()

fo = open("file.txt", "r+")
print "Name of the file: ", fo.name
line = fo.readlines()
print "Read Line: %s" % (line)
line = fo.readlines(2)
print "Read Line: %s" % (line)
fo.close()

fo = open("file.txt", "rw+")
print "Name of the file: ", fo.name
line = fo.readline()
print "Read Line: %s" % (line)
# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print "Read Line: %s" % (line)
fo.close()

fo = open("file.txt", "rw+")
print "Name of the file: ", fo.name
line = fo.readline()
print "Read Line: %s" % (line)
# Get the current position of the file.
pos = fo.tell()
print "Current Position: %d" % (pos)
# Close opend file
fo.close()


fo = open("file.txt", "rw+")
print "Name of the file: ", fo.name
line = fo.readline()
print "Read Line: %s" % (line)
# Now truncate remaining file.
fo.truncate()
# Try to read file now
line = fo.readline()
print "Read Line: %s" % (line)
fo.close()

fo = open("file.txt", "rw+")
print "Name of the file: ", fo.name
str = "This is 6th line"
# Write a line at the end of the file.
#fo.seek(0, 1)
line = fo.write( str )
# Now read complete file from beginning.
fo.seek(0,0)
lines=fo.read()
print lines
fo.close()

fo = open("file.txt", "rw+")
print "Name of the file: ", fo.name
str = "This is 6th line"
# Write a line at the end of the file.
#fo.seek(0, 1)
line = fo.writelines( str )
# Now read complete file from beginning.
fo.seek(0,0)
lines=fo.read()
print lines
fo.close()





'''54. Write a program to handle the following exceptions in you program.
a) KeyboardInterrupt,
b) NameError 
c) ArithmeticError
Note : make use of  Try, except, else: statements.'''

import time
i=1
try:
    while(i<5):
        time.sleep(1)
        print i
        i+=1
except KeyboardInterrupt:
    print "KeyboardInterrupt"
    
    
try:
    name = input("Enter your name:")
    print "Good Morning "+ name
except NameError:#Enter your name in Quotes else NameError msg will appear
    print "NameError"



try:
    num= 0/0
except ArithmeticError:
    print "ArithmeticError"
    


 
 
 '''55. Write a program for converting weight from Pound to Kilo grams.
       a) Use assertion for the negative weight.
       b) Use assertion to weight more than 100 KG'''
       
def PoundToKg(pound):
  try:
    assert (pound>=0),"Negative weight not allowed"
    return pound*0.453592
  except AssertionError, exp:
    return exp
print PoundToKg(43)
print PoundToKg(-13)


def PoundToKg(pound):
  try:
    assert (pound>=100), "Weight should be more than or equal to 100"
    return pound*0.453592
  except AssertionError, exp:
    return exp
print PoundToKg(56)
print PoundToKg(101)





'''56.Write a program to handle following exceptions using Try block.
a) IO Error while you try writing contents into the file that is opened in read mode only.
b) ValueError'''

try:
    myfile =open("file.txt","r")
    print myfile.read()
    myfile.write("Hello")
except IOError:
    print "Writing mode is not allowed"

try:
    num = int(input("Enter value:"))
except ValueError:
    print "ValueError"

'''Output Extract:
Enter value:'trttr'
ValueError'''





'''57. From the Standard Exception Table of Tutorials: Try implementing all (25) exceptions in you program.
Note: Some exceptions might not work on your system.'''

import math
import sys
import time
#Exception
try:
    num=a/2
except Exception:
    print"Exception"

#Standard error
try:
    f0=open("file1.txt","r")
except StandardError:
    print "Standard error:No file exists"

#Arithmetic error
try:
    div=2/0
except ArithmeticError:
    print "Arithmetic error exception"

#StopIteration
try:
    fo=open('file.txt',"r")
    for i in range(1,10):
        print f.next()
except StopIteration:
    print "Stop Iteration Exception"
f.close()

#Systemexit
try:
    sys.exit()
except SystemExit:
    print "system exit exception"


#Overflow error
try:
    a=math.exp(4/42*349304332)
except OverflowError:
    print "Overflow error exception"

#Value error
try:
    a=math.sqrt(-32/3)
except ValueError:
    print "ValueError"

#Zero division error
try:
    a=2/0
except ZeroDivisionError:
    print "Zero Division exception"

#AssertionErrror
try:
    a=12
    assert (a>10),"assertion error"
except AssertionError:
    print "Assertion error"
    
#Attribute Error
try:
    raise AttributeError
except AttributeError:
    print "Attribute error"    

#EOF error
try:
    fo=open("file.txt","r")
    fo.read()
except EOFError:
    print "EOF error"

#import error
try:
    import dummy
except ImportError:
    print "Import error exception"

#look up error
dict = {'empid':'empname'}
try:
    print dict['abc']
except LookupError:
    print 'Lookup error'
    
#index error
try:
    list1=[12,13,14,45,34]
    print list1[9]
except IndexError:
    print "IndexOutofbound"

#name error:
try:
    print name
except NameError:
    print "Name Error"  
    
#keyboard interrupt
try:
    x=input()
    time.sleep(1)
except KeyboardInterrupt:
    print "Keyboard interrupt"

#KeyError
try:
    print dict['1']
except:
    print 'Key Error'

#Unbound Local Error
try:
    raise UnboundLocalError
except UnboundLocalError:
    print 'UnboundLocalError!'
#IOError
try:
    fo = open('file.txt',"r")
    fo.write('write hereafter')
except IOError:
    print 'IOError!'

#SyntaxError
try:
    raise SyntaxError
except SyntaxError:
    print 'Syntax Error !'

#TypeError
try:
    str ='hello'
    str = str-1
except TypeError:
    print 'Type Error'

#ValueError
try:
    str = 'hello'
    print int(str)
except ValueError:
    print 'Value Error'

#Runtime Error
try:
    raise RuntimeError
except RuntimeError:
    print 'Runtime Error occured !'





'''58.Create file called  "calc.py" which has following functions
i) functions to add 2 numbers
ii)  function to find diff of 2 numbers
iii) function to multiply 2 numbers
iv) all maths operations ( Sqrt, div, floor div, modulus, primnumber)
v) Fibonacci series
        
a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
b) Use From <module> import <function> statement to import only few function  from calc module.'''

#calc.py
import math

def add(a,b):
  'This adds 2 numbers'
  print "Sum of a and b is",a+b
    
def diff(a,b):
  'This finds the difference between 2 nos'
  print "Difference of a and b is",a-b
    
def multiply(a,b):
  'This multiplies 2 nos'
  print "Multiplication of a and b is",a*b

def div(a,b):
  'This divides 2 nos'
  print "Division of a and  b is",a/b
    
def sqroot(a):
    print "Square root of the number",a,"is", math.sqrt(a)
    
def floor_div(a,b):
    print "Floor division of a and b is", a//b
    
def fib(nterms):
  "This generates a fibonacci series"
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
n=int(input("Enter the no of terms"))
fib(n)

def isprime(num):
    for i in range(2,):
        if num%i==0:
            print num,"not prime"
            break
        else:
            print num,"is prime"
            break
number=int(raw_input())        
isprime(number)        

#math.py
from calc import*
add(4,5)
diff(34,12)
multiply(5,7)
div(6,2)
sqroot(9)
floor_div(33,5)
fib(8)
isprime(443)





'''59. Create file called  "stringop.py" which has following functions
i) functions to sort numbers( Use loops for  sorting, do not use built in function)
ii)  function to search given element through binary search method.
   ( Refer to net for the Binary search algorithm)
iii) function to reverse the given string
Write new program in file strpackage.py such that you import functions of file  "stringop.py" to your new program'''


#stringop.py
def sortNumbers(num):
  for i in range(len(num)-1):
    for j in range(len(num)-1):
      if num[j] > num[j+1]:
        temp = num[j]
        num[j] = num[j+1]
        num[j+1] = temp
  print "Sorted numbers:", num
    
def binarySearch(list1, item):
    list1.sort()
    first = 0
    last = len(list1)-1
    found = False
    
    while first<=last and not found:
        midpoint = (first+last)/2
        if list1[midpoint] == item:
            found = True
            return found
        else:
            if item < list1[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def reverselist(list2):
    print list2.reverse()
    print "reversed list :", list2

# strpackage.py
from stringop import*
sortNumbers([34,56,21,11,3])
print "binarySearch([22,33,44,12,34]):", binarySearch([22,33,44,12,34],22)
reverselist([11,22,12,10,32,13])