#Math and Random Modules
'''21.Using the built in functions on Numbers perform following operations 
a) Round of the given floating point number example : n=0.543 then round it next decimal number , i.e n=1.0 Use round() function 
b) Find out the square root of a given number. ( use sqrt(x) function) 
c) Generate random number between 0, and 1 ( use random() function) 
d) Generate random number between 10 and 500. ( use uniform() function) 
e) Explore all Math and Random module functions on a given number/ List. ( Refer to tutorial for Math & Random functions list)'''
import math
import random
num1=0.543
print "The round off to next decimal for",num1,"is",round(num1,0)
num2=990
print "The sqrt of number",num2,"is",math.sqrt(num2)
print "A random number between 0 and 1 using random function is",random.random()
print "A random number between 10 and 500 using uniform function is",random.uniform(10,500)

print "BELOW STARTS FOR MATH FUNCTIONS LIST"
print "abs(-1.8)=",abs(-1.8)
print"\nceil(1.3)=",math.ceil(1.3)
print"ceil(-1.3)=",math.ceil(-1.3)
print "ceil(1.6)=",math.ceil(1.6)
print "ceil(-1.6)=",math.ceil(-1.6)
print "\ncmp(3,4)=",cmp(3,4)
print "cmp(10,4)=",cmp(10,4)
print "cmp(4,4)=",cmp(4,4)
print "\nexp(2)=",math.exp(2)
print "\nfabs(-1.4)=",math.fabs(-1.4)
print "\nfloor(1.6)=",math.floor(1.6)
print "floor(-1.6)=",math.floor(-1.6)
print "floor(1.2)=",math.floor(1.2)
print "floor(-1.2)=",math.floor(-1.2)
print "\nlog(2)=",math.log(2)
print "\nlog10(2)=",math.log10(2)
print "\nmax(2,34,55,56)=",max(2,34,55,56)
print "\nmin(2,34,55,56)=",min(2,34,55,56)
print "\nmodf(100.233444)=",math.modf(100.233444)
print "math.modf(math.pi)=",math.modf(math.pi)
print "\npow(2,3) i.e 2**3=",pow(2,3)
print "\nround(80.23456, 2)=",round(80.23456, 2)
print "round(100.000056, 3)=",round(100.000056, 3)
print "round(-100.000056, 3)=",round(-100.000056, 3)
print "\nSqrt(3)=",math.sqrt(3)
print "\nBELOW STARTS FOR RANDOM FUNCTIONS LIST"
print "choice([1, 2, 3, 5, 9])=",random.choice([1, 2, 3, 5, 9])
print "choice('A String')=",random.choice('A String')
print "\nPrinting a number where start=100,end=1000,step=2"
print "randrange(100, 1000, 2) =",random.randrange(100, 1000, 2)
print "\nPrinting a number where start=100,end=1000,step=3"
print "randrange(100, 1000, 3)=",random.randrange(100, 1000, 3)
print "\nFirst random number=",random.random()
print "Second random number=",random.random()
random.seed( 10 )
print "Random number with seed 10=",random.random()
# It will generate same random number
random.seed( 10 )
print "Random number with seed 10=",random.random()
print "Random number",random.random()
print "Random number",random.random()
print "Random number",random.random()
list = [2, 13, 133, 51,'A'];
random.shuffle(list)
print "\nReshuffled list=",list
random.shuffle(list)
print "Reshuffled list=",list
print "\nRandom Float uniform(2,14)=",random.uniform(2,14)
print "Random Float uniform(4,11)=",random.uniform(4,11)





#Math- Trigonometric functions
'''22.Read the value x and y from the user and apply all trigonometric functions on these numbers. Note : Refer the tutorial Trigonometric operation table.'''
import math
x=float(input("Enter value of x"))
y=float(input("Enter value of y"))
print "acos(x)=",math.acos(x)
print "asin(x)=",math.asin(x)
print "atan(x)=",math.atan(x)
print "atan2(y,x)=",math.atan2(y,x)
print "cos(x)=",math.cos(x)
print "hypot(x,y)=",math.hypot(x,y)
print "sin(x)=",math.sin(x)
print "tan(x)=",math.tan(x)
print "degrees(x)=",math.degrees(x)
print "radians(x)=",math.radians(x)





