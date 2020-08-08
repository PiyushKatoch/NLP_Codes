import nltk
import collections as c
import re as regex
#nltk.download('brown')
from nltk.corpus import brown
from nltk.corpus import stopwords 
print("")
print("")

"""
    Brown Corpus has 1161192 words and contains 56067 unique words.
"""

brown_words=list(brown.words())  


#Sentence input
print("Enter the sentence for spell check")
sentence=input()
sen=sentence.split(" ")
print("")
print("Enter value of N to get N-Gram Model")
n=int(input())
print("For MRR calculation we need the correct sentence please enter it :")
c=input()
crr=c.split(" ");




def Ngram_MRR(sen,n,brown_words,crr):

    temp=[]
    for x in sen:
        temp.append(x.lower())
    sen=temp
    
    temp=[]
    for x in brown_words:
        temp.append(x.lower())
    brown_words=temp
    
    temp=[]
    for x in crr:
        temp.append(x.lower())
    crr=temp
    
    
    
    
    #getting bigrams of sentence
    s={}
    for k in sen:
        word_list = []
        for i in range(0, len(k)-1):
            word_list.append(k[i:i+2])
            i+=1
        s.update({k:word_list})
    
    sen_input=s.items()
    
    
    #Getting brown corpus Bigram
    brown_bigrams={}
    
    for i in brown_words:
        w=[]
        for j in range(0, len(i)-1):
           w.append(i[j:j+2])
           j+=1
        brown_bigrams.update({i:w})
        
    corpus=brown_bigrams.items() 
     
    
    
    #Spell check code
    count=0
    print("")
    print("Output :")
    print("")
    
    mrr=[];
    
    for i in sen_input:
           print("Word :",i[0])
           freq={}
           for k in corpus:
              for j in i[1]:
                 if((j in k[1])==True):
                     count=count+1;
              if(count>0):
                  freq.update({k[0]:count})  
                  count=0
           freq_sorted =dict(sorted(freq.items(), key=lambda p: p[1]))
           rev=list(reversed(list(freq_sorted.items())));
          
           flag=0
           match_one_less={}
           match_two_less={}
           x=int(list(rev)[0][1])
           
           for r in rev:
               if((len(i[0])-3)<len(r[0])<(len(i[0])+3)):
                   if(r[1]==x):
                      match_one_less.update({r});
                   if(r[1]==x-1):
                      match_two_less.update({r});
           
           new_mol = {}
           for k in sorted(match_one_less, key=len, reverse=False):
                  new_mol[k] = match_one_less[k]
           
           new_mtl = {}
           for k in sorted(match_two_less, key=len, reverse=False):
                  new_mtl[k] = match_two_less[k]
           
           flag=0
           output={}
           for key, value in new_mol.items() :
               if(flag<(n)):
                   output.update({key:value})
                   flag=flag+1;
               if(flag==n):
                   break;
           left=n-flag;
           x=0
           for key, value in new_mtl.items():
               if(x<left):
                   output.update({key:value})
                   x=x+1;
               if(x==left):
                   break;
           print("Correct word could be :",output);
           position=0
           for key, value in output.items() :
               position=position+1;
               if key in crr:
                   break;
           mrr.append(1/position);
    print(mrr)
    sum=0
    for i in mrr:
        sum=sum+i;
    print("MRR for given Query : ",(sum/len(mrr)));
    return (sum/len(mrr));
    
def Ngram_MRR_nonConstrained(sen,n,brown_words,crr):

    temp=[]
    for x in sen:
        temp.append(x.lower())
    sen=temp
    
    temp=[]
    for x in brown_words:
        temp.append(x.lower())
    brown_words=temp
    
    temp=[]
    for x in crr:
        temp.append(x.lower())
    crr=temp
    
    
    
    
    #getting bigrams of sentence
    s={}
    for k in sen:
        word_list = []
        for i in range(0, len(k)-1):
            word_list.append(k[i:i+2])
            i+=1
        s.update({k:word_list})
    
    sen_input=s.items()
    
    #Getting brown corpus Bigram
    brown_bigrams={}
    
    for i in brown_words:
        w=[]
        for j in range(0, len(i)-1):
           w.append(i[j:j+2])
           j+=1
        brown_bigrams.update({i:w})
        
    corpus=brown_bigrams.items() 
     
    
    
    #Spell check code
    count=0
    print("")
    print("Output :")
    print("")
    
    mrr=[];
    
    for i in sen_input:
           print("Word :",i[0])
           freq={}
           for k in corpus:
              for j in i[1]:
                 if((j in k[1])==True):
                     count=count+1;
              if(count>0):
                  freq.update({k[0]:count})  
                  count=0
           freq_sorted =dict(sorted(freq.items(), key=lambda p: p[1]))
           rev=list(reversed(list(freq_sorted.items())));
           
           flag=0
           output={}
           for r in rev:
               flag=flag+1;
               if(flag<=n):
                   output.update({r[0]:r[1]})
               else:
                   break;
           print("Correct word could be :",output);        
           position=0;
           for key, value in output.items() :
               position=position+1;
               if(key in crr):
                   break;
           mrr.append(1/position);
    print(mrr)
    sum=0
    for i in mrr:
        sum=sum+i;
    print("MRR for given Query : ",(sum/len(mrr)))
    return (sum/len(mrr));
    
def start_end_symbol_additions(sen):
    
    new_s=[]
    for x in sen:
        temp='@'+x+'$'
        new_s.append(temp)

    return new_s;

def punc_removal(s):
    #Removal of special characters
    n_s=[]
    bad_char=[';', ':', '!', "*",'.',',','!']
    for x in s:
        for i in x : 
             if i in bad_char:
                 x=x.replace(i,'');
        n_s.append(x);
    return n_s;


 
a=Ngram_MRR(sen,n,brown_words,crr);

b=Ngram_MRR(start_end_symbol_additions(sen),n,start_end_symbol_additions(brown_words),start_end_symbol_additions(crr));
   
c=Ngram_MRR(punc_removal(sen),n,(brown_words),crr);

d=Ngram_MRR(start_end_symbol_additions(punc_removal(sen)),n,start_end_symbol_additions(brown_words),start_end_symbol_additions(crr));



e=Ngram_MRR_nonConstrained(sen,n,brown_words,crr);

f=Ngram_MRR_nonConstrained(start_end_symbol_additions(sen),n,start_end_symbol_additions(brown_words),start_end_symbol_additions(crr));
 
g=Ngram_MRR_nonConstrained(punc_removal(sen),n,(brown_words),crr);

h=Ngram_MRR_nonConstrained(start_end_symbol_additions(punc_removal(sen)),n,start_end_symbol_additions(brown_words),start_end_symbol_additions(crr));

print("Non-Enhanced Ngram Model :") 
print("MRR without any change in input and corpus : ",e); 
print("MRR with addition of start and end symbol to input and corpus : ",f);
print("MRR without any change in input and corpus input and corpus(Punc removal in input) : ",g);
print("MRR with addition of start and end symbol to input and corpus(Punc removal in input) : ",h);


print("Enhanced Ngram Model :")
print("MRR without any change in input and corpus : ",a); 
print("MRR with addition of start and end symbol to input and corpus : ",b); 
print("MRR without any change in input and corpus input and corpus(Punc removal in input) : ",c);
print("MRR with addition of start and end symbol to input and corpus(Punc removal in input) : ",d);
print("")



print("Non-Enhanced Ngram Model :",e," ",f," ",g," ",h);
print("Enhanced Ngram Model :",a," ",b," ",c," ",d);
