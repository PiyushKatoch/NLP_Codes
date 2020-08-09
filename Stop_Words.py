import nltk
import collections as c
import re as regex
nltk.download('brown')
from nltk.corpus import brown
from nltk.corpus import stopwords 


brown_words=list(brown.words())
 

bad_chars = ['\'','(' ,'' ,'.' ,')' , ',' ,'?' , '\'\'' ,':',';']


brown_split=[]
for x in brown_words:
    x=regex.split(', |_|-|!|\'',x)
    if len(x)<1:
      for i in x:
        if not i in bad_chars:
            x= ''.join(i)
        else: 
            break
      brown_split.append(x.lower())
    else:
       for j in x: 
         if not j in bad_chars:
           brown_split.append(j.lower())
   
    


brown_dict=dict(c.Counter(brown_split))  
brown_sorted =dict(sorted(brown_dict.items(), key=lambda x: x[1]))
stop_words =list(stopwords.words('english'))



'''This code here was used to find the Threashold doing the following:
    
     1)Get the Total number of stop words in the corpus.
'''
    
total_stop=0
for i in brown_sorted:
   for j in range(0,len(stop_words)):
       if i==stop_words[j]:
           total_stop+=1

            
   ''' 2) Create a set of last n elements in sorted ascending corpus.
         n = number of stops elements in brown corpus.
         Threshold frequency will be equal to nth frequency from the 
         last.
   '''
           

rev=list(reversed(list(brown_sorted)));
Threshold=(brown_sorted[rev[total_stop]])
   



Obs_stops=[]
for i in brown_sorted:
    if brown_sorted[i]>=Threshold:
        Obs_stops.append(i)
        


count=0
for i in range(0,len(Obs_stops)):
    for j in range(0,len(stop_words)):
        if Obs_stops[i]==stop_words[j]:
            count+=1

print('Brown Corpus has ',len(brown_split),' words and contains ',len(brown_sorted),' unique words') 
print('Brown Corpus has ',total_stop,' stop words of the 179 stop words in English Language')
print(count,'/',total_stop,' stop words found in the last ',total_stop,' words of sorted brown corpus.')
print('Overlap Percentage = ',(count/(len(Obs_stops)))*100,' %.')
        

"""
Observations Made :
    1) NLTK class has a total of 179 stop words.
    2)Machine was not able to plot bar graph for brown corpus as number of unique
      words ,so in order to get the Threshold value I used another method mentioned 
      above in the code.
      
Result 1: Without removal of Special Characters.
    Brown Corpus has 1161192 words and contains 56067 unique words.
    Brown Corpus has 155 stop words of the 179 stop words in English Language.
    90 / 155 stop words found in the last 155 words of sorted brown corpus.
    Overlap Percentage =  57.692307692307686 %.

Result 2: With removal of Special Characters.
    Brown Corpus has  1040623  words and contains  43375  unique words
    Brown Corpus has  151  stop words of the 179 stop words in English Language
    99 / 151  stop words found in the last  151  words of sorted brown corpus.
    Overlap Percentage =  65.13157894736842  %.
   
Conclusion : When special characters were removed (especially ' ) new stop words
             like 'll','re','ve','t','d','s' came into existence so the number of 
             stop words in brown corpus changes.


"""
