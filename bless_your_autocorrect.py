# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:27:40 2017

@author: amine
"""
'''bless your autocorrect'''

# this function get the minimum triplet in a list
# using this order : (a,b,c) < (e,f,g) <--> b < f
# in our case b and f represent the difference between each string in the dictionnary and the word we look for 
def get_min_triplet(L):
  return min(L, key = lambda x: x[1])

# this function retuns the number of letters from the second string that are in the begining of the first string
def get_num_similar(ch1,ch2):
  q = 1
  while(ch1[:q]==ch2[:q] and q<=min(len(ch1),len(ch2))):
    q+=1
  return (q-1)
      
# this function get the difference between two string by computing only the number of letters 
# in the first string that are not in the second with the condition that ch1 start with ch2
def dif_right(ch1,ch2):
  return len(ch1) - get_num_similar(ch1,ch2)

# this function do the same thing as the function dif_right but it returns the maximum difference between the two strings'''
def dif(ch1,ch2):
  return max(len(ch1),len(ch2)) - get_num_similar(ch1,ch2)

def get_list_scores(dict,word):
    word_size = len(word)
    list_scores = []
    i = 1
    
    while(i<=word_size):
      ch = word[:i]
      for j in range(0,len(dict)):
        if(dict[j].startswith(ch)):
          list_scores.append((i,i+dif(word,dict[j]),j))
          break
      i+=1

    return list_scores

'''and this is a function that returns a new_word from the previous word , a list of elemens and the number of keywords we pressed'''
def compare(dict,word):
    
    list_scores = get_list_scores(dict,word)

    if(len(list_scores)==0):
      nb_total_keys = len(word)
      return "",[],nb_total_keys
    
    else : 
      nb_total_keys = 0
      score_triplet = get_min_triplet(list_scores)
      #print("c[2]" ,dict[c[2]])
      nb_before_tab = score_triplet[0]
      nb_total_keys += nb_before_tab + 1
      
      close_word_index = score_triplet[2]
      close_word = dict[close_word_index]

      difference_right = dif_right(close_word,word)
      nb_total_keys += difference_right

      shared_keys  = len(close_word) - difference_right
      new_dict = []
      for k in range(len(list_scores)):
        close_word_index = list_scores[k][2]
        new_member = dict[close_word_index][shared_keys:]
        if(new_member!=""):
          new_dict.append(new_member)
      return word[shared_keys:],new_dict,nb_total_keys
   
def get_min_keys_number(dicto, word):
    word_0 = word
    nb_total_keys = 0
    while(word!=""):
       word,dicto,nb_keys = compare(dicto,word)
       nb_total_keys+=nb_keys
    return min(nb_total_keys,len(word_0))
      
# main
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
    word = words[j]
    dicto=dict
    print(get_min_keys_number(dicto,word))
    


