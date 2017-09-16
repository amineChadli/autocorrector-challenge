# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:27:40 2017

@author: amine
"""
'''bless your autocorrect'''


'''this function test if a string ch1 start with another string ch2'''
def start_with(ch1,ch2):
  #if the length of the second string is greater thant the length of the first one then we return false
  if(len(ch2)>len(ch1)):
    return False
  #else and if the fist string ch1 starts with the second string then we return true
  if(ch1[:len(ch2)]==ch2):
    return True
  #else we return false
  return False
  

'''this function get the minimum triplet in a list
using this order : (a,b,c) < (e,f,g) <--> b < f
in our case b and f represent the difference between each string in the dictionnary and the word we look for '''
def get_min(L):
  c = (200,200,200)
  for i in range(len(L)):
    a = L[i]
    if(a[1] < c[1] ):
      c = a 
  return c
'''this function get the difference between two string by computer only the number of letters in the first string that are not in the second with the condition that ch1 start with ch2
'''
def dif_right(ch1,ch2):
  q = 1
  while(ch1[:q]==ch2[:q] and q<=min(len(ch1),len(ch2))):
    q+=1
  return len(ch1) - (q-1)
'''the function do the same thing as the function dif_right but by getting the max difference between the two strings'''
def dif(ch1,ch2):
  q = 1
  while(ch1[:q]==ch2[:q] and q<=min(len(ch1),len(ch2))):
    q+=1
  return max(len(ch1),len(ch2)) - (q-1)
'''and this is a function that returns a new_word from the previous word , a list of elemens and the number of buttons we clicked'''
def compare(dict,word):
    sum=0
    size = len(word)
    #L=np.zeros(size)
    L=[]
    M=[]
    
    i = 1
    ch = " "
    while(i<=size):
      ch = word[:i]
      for j in range(0,len(dict)):
        if(start_with(dict[j],ch)):
          if (j in M) : 
            break
          L.append((i,i+dif(word,dict[j]),j))
          M.append(j)
          break
      i+=1
    if(len(L)==0):
      min = len(word)
      sum+=min
      return "",[],sum
    else : 
      c = get_min(L)
      #print("c[2]" ,dict[c[2]])
      sum+=c[0]+1
      K = []
      dif_r=dif_right(dict[c[2]],word)
      c_2 = len(dict[c[2]]) - dif_r
      sum+=dif_r
      for k in range(len(M)):
        new_member = dict[M[k]][c_2:]
        if(new_member!=""):
          K.append(new_member)
      return word[c_2:],K,sum
   
sum = 0    
dict = []
s=raw_input("")
n = int(s[0])
m = int(s[2])
for i in range(0,n):
    elm = input("")
    dict.append(elm)
words=[]
for j in range(0,m):
    word = input("")
    words.append(word)
for j in range(0,m):
    init_word=words[j]
    word = words[j]
    dicto=dict
    sum = 0
    while(word!=""):
          
       word,dicto,l = compare(dicto,word)
       sum+=l
    print(min(sum,len(init_word)))
    