#Math – math.pi application
'''23.Find the area of Circle given that radius of a circle. ( Use pi value from Math module)'''
import math
radius=int(input("Enter value of radius"))
area=math.pi*radius*radius
print "The area of circle is",area,"sqmeters"





#Strings
'''24.Special Characters: Write program to explore all Escape characters specified in Tutorial ( Under String chapter)'''
print "\a=\a"
print "\b"
print "\cx"
print"\C-x"
print "\e"
print "\f"
print"\M-\C-x"
print "\n"
print "\nnn"
print "\r"
print "\s"
print "\t"
print "\v"
#print "\x"
#print "\xnn"





#Strings
'''25.Write a program to print the different data types( Numbers, strings characters) using the Format symbols ( Refer to different format symbols specified in Tutorial )'''
print "My name is %s and weight is %d kg!" % ('Zara', 21)
print "my name is %c (example for for character)"%('A')
print "My name is %s (example for string conversion)"%('Rahul')
print "the no is %i (signed decimal integer)"%(-2)
print "the no is %d (signed decimal integer)"%(2)
print "the no is %u (unsigned decimal integer)"%(-2)
print "octal integer for 21 is %o"%(21)
print "hexadecimal integer (lowercase letters) of 21 is %x"%(21)
print "hexadecimal integer (uppercase letters) of 21 is %X"%(21)
print "exponential notation (with lowercase 'e') of 21 is %e"%(21)
print "exponential notation (with UPPERcase 'E') of 21 is %E"%(21)
print "floating point real number is %f"%23
print "%g"%21
print "%G"%21





#Strings
'''26.Receive the encoded string from your friend and decode it to check the original message. PS: You will receive Encoded string and the Algorithm used for encoding.'''
encStr = "dGhpcyBpcyB0byBjaGVjayBmb3IgZW5jb2RlIGFuZCBkZWNvZGU="
decStr = encStr.decode('base64','strict')
print "Encoded String: " + encStr
print "Decoded String: " + decStr





#Strings
'''27.Write a program to check given string is Palindrome or not. That is reverse the given string and check whether it is same as original string, if so then it is palindrome. Example : String = "malayalam" reverse string = "malayalam" hence given string is palindrome. Use built functions to check given string is palindrome or not.'''
myStr=input("Enter the string")
#myStr="Hello buddy"
myStr1=myStr[::-1]
if myStr==myStr1:
  print "The given string",myStr,"is palindrome"
else:
  print "The given string",myStr,"is not palindrome"





#Strings
'''28.Write a program to check how many ovals present in the given string. That is, count the number of " a e i o u" in the given string and print the numbers against each oval. Example :- "This is Python" Number of total ovals = 3 i = 2 o =1'''
myStr=input("Enter the string")
myStr=myStr.lower()
list1=list(myStr)
print myStr
count=0 
countA=0 
countE=0 
countI=0 
countO=0 
countU=0
for i in list1:
  if i=='a':
    count+=1
    countA+=1
  elif i=='e':
    count+=1
    countE+=1
  elif i=='i':
    count+=1
    countI+=1
  elif i=='o':
    count+=1
    countO+=1
  elif i=='u':
    count+=1
    countU+=1
print"No of total vowels=",count
print "count of A",countA
print "count of E",countE
print "count of I",countI
print "count of O",countO
print "count of U",countU





#Strings
'''29.Apply all built in functions on Strings in your program. Note there are 40 string functions. Use Tutorial for the help. Note: Each program should have 5 string built in functions ( so write 8 programs to cover all string functions)'''
#1.First 5 string built-in functions
str = "this is a string"
print "str.capitalize():",str.capitalize()

