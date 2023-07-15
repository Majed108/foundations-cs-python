#problem #1

#def getFactorial(n):
    # x = 1
    # for i in range(1,n+1):
    #  x = x*i 
    # return x



#print(getFactorial())

  
################################

#problem #2

#divisorsList = []


#def findDiviser(n):
 # for i in range(1, n+1):
  #  if (n%i==0):
   #   divisorsList.append(i)
 
    

#findDiviser(16)
#print(divisorsList)

#########################################
 

# problem #3

# my answer

#def reverseString(str):
 # for i in range (len(str)):
  #  print(str[len(str) - 1 : : -1])
    
    
#reverseString("hello world")


# google's answer

#def reverseString2(string):
 # reversed_string = ""
 # for i in range(len(string) - 1, -1, -1):
  #  reversed_string += string[i]
  #return reversed_string


#print(reverseString2("hello world"))

###################################################

#problem #4

#evenNumbers = []


#def findEvenNumber(lst):
  #for i in range(lst[0] ,len(lst) + 1,):
   # if (i%2==0):
    
     # evenNumbers.append(i)


#findEvenNumber([1,2])
#print(evenNumbers)
####################################################

# problem #5


#password = input("please enter your password: ")

#import re

#def checkPassword(password):
  #if(len(password) >= 8 and re.search("[A-Z]", password) and re.search("[a-z]", password) and re.search("[0-9]", password) and re.search("[#, ?, !, $]", password) ):
    #print("strong password")
  #else:
   # print("weak password")



#checkPassword(password)

