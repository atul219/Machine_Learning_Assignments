# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:43:39 2018

@author: Atul
"""
import random
import numpy as np
#a="hello atul. Anything new? "


# to generate random word
def word(a,b,string):
    length=random.randint(a,b)                  # to generate random length of word
    #print(length)
    random_word=""
    for i in range(0, length):
        random_word += random.choice(string)    # random selected word
    return random_word    


# to generate random pararaph
def paragraph(x,y,a,b,string):
    ot=random.randint(x+b+1,y)  # length of paragraph(min and max)  (b+1 for not stopping at 75-b)
    #print(length)
    random_paragraph=""
    count=0                         # to check how much characters are in paragraph
    while(count<ot-b-1):        # (b-1 for not exceeding 250 ) (b is length of word)
        if(count!=0):
            random_paragraph=random_paragraph+" " # to give space between two words
            count=count+1           # 1 character for space
        t=word(a,b,string)          # random word
        random_paragraph=random_paragraph+t # random word will be added to random paragraph
        count=count+len(t)          # length of paragraph
    return random_paragraph    
    

string="abcdefghijklmnopqrstuvwxyz"    
data_paragraph=[]            # 1000 paragraph
data_unique_words=[]         # list for unique words in each paragraph       
all_unique_words=[]          #  total unique words in 1000 paragraph  
for i in range(1000): 
    p=paragraph(75,250,2,5,string)  # paragraph will be genrated(min = 75 , max = 250 and lentgh of word min = 2 , max = 10)
    len(p)
    words = p.split(" ")            # to seprate every word of paragraph in single string
    unique_words=np.unique(words)   # to find unique words
    d=np.zeros(len(unique_words))   # dimension of 1 final  paragraph unique words 
    for j in range(len(d)):         # loop to the length of unique words in d
        for k in range(len(words)):  # loop to the length of words in a paragraph
            if (unique_words[j]==words[k]):
                d[j]=d[j]+1         # to check how many times a unique word is in paragraph
                #print(words[k])
    if(i==0):
          data_paragraph=[p]   # adding paragraph to data paragraph becuase in zero list we can do this list.append(x)   
          all_unique_words=unique_words  # total count of unique words in 1000 paragraph
          data_unique_words=[unique_words] # list for unique words in each paragraph
    else:      
        data_paragraph.append(p)
        #data_unique_words=[data_unique_words, unique_words]
        data_unique_words.append(unique_words)
        all_unique_words=np.concatenate((all_unique_words,unique_words))
                
    dim=np.unique(all_unique_words)  # unique words in all unique words   (final dimension)
    
    
dictionary=np.zeros([1000,len(dim)]) # initialize final dictionary of all para
    

for ii in range (1000):               #each para
    current_para=data_paragraph[ii]     
    split_words= current_para.split(" ")
    for jj in range (len(split_words)):    #length of current para
        current_word=split_words[jj]       #each word 
        loc=np.where(dim==current_word)    #loc according to all unique columns in dictionary
        loc=loc[0]                         # to read the value of location(tupple to array)
        loc=loc[0]                         # array to element
        dictionary[ii,loc]=dictionary[ii,loc]+1    # update the value in the dictionary
        
        
        
 # dictionary created


 #%%     
  
# create a new para        
    
new_para=paragraph(75,250,2,5,string)
new_para_encoded=np.zeros([1,len(dim)])
split_encoded_words= new_para.split(" ")
count_ignored=0                                     # count the number of unique words in new para which are not present in dictionary
for kk in range (len(split_encoded_words)):         # each word in the para
        current_encoded_word=split_encoded_words[kk]    # current word
        new_loc=np.where(dim==current_encoded_word)     #loc according to all unique columns in dictionary
        new_loc=new_loc[0]                              # to read the value of location(tupple to array)
        if (np.shape(new_loc)==(0,)):                   # if the word is not present in the dictionary
            print("unique word encountered")
            count_ignored=count_ignored+1
        else:                                           # word present in dictionary                                            
            
            new_loc=new_loc[0]                          # array to element
            new_para_encoded[0,new_loc]=new_para_encoded[0,new_loc]+1  # update the value in the new encoded para
            



# calculate distance from each para 
ui=np.repeat(new_para_encoded,1000,axis=0)     #  repeat matrix 1000 times     
distance=dictionary-ui                         
sq_distance=distance**2                        # square each element of distance                 
total_distance=np.sum(sq_distance,axis=1)       # obtain distance of each para
min_distance=np.min(total_distance)             # obtain min distance 
closest_para=np.where(total_distance==min_distance) # obtain index of the closest para


print(min_distance , closest_para[0])


############################################################### Great Job #######################################################################################################