print "str.center(60,'x'):",str.center(60,'x')

sub = "i";
print "str.count(sub,1,30):",str.count(sub,1,30)
sub = "wow";
print "str.count(sub):",str.count(sub)

str = str.encode('base64','strict')
print "Encoded String:",str
print "Decoded String:",str.decode('base64','strict'),'\n'



#2.Second 5 string built in functions
str = "this is a string"
suffix = "ing"
print "str.endswith(suffix):",str.endswith(suffix)
print "str.endswith(suffix,10):",str.endswith(suffix,10)
suffix = "i"
print "str.endswith(suffix, 1, 4):",str.endswith(suffix, 1, 4)
print "str.endswith(suffix, 2, 6):",str.endswith(suffix, 2, 6)

print "\nOriginal string:",str
print "Default exapanded tab:",str.expandtabs()
print "Double exapanded tab:",str.expandtabs(16)

str2 = "ng"
print "\nstr.find(str2):",str.find(str2)
print "str.find(str2, 10):",str.find(str2, 10)
print "str.find(str2, 40):",str.find(str2, 40)

print "\nstr.index(str2):",str.index(str2)
print "str.index(str2, 10):",str.index(str2, 10)
#print "str.index(str2, 40):",str.index(str2, 40)

str = "this2009"
print "\nstr.isalnum():",str.isalnum()
str = "this is a string";
print "str.isalnum():",str.isalnum()



#3.Third set of 5 string built in functions
str = "this";  # No space & digit in this string
print "\nstr.isalpha():",str.isalpha()
str = "this is string example";
print "str.isalpha():",str.isalpha()

str = "123456";  # Only digit in this string
print "\nstr.isdigit():",str.isdigit()

str = "this is string example..";
print "\nstr.isdigit():",str.isdigit()

str = "THIS is string example"; 
print "\nstr.islower():",str.islower()
str = "this is string example";
print "str.islower()",str.islower()

str = u"this2009";  # u stands for Unicode.One must prefix u to check for isnumeric
print "\nstr.isnumeric():",str.isnumeric()
str = u"23443434";
print "str.isnumeric():",str.isnumeric()

str = "       "; 
print "\nstr.isspace():",str.isspace()
str = "This is string example";
print "str.isspace():",str.isspace()



#4.Fourth set of 5 string built in functions
str = "This Is String Example";
print "\nstr.istitle():",str.istitle()
str = "This is string example";
print "str.istitle():",str.istitle()

str = "THIS IS STRING EXAMPLE"; 
print "\nstr.isupper():",str.isupper()
str = "THIS is string example";
print "str.isupper():",str.isupper()

s = "-";
seq = ('a','b','c'); # This is sequence of strings.
print "\ns.join(seq):",s.join(seq)

str = "this is string example";
print "\nLength of the string:",len(str)

print "\nstr.ljust(50, '1')",str.ljust(50, '1')



#5.Fifth set of 5 string built in functions
str = "THIS IS STRING EXAMPLE";
print "\nstr.lower():",str.lower()

str = "     this is string example    ";
print "\nstr.lstrip():",str.lstrip()
str = "88888888this is string example8888888";
print "\nstr.lstrip('8'):",str.lstrip('8')

from string import maketrans   # Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!"
print "\nstr.translate(trantab):",str.translate(trantab)

str = "this is really a  frozen string example";
print "\nMax character: ",max(str)
str = "this is a string example";
print "Max character: ",max(str)

str = "this-is-real-string!example";
print "\nMin character: " + min(str)
str = "this-is-a-string-example";
print "Min character: " + min(str)



#6.Sixth set of 5 string built in functions
str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)

str1 = "this is really a string example....wow!!!";
str2 = "is";
print str1.rfind(str2)
print str1.rfind(str2, 0, 10)
print str1.rfind(str2, 10, 0)
print str1.find(str2)
print str1.find(str2, 0, 10)
print str1.find(str2, 10, 0)

str1 = "this is string example....wow!!!";
str2 = "is";
print str1.rindex(str2)
print str1.index(str2)

str = "this is string example....wow!!!";
print str.rjust(50, '0')

str = "     this is string example....wow!!!     ";
print str.rstrip()
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8')



#7.Seventh set of 5 string built in functions
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 1 )

str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print str.splitlines( )
print str.splitlines( 0 )
print str.splitlines( 3 )
print str.splitlines( 4 )
print str.splitlines( 5 )

str = "this is string example....wow!!!";
print str.startswith( 'this' )
print str.startswith( 'is', 2, 4 )
print str.startswith( 'this', 2, 4 )

str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' )

str = "this is string example....wow!!!";
print str.swapcase()
str = "THIS IS STRING EXAMPLE....WOW!!!";
print str.swapcase()



#8.Eighth set of 5 string built in functions
str = "this is string example!!!";
print "\nstr.title():",str.title()

from string import maketrans   # Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example";
print str.translate(trantab)

str = "this is string example";
print "\nstr.capitalize():",str.upper()

str = "this is string example";
print "\nstr.zfill(40):",str.zfill(40)
print "str.zfill(50):",str.zfill(50)

str = u"this2009";  
print "\nstr.isdecimal():",str.isdecimal()
str = u"23443434";
print "str.isdecimal():",str.isdecimal()





#Strings
'''30.Write a program to Sort given N numbers ( Use only loop structures and Conditions to sort the elements. Use Bubble sort / Selection sort technique to sort the elements of List) Note : don't use built in functions to sort.'''
str1=input("Enter the numbers")
list1=list(str1)
for each in range(len(list1)):
  swap=False
  i = 0
  while i<len(list1)-1:
    if list1[i]>list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i]
      swap = True
    i = i+1
  if swap == False:
    break
print (list1)





#Strings
'''31.Write a program to search an element in the list. i.e. Perform the binary search on the sorted list having integers as elements. If the search is successful print "Success" else print "un successful search".'''
str1=input("Enter the numbers")
list1=list(str1)
list1.sort()
print "The sorted order list1 of elements is",list1
searchElement=int(input("Enter the element tosearch from the above list"))
found=0
for each in list1:
  if each==searchElement:
    print "Successful"
    found=1
    break
if found==0:
  print "Unsuccessful search"
  
  



#Lists
'''32.Write a program to perform following operations on List. 
Create 3 lists List1,List2 and List3 
a. Find the length of each list and print it 
b. Find the maximum and minimum element of each list 
c. Compare each list and determine which list is biggest & which list is smallest. 
d. Delete first and last element of each list and print list contents.'''
list1=[1,2,3,4,5,6,7]
list2=['a','b','c','d','e']
list3=['abc','def','edd']
print list1
print list2
print list3
print "Length of list1=",len(list1)
print "Length of list2=",len(list2)
print "Length of list3=",len(list3)
print "Max of list1=",max(list1)
print "Min of list1=",min(list1)
print "Max of list2=",max(list2)
print "Min of list2=",min(list2)
print "Max of list3=",max(list3)
print "Min of list3=",min(list3)
if list1>list2 and list1>list3:
  print "\nlist1 is the biggest",list1
elif list2>list1 and list2>list3:
  print "\nlist2 is the biggest",list2
else:
  print "\nlist3 is the biggest",list3
  
if list1<list2 and list1<list3:
  print "\nlist1 is the smallest",list1
elif list2<list1 and list2<list3:
  print "\nlist2 is the smallest",list2
else:
  print "\nlist3 is the smallest",list3

print "\nList1 before removing 1st and last element using Pop method"
print list1
print "\nList1 after removing 1st and last element using pop method"
list1.pop(0);list1.pop(-1)
print list1
print "List2 before removing 1st and last element using Pop method"
print list2
print "List2 after removing 1st and last element using pop method"
list2.pop(0);list2.pop(-1)
print list2
print "List3 before removing 1st and last element using Pop method"
print list3
print "List3 after removing 1st and last element using pop method"
list3.pop(0);list3.pop(-1)
print list3





#Lists
'''33.Create a list with 7 elements and perform following operations. 
Let List=[10,20,30,40,50,60,70] 
a) Append an object 80 to the List 
b) insert object 100 at 4th position 
c) Sort the list and print all elements 
d) Sort the elements of the list in descending order. 
e) delete last three elements using pop operation'''
List=[10,20,30,40,50,60,70]
print List
List.append(80)
print "The Appended list is",List
List.insert(3,100)
print "The list after inserting 100 at 4th position is",List
List.sort()
print "List after sorting is",List
List.reverse()
print "The list in descending order",List
List.pop()
List.pop()
List.pop()
print "List after removing last 3 elements",List





#Lists
'''34.Create 3 Lists ( list1,list2,list3) with numbers and perform following operations 
a) Create Maxlist by taking 2 maximum elements from each list. 
b) Find average value from all the elements of Maxlist.
c) Create a MinlIst by taking 2 minimum elements from each list 
d) Find the average value from all the elements of Minlist'''
list1=[1,32,12,23,45]
list2=[45,21,2,35,56,33]
list3=[22,32,43,12,66]
list1.sort()
list2.sort()
list3.sort()
print "list1=",list1
print "list2=",list2
print "list3=",list3
Maxlist1=list1[-2:]
print "Maxlist1=",Maxlist1
Minlist1=list1[:2]
print "Minlist1=",Minlist1
Maxlist2=list2[-2:]
print "Maxlist2=",Maxlist2
Minlist2=list2[:2]
print "Minlist2=",Minlist2
Maxlist3=list3[-2:]
print "Maxlist3=",Maxlist3
Minlist3=list3[:2]
print "Minlist3=",Minlist3
Maxlist=Maxlist1+Maxlist2+Maxlist3
print "The Maxlist taking 2 maximum elements from each list is",Maxlist
Minlist=Minlist1+Minlist2+Minlist3
print "The Minlist taking 2 minimum elements from each list is",Minlist
sumMax=0
for each in Maxlist:
  sumMax+=each
print sumMax
SumMaxAvg=float(sumMax/6.0)
print "Average of Maxlist is",SumMaxAvg
sumMin=0
for each in Minlist:
  sumMin+=each
print sumMin
sumMinAvg=float(sumMin/6.0)
print "Average of Minlist is",sumMinAvg





#Tuples
'''35.Create Tuple as specified below 
a) Create a Tuple tup1 with days in a week & print the tuple elements 
b) Create a Tuple tup2 with months in a year and concatenate it with tup1 
c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater. 
d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 Notice the error type you get. 
e) Insert new element in to tuple by typecasting it to List'''
tup1=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
for each in tup1:
  print each
tup2=('January','February','March','April','May','June','July','August','September',
'October','November','December')
tupConcat=tup1+tup2
print "tupConcat=",tupConcat
tup1=(100,9,2,5,3)
tup2=(22,44,20,13,45,9)
tup3=(99,12,34,21,55)
if tup1>tup2 and tup1>tup3:
  print "Tup1 is the biggest"
elif tup2>tup1 and tup2>tup3:
  print "tup2 is the biggest"
else:
  print "tup3 is the biggest of all"
'''del tup1[2]
  Traceback (most recent call last):
  File "python", line 24, in <module>
TypeError: 'tuple' object doesn't support item deletion'''
del tup1
print tup1
'''Traceback (most recent call last):
  File "python", line 29, in <module>
NameError: name 'tup1' is not defined'''
tup2=list(tup2)
tup2.append(323)
print "Tup2 after appending a new item to this by typecasting it to List is",tup2





#Tuples
'''36.Create two tuples tup1 & tup2 and apply all built in functions on tuples. ( Refer Tutorial for the Built in functions list)'''
tup1=('abc',1,3,'123ab','xyz')
tup2=('wer',33,'213erf','rte1',12,123)
print "tup1 is",tup1
print "tup2 is",tup2
print "cmp(tup1,tup2)=",cmp(tup1,tup2)
print "cmp(tup2,tup1)=",cmp(tup2,tup1)
print "Length of tup1 is",len(tup1)
print "Length of tup2 is",len(tup2)
print "Max of tup1 is",max(tup1)
print "Max of tup2 is",max(tup2)
print "Min of tup1 is",min(tup1)
print "Min of tup2 is",min(tup2)
aList = (123, 'xyz', 'zara', 'abc')
aTuple = tuple(aList)
print "Tuple elements are",aTuple





#Dictionary and Date & Time
'''37.Create 3 dictionaries(dict1,dict2,dict3) with 3 elements each. Perform following operations
a) Compare dictionaries to determine the biggest. 
b) Add new elements in to the dictionaries dict1, dict2 
c) print the length of dict1,dict2,dict3. 
d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.'''
dict1={'Empid':12,'Ename':'Vijay','Band':'B1'}
dict2={'Rollno':11,'Name':'Arshiya','Class':7}
dict3={'Kname':'Ashu','Kage':8,'Bgroup':'B+'}
if dict1>dict2 and dict1>dict3:
  print "dict1 is th biggest",dict1
elif dict2>dict1 and dict2>dict3:
  print "dict2 is the biggest",dict2
else:
  print "dict3 is the biggest",dict3
dict1['Experience']=4
dict2['School']='KV bhrukunda'
print "\ndict1 after adding new elements is",dict1
print "\ndict2 after adding new elements is",dict2
print "Length of dict1 is",len(dict1)
print "Length of dict2 is",len(dict2)
print "Length of dict3 is",len(dict3)
dict1Str=str(dict1)
dict2Str=str(dict2)
dict3Str=str(dict3)
dictStr=dict1Str+dict2Str+dict3Str
print "the concatenated dicts as strings all together is",dictStr





#Dictionary and Date & Time
'''38.Create 2 dictionaries as follows 
dict1 ={'Name':'Ramakrishna','Age':25} 
dict2={'EmpId':1234,'Salary':5000} 
Perform following operations 
a) Create single dictionary by merging dict1 and dict2 
b) Update the salary to 10% 
c) Update the age to 26 
d) Insert the new element with key "grade" and assign value as "B1" 
e) Extract and print all values and keys separately. 
f) delete the element with key 'Age' and print dictionary elements.'''
dict1 ={'Name':'Ramakrishna','Age':25} 
dict2={'EmpId':1234,'Salary':5000}
dict1.update(dict2)
print "After merging dict1and dict2, the single dict is",dict1
dict1['Salary']='5500'
print "\nthe dict after updating salary to 10% is now",dict1
dict1['Age']=26
print "\nthe dict after updating age to 26 is now",dict1
dict1['Grade']='B1'
print"\nNow the dict is",dict1
print "The keys of dict separately is",dict1.keys()
print "The values of dict separately is",dict1.values()
del dict1['Age']
print "\nDict after deleting element with key Age is",dict1





#Dictionary and Date & Time
'''39.Using Time and Calendar module ,Print current date and time. Print current month calendar.'''
import time
localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime

import calendar
cal = calendar.month(2017,10)
print "\nHere is the calendar:"
print cal





#Dictionary and Date & Time
'''40.Using time module perform following operations. 
a) Print current time for every 5 seconds up to 1 minute time interval. 
b) Write a program to find out how much CPU time is taken for the execution of above(40.a) program.'''
import time
i=12
while i>0:
  localtime = time.asctime(time.localtime(time.time()))
  print "Local current time :", localtime
  time.sleep(5)
  i=i-1