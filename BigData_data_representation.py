#!/usr/bin/env python
# coding: utf-8

# In[173]:


import pprint
import requests     # 2.19.1
secret = "----"

# Define the endpoint
url = 'https://newsapi.org/v2/everything?'

# Specify the query and number of returns
parameters = {
    'q': 'merkel', # query phrase
    'pageSize': 100,  # maximum is 100
    'apiKey': secret # your own API key
}

# Make the request
response = requests.get(url, params=parameters)

# Convert the response to JSON format and pretty print it
response_json = response.json()
pprint.pprint(response_json)


# In[174]:


for i in response_json['articles']:
    print(i['title'])


# In[175]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create an empty string
text_combined = ''
# Loop through all the headlines and add them to 'text_combined' 
for i in response_json['articles']:
    if i['description'] != None:
        text_combined += i['description'] + ' ' # add a space after every headline, so the first and last words are not glued together
# Print the first 300 characters to screen for inspection
#print(text_combined)



# In[176]:


wordcount={}
for word in text_combined.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v, in sorted(wordcount.items(), key=lambda words: words[1], reverse = True):
    print(k,v)


# In[177]:


wordcloud = WordCloud(max_font_size=40).generate(text_combined)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# In[204]:


# initializing bad_chars_list 
bad_words = ["a", "the" , "of", "in", "to", "and", "on", "de", "with", 
             "by", "at", "dans", "ont", "été", "les", "des", "au", "et", 
             "après", "avec", "qui", "par", "leurs", "ils", "a", "pour", 
             "les", "on", "as", "france", "eux", "où", "son", "le", "la",
             "en", "with", "is", "has", "for", "that", "an", "but", "be", 
             "are", "du", "it", "à", "had", "ist", "Der", "um", "zu", "den", 
             "der", "-", "und", "für", "Die", "von", "als",
             "sich", "nicht", "nach", "auch"  ] 


# In[205]:


r = text_combined.replace('\s+', ' ').replace(',', ' ').replace('.', ' ')
words = r.split()
rst = [word for word in words if ( word.lower() not in bad_words and len(word) > 3) ]
rst = ' '.join(rst)

wordcount={}
for word in rst.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v, in sorted(wordcount.items(), key=lambda words: words[1], reverse = True):
    print(k,v)


# In[206]:


word = WordCloud(max_font_size=40).generate(rst)
plt.figure()
plt.imshow(word, interpolation="bilinear")
plt.axis("off")
plt.show()


# In[200]:


# Create an empty string
title_combined = ''
# Loop through all the headlines and add them to 'text_combined' 
for i in response_json['articles']:
    title_combined += i['title'] + ' ' # add a space after every headline, so the first and last words are not glued together
# Print the first 300 characters to screen for inspection
#print(text_combined[0:300])


# In[217]:



titles = title_combined.replace('\s+', ' ').replace(',', ' ').replace('.', ' ')
words_t = titles.split()
result = [word for word in words_t if ( word.lower() not in bad_words and len(word) > 3) ]
result = ' '.join(result)

wordcount={}
for word in result.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v, in sorted(wordcount.items(), key=lambda words: words[1], reverse = True):
    print(k,v)


# In[218]:


wordcloud = WordCloud(max_font_size=40).generate(result)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


# In[ ]:




