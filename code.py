# --------------
#Code starts here
import sys
def palindrome(num):
 numstr = str(num)
 for i in range(num+1,sys.maxsize):
  if str(i) == str(i)[::-1]:
   return i

print(palindrome(12021))



# --------------
#Code starts here
def a_scramble(str_1,str_2):
 result=True
 for i in (str_2.lower()):
  if i not in (str_1.lower()):
   result=False
   break
  str_1=str_1.replace(i,'',1)
 return(result)

  




# --------------
#Code starts here
import math 
def isPerfectSquare(x): 
 s = int(math.sqrt(x)) 
 return s*s == x 
 s = int(math.sqrt(x)) 
 return s*s == x 

def check_fib(num):
   return isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4)

print(check_fib(145))


# --------------
#Code starts here
def compress(word):
 word=word.lower()
 mist=[]
 l=0
 while(l<len(word)):
  m=word[l]
  j=0
  while(l<len(word) and word[l]==m):
   j=j+1
   l=l+1    

  mist.append(m)
  mist.append(str(j))
    
 return ''.join(mist)



# --------------
#Code starts here
def k_distinct(string,k):
 s_list=(set(string.lower()))
 return len(s_list)>=k


